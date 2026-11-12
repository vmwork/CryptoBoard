# FRONTEND_MAP

## Theme defaults
- `frontend/app/composables/useTheme.ts` — централизованная логика выбора темы, чтение/запись `classifyd_theme` и применение классов `dark/light` на `html`/`body`.
- `frontend/app/app.vue` — подключение `useTheme` и синхронизация `htmlAttrs`/`bodyAttrs`, чтобы `dark` был установлен по умолчанию и реагировал на переключение.
- `frontend/app/components/landing/LandingHeader.vue` — добавлен переключатель (иконка солнца/луны) с доступным лейблом и вызовом `toggleTheme`; шапка сохраняет светлые цвета в тёмной теме.
- `frontend/app/components/landing/LandingFeatures.vue` — секция и карточки теперь используют `dark:` модификаторы, чтобы оставаться белыми/яркими в тёмной теме.
- `frontend/app/components/landing/LandingHero.vue` — заголовки, описания и кнопки поддерживают светлый текст в режиме `dark`, а призывы к действию теперь разделяют одинаковый эффект hover/scale+translate, чтобы интерфейс чувствовался единообразным и легко читаемым.
- `frontend/app/components/landing/LandingFAQ.vue` — секция, заголовки, карточки и ответы теперь получают `dark:`-стили, чтобы вся информация была чёткой на тёмном фоне без потери дизайна.
- `frontend/app/layouts/landing.vue` — размещён `OnboardingModal` в лейауте; тёмная обёртка дизайнерских блоков уже рассчитывает на существующий `dark` класс.

## Onboarding modal
- `frontend/app/components/OnboardingModal.vue` — центровая модалка с карточкой сделки #421, прогресс-баром 75%, пояснением работы эскроу и кнопкой «Понятно / Начать»; сохраняет флаг `classifyd_onboarded` в `localStorage` и открывается только при первом визите.
