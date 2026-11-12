<template>
    <section class="border-t border-neutral-200/50 bg-neutral-50/50 px-4 py-24 sm:px-6 sm:py-32 lg:px-8 dark:border-white/20 dark:bg-white/90">
        <div class="mx-auto max-w-7xl">
            <!-- Заголовок -->
            <div class="text-center">
                <h2 class="text-3xl font-bold text-neutral-900 sm:text-4xl lg:text-5xl dark:text-neutral-900">
                    Почему <span class="text-primary">CryptoBoard</span>?
                </h2>
                <p class="mx-auto mt-4 max-w-2xl text-lg text-neutral-600 dark:text-neutral-700">
                    Все, что нужно для безопасной и выгодной торговли
                </p>
            </div>

            <!-- Сетка преимуществ -->
            <div class="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
                <!-- Смарт-контракты -->
                <div
                    class="group rounded-2xl border border-neutral-200 bg-white p-6 text-neutral-900 transition hover:border-primary/30 hover:shadow-lg dark:border-white/20 dark:bg-white/90 dark:text-neutral-900">
                    <div class="mb-4 inline-flex rounded-lg bg-primary/10 p-3 text-primary group-hover:bg-primary/20 dark:bg-primary/20">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
                            class="h-6 w-6">
                            <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2" />
                            <path d="M9 8H15" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M9 12H13" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M9 16H11" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                        </svg>
                    </div>
                    <h3 class="text-lg font-semibold text-neutral-900 dark:text-neutral-900">Смарт-контракты</h3>
                    <p class="mt-2 text-sm text-neutral-600 dark:text-neutral-700">
                        Все средства замораживаются на смарт-контракте до подтверждения получения.
                    </p>
                </div>

                <!-- Без комиссий -->
                <div
                    class="group rounded-2xl border border-neutral-200 bg-white p-6 text-neutral-900 transition hover:border-primary/30 hover:shadow-lg dark:border-white/20 dark:bg-white/90 dark:text-neutral-900">
                    <div class="mb-4 inline-flex rounded-lg bg-primary/10 p-3 text-primary group-hover:bg-primary/20 dark:bg-primary/20">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
                            class="h-6 w-6">
                            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
                            <path d="M8 8L16 16" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M16 8L8 16" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                        </svg>
                    </div>
                    <h3 class="text-lg font-semibold text-neutral-900 dark:text-neutral-900">Без комиссий</h3>
                    <p class="mt-2 text-sm text-neutral-600 dark:text-neutral-700">
                        Платишь только за газ сети. Мы не берем процент со сделок.
                    </p>
                </div>

                <!-- Мгновенные сделки -->
                <div
                    class="group rounded-2xl border border-neutral-200 bg-white p-6 text-neutral-900 transition hover:border-primary/30 hover:shadow-lg dark:border-white/20 dark:bg-white/90 dark:text-neutral-900">
                    <div class="mb-4 inline-flex rounded-lg bg-primary/10 p-3 text-primary group-hover:bg-primary/20 dark:bg-primary/20">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
                            class="h-6 w-6">
                            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
                            <path d="M12 6V12L16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3 class="text-lg font-semibold text-neutral-900 dark:text-neutral-900">Мгновенные сделки</h3>
                    <p class="mt-2 text-sm text-neutral-600 dark:text-neutral-700">
                        Встроенный P2P-чат и кнопка "Принять" в один клик.
                    </p>
                </div>

                <!-- Токенизация сделок -->
                <div
                    class="group rounded-2xl border border-neutral-200 bg-white p-6 text-neutral-900 transition hover:border-primary/30 hover:shadow-lg dark:border-white/20 dark:bg-white/90 dark:text-neutral-900">
                    <div class="mb-4 inline-flex rounded-lg bg-primary/10 p-3 text-primary group-hover:bg-primary/20 dark:bg-primary/20">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
                            class="h-6 w-6">
                            <path
                                d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"
                                stroke="currentColor" stroke-width="2" stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3 class="text-lg font-semibold text-neutral-900 dark:text-neutral-900">Токенизация сделок</h3>
                    <p class="mt-2 text-sm text-neutral-600 dark:text-neutral-700">
                        Каждая успешная сделка генерирует уникальный NFT-сертификат.
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>