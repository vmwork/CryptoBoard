<template>
    <header class="sticky top-0 z-50 border-b border-neutral-200/50 bg-white/80 backdrop-blur-xl dark:border-white/80 dark:bg-white/95">
        <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
            <!-- Логотип -->
            <a href="/" class="flex items-center gap-2">
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
                </svg>
            </a>

            <!-- Навигация -->
            <nav class="hidden items-center gap-6 md:flex">
                <a href="/faq" class="text-sm text-neutral-600 transition hover:text-neutral-900 dark:text-neutral-900">FAQ</a>
                <a href="/terms" class="text-sm text-neutral-600 transition hover:text-neutral-900 dark:text-neutral-900">Terms</a>
                <a href="/privacy" class="text-sm text-neutral-600 transition hover:text-neutral-900 dark:text-neutral-900">Privacy</a>
            </nav>

            <!-- Кнопки -->
            <div class="flex items-center gap-3">
                <button
                    type="button"
                    class="rounded-full border border-neutral-200/60 bg-white/80 p-2 text-neutral-600 shadow-sm transition hover:border-neutral-300 hover:bg-neutral-100 hover:text-neutral-900 dark:border-white/20 dark:bg-neutral-900/60 dark:text-neutral-200 dark:hover:bg-neutral-800 dark:hover:text-white"
                    :aria-label="toggleLabel"
                    @click="toggleTheme"
                >
                    <span class="sr-only">{{ toggleLabel }}</span>
                    <svg v-if="isDark" width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M21 12.79A9 9 0 0 1 11.21 3 7 7 0 1 0 21 12.79Z"
                            stroke="currentColor"
                            stroke-width="1.5"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                    </svg>
                    <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="5" fill="currentColor" />
                        <path
                            d="M12 3V1M12 23V21M4.22 4.22L2.81 2.81M21.19 21.19L19.78 19.78M3 12H1M23 12H21M4.22 19.78L2.81 21.19M21.19 2.81L19.78 4.22"
                            stroke="currentColor"
                            stroke-width="1.5"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                        />
                    </svg>
                </button>
                <NuxtLink to="/auth"
                    class="rounded-full px-4 py-2 text-sm font-medium text-neutral-700 transition hover:bg-neutral-100 hover:text-neutral-900">
                    Войти
                </NuxtLink>
                <NuxtLink to="/auth"
                    class="rounded-full bg-primary px-4 py-2 text-sm font-medium text-white transition hover:bg-primary/80">
                    Зарегистрироваться
                </NuxtLink>
            </div>
        </div>
    </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useTheme } from '~/composables/useTheme'

const { isDark, toggleTheme } = useTheme()
const toggleLabel = computed(() =>
    isDark.value ? 'Переключить на светлую тему' : 'Переключить на тёмную тему'
)
</script>
