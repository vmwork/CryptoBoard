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
                        Политика конфиденциальности
                    </h1>
                    <p class="mt-2 text-sm text-neutral-500">
                        Последнее обновление: 12 августа 2026
                    </p>
                </div>

                <div class="space-y-8 px-6 py-8 sm:px-10 sm:py-10">
                    <!-- Раздел 1 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">1. Введение</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Мы в CryptoBoard уважаем вашу конфиденциальность и обязуемся защищать ваши персональные
                                данные.
                                Настоящая Политика конфиденциальности объясняет, как мы собираем, используем и защищаем
                                вашу информацию.
                            </p>
                            <p>
                                Используя Платформу, вы соглашаетесь с условиями данной Политики.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 2 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">2. Какие данные мы собираем</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>Для предоставления услуг Платформа собирает следующие данные:</p>

                            <div class="mt-4 space-y-4">
                                <div class="rounded-xl border border-neutral-100 bg-neutral-50 p-4">
                                    <h3 class="font-medium text-neutral-900">Личная информация</h3>
                                    <ul class="mt-2 list-disc space-y-1 pl-5 text-neutral-600">
                                        <li>Email адрес</li>
                                        <li>Имя пользователя</li>
                                        <li>Адрес крипто-кошелька</li>
                                        <li>Данные профиля (аватар, описание)</li>
                                    </ul>
                                </div>

                                <div class="rounded-xl border border-neutral-100 bg-neutral-50 p-4">
                                    <h3 class="font-medium text-neutral-900">Технические данные</h3>
                                    <ul class="mt-2 list-disc space-y-1 pl-5 text-neutral-600">
                                        <li>IP-адрес</li>
                                        <li>Тип браузера и версия</li>
                                        <li>Тип устройства и операционная система</li>
                                        <li>Время и дата посещения</li>
                                        <li>Страницы, которые вы посещаете</li>
                                    </ul>
                                </div>

                                <div class="rounded-xl border border-neutral-100 bg-neutral-50 p-4">
                                    <h3 class="font-medium text-neutral-900">Данные о сделках</h3>
                                    <ul class="mt-2 list-disc space-y-1 pl-5 text-neutral-600">
                                        <li>Созданные объявления</li>
                                        <li>Совершенные транзакции</li>
                                        <li>История сделок</li>
                                        <li>Полученные NFT</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Раздел 3 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">3. Как мы используем ваши данные</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <ul class="list-disc space-y-2 pl-6">
                                <li>
                                    <span class="font-medium">Регистрация и управление аккаунтом</span>
                                    <br>
                                    <span class="text-neutral-600 text-sm">Для создания и ведения вашего профиля на
                                        Платформе</span>
                                </li>
                                <li>
                                    <span class="font-medium">Обеспечение безопасности</span>
                                    <br>
                                    <span class="text-neutral-600 text-sm">Для предотвращения мошенничества и
                                        несанкционированного доступа</span>
                                </li>
                                <li>
                                    <span class="font-medium">Улучшение Платформы</span>
                                    <br>
                                    <span class="text-neutral-600 text-sm">Для анализа поведения пользователей и
                                        оптимизации сервиса</span>
                                </li>
                                <li>
                                    <span class="font-medium">Коммуникация</span>
                                    <br>
                                    <span class="text-neutral-600 text-sm">Для отправки уведомлений, обновлений и
                                        ответов на запросы поддержки</span>
                                </li>
                                <li>
                                    <span class="font-medium">Юридические обязательства</span>
                                    <br>
                                    <span class="text-neutral-600 text-sm">Для соблюдения требований
                                        законодательства</span>
                                </li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 4 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">4. Передача данных третьим лицам</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p class="font-medium text-neutral-900">
                                Мы НЕ продаем и НЕ передаем ваши персональные данные третьим лицам, за исключением:
                            </p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>
                                    <span class="font-medium">Блокчейн:</span>
                                    Данные о сделках записываются в публичный блокчейн и являются необратимыми
                                </li>
                                <li>
                                    <span class="font-medium">Аналитика:</span>
                                    Мы используем сервисы аналитики для улучшения Платформы
                                </li>
                                <li>
                                    <span class="font-medium">Законодательство:</span>
                                    Мы можем передавать данные по требованию правоохранительных органов
                                </li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 5 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">5. Безопасность данных</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>Мы принимаем все необходимые меры для защиты ваших данных:</p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>
                                    <span class="font-medium">Шифрование:</span>
                                    Все данные передаются через защищенное соединение (SSL/TLS)
                                </li>
                                <li>
                                    <span class="font-medium">Хеширование паролей:</span>
                                    Пароли хранятся в зашифрованном виде
                                </li>
                                <li>
                                    <span class="font-medium">Регулярные проверки:</span>
                                    Мы проводим аудиты безопасности
                                </li>
                                <li>
                                    <span class="font-medium">2FA:</span>
                                    Рекомендуем включить двухфакторную аутентификацию
                                </li>
                            </ul>
                        </div>
                    </section>

                    <!-- Раздел 6 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">6. Права пользователя</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>В соответствии с GDPR и другими законами, вы имеете право:</p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>Запросить копию ваших данных</li>
                                <li>Исправить неточные или неполные данные</li>
                                <li>Удалить ваш аккаунт и все связанные данные</li>
                                <li>Отозвать согласие на обработку данных</li>
                                <li>Экспортировать ваши данные в машиночитаемом формате</li>
                            </ul>
                            <p class="mt-3">
                                Для реализации этих прав свяжитесь с нами через контакты, указанные ниже.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 7 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">7. Cookie</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Платформа использует файлы cookie для улучшения пользовательского опыта:
                            </p>
                            <ul class="list-disc space-y-2 pl-6">
                                <li>
                                    <span class="font-medium">Необходимые:</span>
                                    Для базовой функциональности Платформы
                                </li>
                                <li>
                                    <span class="font-medium">Аналитические:</span>
                                    Для сбора статистики использования
                                </li>
                                <li>
                                    <span class="font-medium">Предпочтения:</span>
                                    Для запоминания настроек пользователя
                                </li>
                            </ul>
                            <p class="mt-3">
                                Вы можете отключить cookie в настройках браузера, но это может повлиять
                                на функциональность Платформы.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 8 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">8. Хранение данных</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Мы храним ваши данные до тех пор, пока ваш аккаунт активен.
                                После удаления аккаунта данные удаляются в течение 30 дней,
                                за исключением данных, записанных в блокчейн (они необратимы).
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 9 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">9. Изменения в Политике</h2>
                        <div class="mt-3 space-y-3 text-neutral-700 leading-relaxed">
                            <p>
                                Мы можем обновлять данную Политику конфиденциальности.
                                О существенных изменениях мы уведомим вас через email или через Платформу.
                            </p>
                            <p>
                                Рекомендуем регулярно проверять актуальную версию Политики.
                            </p>
                        </div>
                    </section>

                    <!-- Раздел 10 -->
                    <section>
                        <h2 class="text-xl font-semibold text-neutral-900">10. Контакты</h2>
                        <div class="mt-3 rounded-xl bg-neutral-50 p-4 text-neutral-700">
                            <p>По вопросам конфиденциальности обращайтесь:</p>
                            <div class="mt-2 space-y-1">
                                <p>
                                    <span class="font-medium">Email:</span>
                                    <a href="mailto:privacy@cryptoboard.com" class="text-primary hover:underline">
                                        privacy@cryptoboard.com
                                    </a>
                                </p>
                                <p>
                                    <span class="font-medium">Telegram:</span>
                                    <a href="#" class="text-primary hover:underline">@cryptoboard_privacy</a>
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