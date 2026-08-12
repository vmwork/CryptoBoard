<template>
    <section class="border-t border-neutral-200/50 px-4 py-24 sm:px-6 sm:py-32 lg:px-8" id="faq">
        <div class="mx-auto max-w-4xl">
            <!-- Заголовок -->
            <div class="text-center">
                <h2 class="text-3xl font-bold text-neutral-900 sm:text-4xl lg:text-5xl">
                    Часто задаваемые <span class="text-primary">вопросы</span>
                </h2>
                <p class="mt-4 text-neutral-600">
                    Найди ответ на свой вопрос. Если не нашел — пиши в поддержку
                </p>
            </div>

            <!-- Аккордеон -->
            <div class="mt-12 space-y-4">
                <div v-for="(item, index) in faqItems" :key="index"
                    class="rounded-2xl border border-neutral-200 bg-white transition-shadow hover:shadow-sm">
                    <button @click="toggleItem(index)"
                        class="flex w-full items-center justify-between px-6 py-5 text-left transition hover:text-primary">
                        <span class="text-base font-medium text-neutral-900 sm:text-lg">{{ item.question }}</span>
                        <svg class="h-5 w-5 text-neutral-400 transition-transform duration-300"
                            :class="{ 'rotate-180 text-primary': openIndex === index }" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>

                    <div class="overflow-hidden transition-all duration-300 ease-in-out"
                        :class="openIndex === index ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'">
                        <div class="border-t border-neutral-100 px-6 pb-5 pt-4 text-neutral-600">
                            {{ item.answer }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
definePageMeta({
    layout: 'landing'
})
const openIndex = ref<number | null>(null)

const toggleItem = (index: number) => {
    // Если кликнули по тому же элементу - закрываем, иначе открываем новый
    openIndex.value = openIndex.value === index ? null : index
}

const faqItems = [
    {
        question: 'Что такое CryptoBoard?',
        answer: 'Это децентрализованная доска объявлений для торговли цифровыми активами. Мы объединяем покупателей и продавцов напрямую, используя смарт-контракты для безопасных сделок.'
    },
    {
        question: 'Как вы зарабатываете, если не берете комиссию?',
        answer: 'Мы создаем уникальные NFT на каждую успешную сделку. Это ваш цифровой сертификат надежности, который можно коллекционировать. Торгуй активно — получай редкие NFT.'
    },
    {
        question: 'Безопасно ли это?',
        answer: 'Да. Смарт-контракт выступает гарантом сделки. Деньги замораживаются на контракте и переводятся продавцу только после подтверждения получения товара. Все операции прозрачны и проверяемы в блокчейне.'
    },
    {
        question: 'Какие активы можно продавать?',
        answer: 'Любые: от токенов ERC-20 до NFT и даже услуг (если это разрешено в вашей юрисдикции). Главное — соблюдать правила платформы и законы вашей страны.'
    },
    {
        question: 'Нужна ли верификация?',
        answer: 'Для начала достаточно подтверждения почты. Для крупных сделок и дополнительной безопасности рекомендуется настроить 2FA (двухфакторную аутентификацию).'
    },
    {
        question: 'Как создать объявление?',
        answer: 'Зарегистрируйся, пополни баланс (для активации аккаунта), нажми "Создать объявление" в дашборде, заполни форму и опубликуй. Первое объявление появится после модерации.'
    }
]
</script>