# Classifyd — реальная карта архитектуры

Снимок: 2026-11-11. Описано фактическое состояние, а не целевая архитектура.

## Реальное дерево директорий

```text
CryptoBoard/
├── docker-compose.yml          # PostgreSQL 15, Dragonfly, backend, frontend, Caddy
├── Caddyfile                   # localhost и dev.localhost; reverse proxy
├── Dockerfile                  # образ backend
├── backend/
│   ├── main.py                 # Classifyd API, v1 router, GET /health
│   ├── requirements.txt
│   ├── alembic.ini
│   ├── alembic/                # конфигурация миграций
│   │   └── versions/           # 0001 users; 0002 listings/waitlist/votes
│   └── app/
│       ├── api/
│       │   ├── dependencies.py # DB, cache и SIWE current-user dependencies
│       │   └── v1/
│       │       ├── router.py   # защищённый v1 router: auth, listings, waitlist
│       │       └── endpoints/
│       │           ├── auth.py     # nonce, verify, me, logout
│       │           ├── users.py
│       │           ├── listings.py # публичная витрина и защищённый CRUD
│       │           └── waitlist.py # waitlist, token votes, stats
│       ├── core/
│       │   ├── config.py
│       │   └── security.py
│       ├── db/
│       │   ├── base.py         # регистрация ORM metadata
│       │   ├── base_class.py   # declarative Base
│       │   ├── cache.py        # Redis/Dragonfly client
│       │   └── session.py      # sync engine, SessionLocal, get_db
│       ├── models/
│       │   ├── user.py         # wallet identity, UUID v7
│       │   ├── listing.py      # Listing, enums, JSONB images, Numeric price
│       │   └── waitlist.py     # FeatureWaitlist и TokenVote
│       ├── schemas/
│       │   ├── user.py         # SIWE/auth API contracts
│       │   ├── listing.py      # public/owner DTO, create/update/pagination
│       │   └── waitlist.py     # enrollment, vote и stats contracts
│       └── services/
│           ├── auth_service.py # nonce, sessions, auto-registration
│           ├── siwe.py         # EIP-4361 parsing and signature recovery
│           ├── listing_service.py # CRUD, тарифные лимиты, RPC/cache
│           └── waitlist_service.py # идемпотентность, голоса, счётчики
├── frontend/
│   ├── nuxt.config.ts          # Nuxt, Tailwind Vite plugin, shadcn-nuxt
│   ├── Dockerfile
│   ├── package.json
│   ├── app/
│   │   ├── app.vue
│   │   ├── assets/css/tailwind.css
│   │   ├── components/         # dashboard, landing и shadcn/ui-компоненты
│   │   ├── layouts/{default,landing}.vue
│   │   ├── lib/utils.ts
│   │   └── pages/
│   │       ├── index.vue
│   │       ├── auth/index.vue
│   │       ├── dashboard/index.vue
│   │       └── {faq,privacy,support,terms}.vue
│   └── server/
│       ├── api/auth/           # nonce.post, verify.post, me.get, logout.post
│       ├── api/listings/       # публичные GET и SIWE POST/PATCH/DELETE handlers
│       ├── api/waitlist/       # enrollment, vote и stats handlers
│       ├── utils/backend.ts    # Nitro → FastAPI proxy, session/query/status forwarding
│       └── tsconfig.json
└── ARCHITECTURE_MAP.md
```

Важные фактические расхождения с целевой схемой:

- Backend находится в `backend/app/...`, а не в `backend/models`, `backend/apis` или `backend/services`.
- `frontend/server/api/auth/` и общий BFF-прокси реализованы; клиентский `useApi` пока отсутствует.
- `frontend/i18n/locales/` отсутствует; `@nuxtjs/i18n` не подключён в `nuxt.config.ts`.
- `frontend/app/composables/` и `frontend/app/stores/` не найдены.
- Redis/Dragonfly используется backend для одноразовых SIWE nonce и stateful-сессий.

## Сквозная цепочка запроса

### Что работает сейчас

