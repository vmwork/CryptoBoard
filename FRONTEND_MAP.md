# FRONTEND_MAP

## Theme defaults
- `frontend/app/composables/useTheme.ts` — централизованная логика выбора темы, чтение/запись `classifyd_theme` и применение классов `dark/light` на `html`/`body`.
- `frontend/app/app.vue` — подключение `useTheme` и синхронизация `htmlAttrs`/`bodyAttrs`, чтобы `dark` был установлен по умолчанию и реагировал на переключение.
- `frontend/tailwind.config.ts` — Tailwind расширен цветами, основанными на CSS-переменных (например, `background`, `foreground`, `card`, `border`, `muted-foreground`), что позволяет использовать классы вроде `text-foreground`, `bg-card`, `border-border` и автоматически переключать цвета вместе с `dark` классом.
- `frontend/app/components/landing/LandingHeader.vue` — добавлен переключатель (иконка солнца/луны) с доступным лейблом и вызовом `toggleTheme`; шапка сохраняет светлые цвета в тёмной теме.
- `frontend/app/components/landing/LandingHero.vue` — заголовки, описания и кнопки опираются на токены (`text-foreground`, `text-muted-foreground`, `border-border`, `bg-background`), чтобы текст всегда оставался читабельным, сохраняя яркость градиента.
- `frontend/app/components/IconNft.vue` — новый локальный компонент, рисующий NFT-символ с контуром и буквами, которые всегда используют `currentColor`, улучшая контраст на тёмных блоках лендинга.
- `frontend/app/components/landing/LandingFeatures.vue` — секция и карточки используют `bg-card`, `text-card-foreground` и `text-muted-foreground` для стабильной типографики на любых фонах.
- `frontend/app/components/landing/LandingFAQ.vue` — FAQ секция и аккордеон переключаются на `border-border`/`bg-card`, а вопросы и ответы рендерятся через `text-foreground`/`text-muted-foreground`.
- `frontend/app/components/landing/LandingFooter.vue` — подвал применяет `border-border`, `bg-card`, `text-muted-foreground` и `text-foreground` для ссылок, логотип налажен на `currentColor`.
- `frontend/app/layouts/landing.vue` — размещён `OnboardingModal` в лейауте; тёмная обёртка дизайнерских блоков уже рассчитывает на существующий `dark` класс.

## Onboarding modal
- `frontend/app/components/OnboardingModal.vue` — центровая модалка с карточкой сделки #421, прогресс-баром 75%, пояснением работы эскроу и кнопкой «Понятно / Начать»; сохраняет флаг `classifyd_onboarded` в `localStorage` и открывается только при первом визите.

## Pages
- `frontend/app/pages/faq.vue` — теперь рендерит `LandingFAQ`, чтобы публичный FAQ всегда использовал одни и те же акценты, границы и чтение текста, что и секция на главной.
- `frontend/app/pages/terms.vue` и `frontend/app/pages/privacy.vue` — переписаны под темы: корневая обёртка, карточки, списки, заголовки и контактные блоки используют `bg-background`, `bg-card`, `border-border`, `text-foreground` / `text-muted-foreground`, чтобы страницы оставались читаемыми при включённой тёмной теме.
- `frontend/app/pages/support.vue` — приоритетные радиокнопки теперь используют `accent-primary`/`focus:ring-primary`, а сообщения об успехе и ошибке получили тёмные оттенки (`bg-emerald-900/30`, `bg-red-900/30`) с тонкими рамками, чтобы вписаться в палитру.
