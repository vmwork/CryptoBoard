<template>
    <section class="border-t border-neutral-200/50 bg-neutral-50/50 px-4 py-24 sm:px-6 sm:py-32 lg:px-8">
        <div class="mx-auto max-w-7xl">
            <!-- Заголовок -->
            <div class="text-center">
                <h2 class="text-3xl font-bold text-neutral-900 sm:text-4xl lg:text-5xl">
                    Почему <span class="text-primary">CryptoBoard</span>?
                </h2>
                <p class="mx-auto mt-4 max-w-2xl text-lg text-neutral-600">
                    Все, что нужно для безопасной и выгодной торговли.
                </p>
            </div>

            <!-- Сетка преимуществ -->
            <div class="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
                <div v-for="feature in features" :key="feature.title"
                    class="group rounded-2xl border border-neutral-200 bg-white p-6 transition hover:border-primary/30 hover:shadow-lg">
                    <div class="mb-4 inline-flex rounded-lg bg-primary/10 p-3 text-primary group-hover:bg-primary/20">
                        <span class="text-2xl">{{ feature.icon }}</span>
                    </div>
                    <h3 class="text-lg font-semibold text-neutral-900">{{ feature.title }}</h3>
                    <p class="mt-2 text-sm text-neutral-600">{{ feature.description }}</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
const features = [
    {
        icon: '🔒',
        title: 'Смарт-контракты',
        description: 'Все средства замораживаются на смарт-контракте до подтверждения получения.'
    },
    {
        icon: '🤝',
        title: 'Без комиссий',
        description: 'Платишь только за газ сети. Мы не берем процент со сделок.'
    },
    {
        icon: '⚡️',
        title: 'Мгновенные сделки',
        description: 'Встроенный P2P-чат и кнопка "Принять" в один клик.'
    },
    {
        icon: '🏆',
        title: 'Токенизация сделок',
        description: 'Каждая успешная сделка генерирует уникальный NFT.'
    }
]
</script>