<template>
    <section class="border-t border-neutral-200/50 px-4 py-24 sm:px-6 sm:py-32 lg:px-8 dark:border-white/10 dark:bg-neutral-950 dark:text-white" id="faq">
        <div class="mx-auto max-w-4xl">
            <!-- Заголовок -->
            <div class="text-center">
                <h2 class="text-3xl font-bold text-neutral-900 sm:text-4xl lg:text-5xl dark:text-white">
                    Часто задаваемые <span class="text-primary">вопросы</span>
                </h2>
                <p class="mt-4 text-neutral-600 dark:text-neutral-300">
                    Найди ответ на свой вопрос. Если не нашел — пиши в поддержку
                </p>
            </div>

            <!-- Аккордеон -->
            <div class="mt-12 space-y-4">
                <div v-for="(item, index) in faqItems" :key="index"
                class="rounded-2xl border border-neutral-200 bg-white transition hover:shadow-sm dark:border-white/10 dark:bg-white/5">
                    <button @click="toggleItem(index)"
                    class="flex w-full items-center justify-between gap-4 px-6 py-5 text-left transition hover:text-primary dark:text-white">
                        <div class="flex items-start gap-4">
                            <!-- Иконка вопроса -->
                            <div
                                class="mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-primary/10 text-primary">
                                <svg v-if="item.icon === 'rocket'" width="16" height="16" viewBox="0 0 24 24"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2"
                                        stroke-linejoin="round" />
                                    <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2"
                                        stroke-linejoin="round" />
                                    <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2"
                                        stroke-linejoin="round" />
                                </svg>
                                <svg v-else-if="item.icon === 'coin'" width="16" height="16" viewBox="0 0 24 24"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
                                    <path d="M8 8C8 6 10 5 12 5C14 5 16 6 16 8C16 10 14 11 12 11C10 11 8 10 8 8Z"
                                        stroke="currentColor" stroke-width="2" />
                                    <path
                                        d="M8 16C8 14 10 13 12 13C14 13 16 14 16 16C16 18 14 19 12 19C10 19 8 18 8 16Z"
                                        stroke="currentColor" stroke-width="2" />
                                </svg>
                                <svg v-else-if="item.icon === 'shield'" width="16" height="16" viewBox="0 0 24 24"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12 22C12 22 20 18 20 12V5L12 2L4 5V12C4 18 12 22 12 22Z"
                                        stroke="currentColor" stroke-width="2" stroke-linejoin="round" />
                                    <path d="M9 12L11 14L16 9" stroke="currentColor" stroke-width="2.5"
                                        stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                                <svg v-else-if="item.icon === 'box'" width="16" height="16" viewBox="0 0 24 24"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor"
                                        stroke-width="2" />
                                    <path d="M8 3L8 21" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                                    <path d="M16 3L16 21" stroke="currentColor" stroke-width="2"
                                        stroke-linecap="round" />
                                    <path d="M3 8L21 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                                    <path d="M3 16L21 16" stroke="currentColor" stroke-width="2"
                                        stroke-linecap="round" />
                                </svg>
                                <svg v-else-if="item.icon === 'user'" width="16" height="16" viewBox="0 0 24 24"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="12" cy="8" r="5" stroke="currentColor" stroke-width="2" />
                                    <path d="M3 21C3 16.5817 6.58172 13 11 13H13C17.4183 13 21 16.5817 21 21"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                                </svg>
                                <svg v-else-if="item.icon === 'plus'" width="16" height="16" viewBox="0 0 24 24"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
                                    <path d="M12 8V16" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                                    <path d="M8 12H16" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                                </svg>
                                <!-- Иконка по умолчанию (вопрос) -->
                                <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
                                    <path
                                        d="M9.09 9C9.3251 8.33167 9.78915 7.76811 10.4 7.40913C11.0108 7.05016 11.7289 6.92694 12.4272 7.06487C13.1255 7.2028 13.7588 7.59293 14.2151 8.15705C14.6713 8.72118 14.9169 9.42083 14.91 10.14C14.91 12 12.29 12.75 12.29 12.75"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round" />
                                    <path d="M12 17H12.01" stroke="currentColor" stroke-width="2.5"
                                        stroke-linecap="round" />
                                </svg>
                            </div>
                            <span class="text-base font-medium text-neutral-900 sm:text-lg dark:text-white">{{ item.question }}</span>
                        </div>

                        <!-- Стрелка -->
                        <svg class="h-5 w-5 shrink-0 text-neutral-400 transition-transform duration-300 dark:text-neutral-400"
                            :class="{ 'rotate-180 text-primary': openIndex === index }" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>

                    <!-- Ответ -->
                    <div class="overflow-hidden transition-all duration-300 ease-in-out"
                        :class="openIndex === index ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'">
                        <div class="border-t border-neutral-100 px-6 pb-5 pt-4 text-neutral-600 dark:border-neutral-700 dark:text-neutral-300">
                            {{ item.answer }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
const openIndex = ref<number | null>(null)

const toggleItem = (index: number) => {
    openIndex.value = openIndex.value === index ? null : index
}

const faqItems = [
    {
        icon: 'rocket',
        question: 'Что такое CryptoBoard?',
        answer: 'Это децентрализованная доска объявлений для торговли цифровыми активами. Мы объединяем покупателей и продавцов напрямую, используя смарт-контракты для безопасных сделок.'
    },
    {
        icon: 'coin',
        question: 'Как вы зарабатываете, если не берете комиссию?',
        answer: 'Мы создаем уникальные NFT на каждую успешную сделку. Это ваш цифровой сертификат надежности, который можно коллекционировать.'
    },
    {
        icon: 'shield',
        question: 'Безопасно ли это?',
        answer: 'Да. Смарт-контракт выступает гарантом сделки. Деньги замораживаются на контракте и переводятся продавцу только после подтверждения получения.'
    },
    {
        icon: 'box',
        question: 'Какие активы можно продавать?',
        answer: 'Любые: от токенов ERC-20 до NFT и даже услуг (если это разрешено в вашей юрисдикции).'
    },
    {
        icon: 'user',
        question: 'Нужна ли верификация?',
        answer: 'Для начала достаточно подтверждения почты. Для крупных сделок рекомендуется настроить 2FA.'
    },
    {
        icon: 'plus',
        question: 'Как создать объявление?',
        answer: 'Зарегистрируйся, нажми "Создать объявление" в дашборде, заполни форму и опубликуй.'
    }
]
</script>