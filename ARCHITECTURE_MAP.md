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
│   └── app/
│       ├── api/v1/
│       │   ├── router.py       # защищённый v1 router с auth endpoints
│       │   └── endpoints/
│       │       ├── auth.py     # nonce, verify, me, logout
│       │       └── users.py
│       ├── core/
│       │   ├── config.py
│       │   └── security.py
│       ├── db/
│       │   ├── base.py         # регистрация ORM metadata
│       │   ├── base_class.py   # declarative Base
│       │   ├── cache.py        # Redis/Dragonfly client
│       │   └── session.py      # sync engine, SessionLocal, get_db
│       ├── models/
│       │   └── user.py         # wallet identity, UUID v7
│       ├── schemas/
│       │   └── user.py         # SIWE/auth API contracts
│       └── services/
│           ├── auth_service.py # nonce, sessions, auto-registration
│           └── siwe.py         # EIP-4361 parsing and signature recovery
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
│       ├── utils/backend.ts    # Nitro → FastAPI proxy
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
- Wallet auth page, клиентский `useApi` и marketplace-роуты ещё не реализованы.

## Что осталось от старого проекта

| Файл/участок | Наследие | Действие для Classifyd |
|---|---|---|
| `backend/main.py` | `Classifyd API`, защищённый v1 router и health | Добавить marketplace-роуты |
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

Следующий приоритет вертикали: wallet auth page/useApi → Listing/Deal.
