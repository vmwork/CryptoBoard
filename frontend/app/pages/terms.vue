<template>
    <div class="min-h-screen bg-neutral-50">
        <div class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
            <!-- Навигация назад -->
            <div class="mb-8">
                <NuxtLink to="/"
                    class="inline-flex items-center gap-2 text-sm text-neutral-600 transition hover:text-neutral-900">
                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    На главную
                </NuxtLink>
            </div>

            <!-- Контент -->
            <div class="overflow-hidden rounded-2xl bg-white shadow-sm">
                <div class="border-b border-neutral-100 px-6 py-8 sm:px-10 sm:py-10">
                    <h1 class="text-3xl font-bold text-neutral-900 sm:text-4xl">
                        Пользовательское соглашение
                    </h1>
                    <p class="mt-2 text-sm text-neutral-500">
                        Последнее обновление: 12 августа 2026
                    </p>
                </div>

                <div class="space-y-8 px-6 py-8 sm:px-10 sm:py-10">
                    <!-- Раздел 1 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">1. Общие положения</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Настоящее Пользовательское соглашение (далее — «Соглашение») регулирует отношения между
                                <span class="font-medium">CryptoBoard</span> (далее — «Платформа») и пользователем
                                (далее — «Пользователь»)
                                при использовании сервисов Платформы.
                            </p>
                            <p>
                                Используя Платформу, Пользователь соглашается с условиями настоящего Соглашения.
                                Если Пользователь не согласен с условиями, он должен немедленно прекратить использование
                                Платформы.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 2 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">2. Статус Платформы</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p class="font-medium text-neutral-900">
                                CryptoBoard является информационной площадкой (доской объявлений) и НЕ является:
                            </p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>Посредником, агентом или брокером</li>
                                <li>Финансовым институтом или банком</li>
                                <li>Организатором торгов или биржей</li>
                            </ul>
                            <p class="mt-3">
                                Платформа предоставляет возможность размещения объявлений о продаже/покупке цифровых
                                активов,
                                но не участвует в сделках между пользователями.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 3 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">3. Смарт-контракты</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Платформа предоставляет инфраструктуру для использования смарт-контрактов, но:
                            </p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>
                                    <span class="font-medium">Смарт-контракты являются самоисполняемыми</span>
                                    и действуют независимо от Платформы
                                </li>
                                <li>
                                    Платформа не контролирует и не управляет смарт-контрактами
                                </li>
                                <li>
                                    Пользователи самостоятельно несут риски, связанные с использованием блокчейна
                                </li>
                                <li>
                                    Платформа не отвечает за ошибки в коде смарт-контрактов
                                </li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 4 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">4. Ответственность Пользователя</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>Пользователь несет полную ответственность за:</p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>Достоверность размещаемой информации</li>
                                <li>Соблюдение законодательства своей юрисдикции</li>
                                <li>Безопасность своего аккаунта и крипто-кошелька</li>
                                <li>Все операции, совершаемые с использованием аккаунта</li>
                                <li>Уплату налогов, связанных со сделками</li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 5 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">5. Ограничение ответственности</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p class="font-medium text-neutral-900">
                                Платформа предоставляется «как есть» (AS IS) и НЕ несет ответственности за:
                            </p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>Убытки, связанные с использованием Платформы</li>
                                <li>Действия или бездействие других пользователей</li>
                                <li>Технические сбои блокчейна или интернета</li>
                                <li>Взлом аккаунтов или кражу средств</li>
                                <li>Потерю данных или доступа к аккаунту</li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 6 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">6. Интеллектуальная собственность</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Все материалы, размещенные на Платформе, включая текст, графику, логотипы, иконки,
                                являются собственностью CryptoBoard и защищены авторским правом.
                            </p>
                            <p>
                                Пользователь не имеет права копировать, модифицировать или распространять материалы
                                Платформы без письменного согласия владельца.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 7 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">7. NFT и монетизация</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Платформа может генерировать и продавать NFT как дополнительный сервис:
                            </p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>NFT создаются автоматически при успешном завершении сделки</li>
                                <li>NFT являются цифровым активом и подтверждением совершенной сделки</li>
                                <li>Платформа не гарантирует ликвидность или стоимость NFT</li>
                                <li>Пользователь может отказаться от получения NFT</li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 8 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">8. Изменение Соглашения</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Платформа оставляет за собой право изменять настоящее Соглашение в любое время.
                                Изменения вступают в силу с момента публикации на сайте.
                            </p>
                            <p>
                                Пользователь обязуется регулярно проверять актуальную версию Соглашения.
                                Продолжение использования Платформы после изменений означает согласие с новой версией.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 9 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">9. Применимое право</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Настоящее Соглашение регулируется и толкуется в соответствии с законодательством
                                страны регистрации Платформы.
                            </p>
                            <p>
                                Все споры, возникающие из или в связи с Соглашением, подлежат разрешению в суде
                                по месту регистрации Платформы.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 10 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">10. Контакты</h2>
                        <div class="mt-3 rounded-xl bg-neutral-50 p-4 text-neutral-700">
                            <p>По всем вопросам, связанным с Соглашением, обращайтесь:</p>
                            <div class="mt-2 space-y-1">
                                <p>
                                    <span class="font-medium">Email:</span>
                                    <a href="mailto:support@cryptoboard.com" class="text-primary hover:underline">
                                        support@cryptoboard.com
                                    </a>
                                </p>
                                <p>
                                    <span class="font-medium">Telegram:</span>
                                    <a href="#" class="text-primary hover:underline">@cryptoboard_support</a>
                                </p>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
definePageMeta({
    layout: 'landing'
})
</script>