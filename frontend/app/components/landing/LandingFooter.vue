<template>
    <footer class="border-t border-neutral-200/50 bg-white px-4 py-8 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-7xl">
            <div class="flex flex-col items-center justify-between gap-4 sm:flex-row">
                <!-- Левая часть -->
                <div class="flex items-center gap-3">
                    <svg width="220" height="44" viewBox="0 0 220 44" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <!-- Иконка: щит с галочкой -->
                        <g transform="translate(0, 4)">
                            <path d="M16 2L4 6V12C4 18 8 24 16 26C24 24 28 18 28 12V6L16 2Z" stroke="#00DC82"
                                stroke-width="2" stroke-linejoin="round" />
                            <path d="M11 14L14 17L21 10" stroke="#00DC82" stroke-width="2.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </g>

                        <!-- Текст: CryptoBoard -->
                        <text x="38" y="30" font-family="'Inter', 'Segoe UI', Arial, sans-serif" font-size="22"
                            font-weight="700" fill="#1A1A1A" letter-spacing="0">Crypto</text>
                        <text x="124" y="30" font-family="'Inter', 'Segoe UI', Arial, sans-serif" font-size="22"
                            font-weight="700" fill="#00DC82" letter-spacing="0">Board</text>
                    </svg> <span class="text-xs text-neutral-400">© 2026</span>
                </div>

                <!-- Правая часть: ссылки -->
                <div class="flex flex-wrap items-center justify-center gap-4 text-xs text-neutral-500">
                    <a href="/terms" class="transition hover:text-neutral-900">Terms of Service</a>
                    <span class="hidden sm:inline text-neutral-300">•</span>
                    <a href="/privacy" class="transition hover:text-neutral-900">Privacy Policy</a>
                    <span class="hidden sm:inline text-neutral-300">•</span>
                    <a href="/faq" class="transition hover:text-neutral-900">FAQ</a>
                    <span class="hidden sm:inline text-neutral-300">•</span>
                    <a href="/support" class="transition hover:text-neutral-900">Support</a>
                </div>
            </div>


        </div>
    </footer>
</template>