```text
Браузер → Caddy :80/:443 → classifyd_frontend:3000 (Nuxt SSR/страницы и /api/...)
                       ↘ /api/uploads/* → classifyd_api:8000 (strip_prefix /api)
Nitro /api/auth/* → FastAPI /api/v1/auth/* → PostgreSQL + Dragonfly
Nitro /api/listings/* → FastAPI /api/v1/listings/* → PostgreSQL
Nitro /api/waitlist/* → FastAPI /api/v1/waitlist/* → PostgreSQL
FastAPI main.py → GET /health → {"status":"ok"}
```

- Compose передаёт frontend `NUXT_API_BASE=http://classifyd_api:8000` и публичный API base.
- PostgreSQL доступен backend как `postgres:5432`; Dragonfly задан через `REDIS_URL=redis://classifyd_cache:6379`.
- Production-ресурсы используют префикс `classifyd_*`, dev-ресурсы — `classifyd_dev_*`; БД по умолчанию — `classifyd_db` и `classifyd_dev_db`.
- Внутренние порты production-сервисов используют `expose`; наружу публикует порты только Caddy. Host-порты dev/local остаются в соответствующих контурах.
- Caddy не проксирует `/api/v1/*`, `/docs` и `/openapi.json` напрямую; кроме uploads, весь внешний трафик идёт в Nuxt/Nitro.

### Реализованная SIWE-цепочка

```text
Кошелёк → Nitro /api/auth/nonce → FastAPI → Dragonfly (nonce, TTL 5 минут)
Кошелёк → Nitro /api/auth/verify → FastAPI → eth-account + PostgreSQL + Dragonfly
Браузер ← httpOnly; Secure; SameSite=Strict session cookie ← Nitro
Браузер → Nitro /api/auth/me|logout → FastAPI → Dragonfly (session, TTL 7 дней)
```

- Весь v1 router требует `X-Internal-Bff-Secret`; `/health` остаётся публичным.
- Nonce атомарно потребляется один раз; сессия подписывается HMAC и не является JWT.
- Внутренний `session_id` не возвращается браузеру в JSON.
- Wallet auth page и клиентский `useApi` ещё не реализованы; marketplace API уже доступен через Nitro BFF.

### Этап 3: Listings, Feature Waitlist и Token Votes

- Добавлены UUIDv7-модели `Listing`, `FeatureWaitlist` и `TokenVote`; миграция `0002_create_listings_and_waitlist` создаёт таблицы, enum-типы, ограничения и индексы. Смарт-контракты и escrow в этом этапе не используются.
- `Listing` связан с `users.id`, содержит категории `gpu/cpu/ram/mining/smartphone/other`, состояния `new/used/refurbished`, статусы `active/reserved/sold/archived`, `price_usdt Numeric(12,2)` и JSONB-список изображений.
- Публичные `GET /api/listings` и `GET /api/listings/{id}` поддерживают фильтры `category`, `condition`, `min_price`, `max_price` и пагинацию. В списке видны только активные лоты; архивная карточка возвращает 404. Публичные DTO не содержат `seller_id` и `serial_number`.
- `POST /api/listings`, `PATCH /api/listings/{id}` и `DELETE /api/listings/{id}` требуют активную SIWE-сессию и проверяют владельца. DELETE выполняет soft deletion через статус `archived`.
- При создании или повторной активации действуют лимиты: 10 активных лотов с Seller Passport и 3 без него. Для пользователя без Passport проверяется исходящая активность кошелька через `eth_getTransactionCount` (`latest`, `EVM_RPC_URL`); результат кэшируется в Dragonfly на 24 часа. Нулевой nonce даёт `403 PASSPORT_REQUIRED`, ошибки RPC — `503 RPC_UNAVAILABLE`.
- `POST /api/waitlist` поддерживает анонимную запись по wallet или SIWE-идентичность с защитой от mismatch; повторная запись той же пары wallet/feature идемпотентна. `POST /api/waitlist/vote` требует SIWE, допускает один голос пользователя за `USDC`, `TON`, `WBTC` или `SOL`; `GET /api/waitlist/stats` возвращает счётчики.
- Тонкие Nitro handlers находятся в `frontend/server/api/listings/` и `frontend/server/api/waitlist/`; они передают в FastAPI внутренний BFF secret, разрешённые query/body и SIWE-cookie только для защищённых операций. Успешные create/waitlist/vote возвращают 201, DELETE — пустой 204.

### Этап 4: Telegram и привязка кошелька

- [backend/app/models/user.py](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/backend/app/models/user.py) расширяет профиль: `wallet_address` nullable и хранится в lowercase с уникальным индексом, добавлены поля `telegram_id`/`telegram_username`/`first_name`/`avatar_url` и контрольная проверка `wallet_address IS NOT NULL OR telegram_id IS NOT NULL`.
- [backend/app/services/telegram_auth.py](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/backend/app/services/telegram_auth.py) валидирует `initData` и payload Login Widget (HMAC-SHA256 второй стадии, 15-минутное `auth_date`, `start_param` referral) с настройками `TELEGRAM_BOT_TOKEN`/`USERNAME` из [backend/app/core/config.py](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/backend/app/core/config.py).
- [backend/app/services/auth_service.py](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/backend/app/services/auth_service.py) совместно с [backend/app/api/v1/endpoints/auth.py](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/backend/app/api/v1/endpoints/auth.py) открывают `/api/v1/auth/telegram/webapp` и `/api/v1/auth/telegram/widget`, создают или ищут `telegram_id`, применяют `ref_<uuid>` рефералы, записывают `referrer_id`, генерируют stateful-сессию в Dragonfly с TTL `settings.session_ttl_seconds` (7 дней) и подписывают `session_id`, а `/api/v1/auth/link-wallet` защищён SIWE (nonce + подпись) и привязывает кошелёк при отсутствии владельца.
- Nitro BFF-хендлеры `[frontend/server/api/auth/telegram-webapp.post.ts](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/frontend/server/api/auth/telegram-webapp.post.ts)`, `[frontend/server/api/auth/telegram-widget.post.ts](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/frontend/server/api/auth/telegram-widget.post.ts)` и `[frontend/server/api/auth/link-wallet.post.ts](/home/oneway/Desktop/Prodgects/OneWay/CryptoBoard/frontend/server/api/auth/link-wallet.post.ts)` проксируют запросы с `X-Internal-Bff-Secret`, выставляют куку `HttpOnly; Secure; SameSite=Strict` по `config.sessionCookieName`, а `link-wallet.post.ts` ещё и форвардит текущую сессию.

## Что осталось от старого проекта

| Файл/участок | Наследие | Действие для Classifyd |
|---|---|---|
| `backend/main.py` | `Classifyd API`, защищённый v1 router и health | Marketplace-роуты подключены; поддерживать регистрацию новых v1 routers |
| `backend/app/api/v1/endpoints/users.py` | Старый пользовательский CRUD | Переделать под wallet-профиль без email/KYC |
| `backend/app/api/v1/endpoints/auth.py` | Реализован stateful SIWE | Поддерживать вместе с wallet auth page |
| `backend/app/models/user.py` | Реализован wallet identity с UUID v7 | Расширять marketplace-связями по мере необходимости |
| `backend/app/schemas/user.py` | Реализованы SIWE/auth-контракты | Добавить публичный wallet-профиль отдельно |
| `backend/app/core/security.py` | Реализованы BFF secret и HMAC session security | Не переносить секреты в браузер |
| `docker-compose*.yml` | Очищены: ресурсы `classifyd_*`, БД `classifyd_db`, старые JWT/Telegram/admin env удалены | Подключать новые переменные только по мере реализации |
| `Caddyfile` | Upstreams согласованы; прямые API/docs-маршруты закрыты | Добавить Web3/wallet connect-src при необходимости |
| `frontend/app/pages/dashboard/` и dashboard-компоненты | Шаблонная CRM-панель | Заменить кабинетом сделок/объявлений |
| `frontend/app/pages/auth/` | Старая форма входа | Переделать на подключение кошелька и SIWE |
| `frontend/app/components/landing/` | Шаблонный лендинг | Адаптировать тексты и действия под Classifyd |

Следующий приоритет вертикали: wallet auth page/useApi → клиентская витрина Listing → Deal.
