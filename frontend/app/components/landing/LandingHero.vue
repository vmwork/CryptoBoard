<template>
    <section class="relative flex min-h-[calc(100vh-4rem)] items-center overflow-hidden px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-7xl">
            <div class="grid items-center gap-12 lg:grid-cols-2 lg:gap-16">
                <!-- Левая колонка -->
                <div class="space-y-8">
                    <!-- Бейдж -->
                    <div
                        class="inline-flex items-center gap-2 rounded-full border border-primary/20 bg-primary/5 px-4 py-1.5 text-sm text-primary">
                        <IconLock class="h-4 w-4" />
                        P2P платформа с крипто-гарантией
                    </div>

                    <!-- Заголовок -->
                    <h1 class="text-4xl font-bold tracking-tight text-neutral-900 sm:text-5xl lg:text-6xl">
                        Покупай и продавай<br>
                        <span class="bg-gradient-to-r from-primary to-emerald-400 bg-clip-text text-transparent">
                            что угодно
                        </span>
                        <br>с крипто-безопасностью
                    </h1>

                    <!-- Подзаголовок -->
                    <p class="max-w-lg text-lg text-neutral-600 sm:text-xl">
                        Смарт-контракты гарантируют безопасность каждой сделки.
                        <span class="text-neutral-700">Автоматический выпуск NFT — доказательство твоей
                            надежности.</span>
                    </p>

                    <!-- Кнопки -->
                    <div class="flex flex-wrap gap-4">
                        <button @click="handleIntent('buyer')"
                            class="group relative inline-flex items-center gap-2 rounded-full bg-primary px-8 py-4 text-lg font-semibold text-white transition hover:scale-105 hover:bg-primary/80 active:scale-95">
                            <IconShoppingCart class="h-5 w-5" />
                            <span>Хочу купить</span>
                            <IconArrowRight class="h-5 w-5 transition-transform group-hover:translate-x-1" />
                        </button>

                        <button @click="handleIntent('seller')"
                            class="inline-flex items-center gap-2 rounded-full border-2 border-neutral-300 px-8 py-4 text-lg font-semibold text-neutral-700 transition hover:border-primary hover:bg-primary/5 hover:text-primary">
                            <IconCoins class="h-5 w-5" />
                            <span>Хочу продать</span>
                        </button>
                    </div>

                    <!-- Доверительные метки (хештеги в чипсах) -->
                    <div class="flex flex-wrap items-center gap-3">
                        <span
                            class="inline-flex items-center gap-1.5 rounded-full bg-neutral-100 px-3 py-1.5 text-sm text-neutral-600 border border-neutral-200">
                            <IconCircleCheck class="h-4 w-4 text-primary" />
                            #БезКомиссий
                        </span>
                        <span
                            class="inline-flex items-center gap-1.5 rounded-full bg-neutral-100 px-3 py-1.5 text-sm text-neutral-600 border border-neutral-200">
                            <IconSmartHome class="h-4 w-4 text-primary" />
                            #СмартКонтракты
                        </span>
                        <span
                            class="inline-flex items-center gap-1.5 rounded-full bg-neutral-100 px-3 py-1.5 text-sm text-neutral-600 border border-neutral-200">
                            <IconCertificate class="h-4 w-4 text-primary" />
                            #NFTбонусы
                        </span>
                        <span
                            class="inline-flex items-center gap-1.5 rounded-full bg-neutral-100 px-3 py-1.5 text-sm text-neutral-600 border border-neutral-200">
                            <IconShieldCheck class="h-4 w-4 text-primary" />
                            #ЭскроуЗащита
                        </span>
                    </div>
                </div>

                <!-- Правая колонка: визуал -->
                <div class="relative flex items-center justify-center">
                    <div class="relative aspect-square w-full max-w-md">
                        <!-- Карточка сделки (темный стиль) -->
                        <div
                            class="absolute inset-0 rounded-2xl border border-neutral-800 bg-gradient-to-br from-neutral-900 to-neutral-950 p-5 shadow-2xl">
                            <div class="flex h-full flex-col justify-between">
                                <!-- Верх: статус и цена -->
                                <div class="space-y-3">
                                    <div class="flex items-center justify-between">
                                        <div class="flex items-center gap-2">
                                            <span class="text-sm font-medium text-neutral-400">Заказ #421</span>
                                            <span
                                                class="rounded-full bg-emerald-500/10 px-2.5 py-0.5 text-xs text-emerald-400 border border-emerald-500/20">
                                                <span class="flex items-center gap-1">
                                                    <span
                                                        class="inline-block h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                                                    В процессе
                                                </span>
                                            </span>
                                        </div>
                                        <button class="text-neutral-600 hover:text-neutral-400 transition">
                                            <IconDots class="h-5 w-5" />
                                        </button>
                                    </div>

                                    <!-- Цена -->
                                    <div>
                                        <p class="text-2xl font-bold text-white">1,250 <span
                                                class="text-sm font-medium text-neutral-400">USDT</span></p>
                                        <p class="text-sm text-neutral-500">≈ 32,450 грн</p>
                                    </div>
                                </div>

                                <!-- Середина: товар и NFT -->
                                <div class="space-y-3">
                                    <!-- Мини-карточка товара -->
                                    <div
                                        class="flex items-center gap-3 rounded-lg bg-neutral-800/50 p-3 border border-neutral-700/50">
                                        <div
                                            class="flex h-12 w-12 shrink-0 items-center justify-center rounded-lg bg-neutral-800">
                                            <IconDeviceLaptop class="h-6 w-6 text-neutral-400" />
                                        </div>
                                        <div class="min-w-0 flex-1">
                                            <p class="text-sm font-medium text-white truncate">MacBook Pro 14" M3</p>
                                            <p class="text-xs text-neutral-400">Продавец: <span
                                                    class="text-neutral-300">@alex_crypto</span></p>
                                        </div>
                                        <div
                                            class="rounded-full bg-primary/10 px-2 py-0.5 text-xs text-primary border border-primary/20 animate-pulse">
                                            NFT готов
                                        </div>
                                    </div>

                                    <!-- Процесс выпуска NFT с анимацией -->
                                    <div class="rounded-lg bg-neutral-800/30 p-3 border border-neutral-700/30">
                                        <div class="flex items-center justify-between">
                                            <div class="flex items-center gap-2">
                                                <IconNft class="h-4 w-4 text-primary animate-spin-slow" />
                                                <span class="text-xs text-neutral-400">Выпуск NFT-сертификата</span>
                                            </div>
                                            <span class="text-xs text-emerald-400 font-mono">
                                                {{ progress }}%
                                            </span>
                                        </div>
                                        <div class="mt-1.5 h-1 w-full rounded-full bg-neutral-800 overflow-hidden">
                                            <div class="h-1 rounded-full bg-gradient-to-r from-primary to-emerald-400 transition-all duration-1000 ease-out"
                                                :style="{ width: progress + '%' }"></div>
                                        </div>
                                        <p class="mt-1 text-[10px] text-neutral-500 flex items-center gap-1">
                                            <IconClock class="inline h-3 w-3 animate-pulse" />
                                            ~ {{ estimatedTime }} мин до завершения
                                        </p>
                                    </div>
                                </div>

                                <!-- Низ: статус доставки -->
                                <div class="space-y-2">
                                    <div class="flex items-center justify-between text-xs">
                                        <span class="text-neutral-500">Статус сделки</span>
                                        <span class="text-emerald-400 flex items-center gap-1">
                                            <span
                                                class="inline-block h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                                            Эскроу активирован
                                        </span>
                                    </div>

                                    <!-- Прогресс доставки с анимацией -->
                                    <div class="relative flex items-center justify-between">
                                        <div
                                            class="absolute left-0 right-0 top-1/2 h-0.5 -translate-y-1/2 bg-neutral-800">
                                            <div class="h-0.5 bg-gradient-to-r from-primary to-emerald-400 transition-all duration-1000 ease-out"
                                                :style="{ width: deliveryProgress + '%' }"></div>
                                        </div>

                                        <div class="relative flex flex-col items-center">
                                            <div
                                                class="z-10 flex h-6 w-6 items-center justify-center rounded-full bg-primary text-white transition-all duration-500">
                                                <IconCheck class="h-3.5 w-3.5" />
                                            </div>
                                            <span class="mt-1 text-[10px] text-emerald-400 font-medium">Оплачено</span>
                                        </div>

                                        <div class="relative flex flex-col items-center">
                                            <div class="z-10 flex h-6 w-6 items-center justify-center rounded-full transition-all duration-500"
                                                :class="deliveryProgress >= 33 ? 'bg-primary/20 border border-primary text-primary' : 'bg-neutral-800 border border-neutral-700 text-neutral-500'">
                                                <IconPackage class="h-3.5 w-3.5"
                                                    :class="deliveryProgress >= 33 ? 'text-primary' : 'text-neutral-500'" />
                                            </div>
                                            <span class="mt-1 text-[10px] font-medium"
                                                :class="deliveryProgress >= 33 ? 'text-emerald-400' : 'text-neutral-500'">В
                                                пути</span>
                                        </div>

                                        <div class="relative flex flex-col items-center">
                                            <div class="z-10 flex h-6 w-6 items-center justify-center rounded-full transition-all duration-500"
                                                :class="deliveryProgress >= 66 ? 'bg-primary/20 border border-primary text-primary' : 'bg-neutral-800 border border-neutral-700 text-neutral-500'">
                                                <IconCircleCheck class="h-3.5 w-3.5"
                                                    :class="deliveryProgress >= 66 ? 'text-primary' : 'text-neutral-500'" />
                                            </div>
                                            <span class="mt-1 text-[10px] font-medium"
                                                :class="deliveryProgress >= 66 ? 'text-emerald-400' : 'text-neutral-500'">Получено</span>
                                        </div>

                                        <div class="relative flex flex-col items-center">
                                            <div class="z-10 flex h-6 w-6 items-center justify-center rounded-full transition-all duration-500"
                                                :class="deliveryProgress >= 90 ? 'bg-primary/20 border border-primary text-primary' : 'bg-neutral-800 border border-neutral-700 text-neutral-500'">
                                                <IconNft class="h-3.5 w-3.5"
                                                    :class="deliveryProgress >= 90 ? 'text-primary' : 'text-neutral-500'" />
                                            </div>
                                            <span class="mt-1 text-[10px] font-medium"
                                                :class="deliveryProgress >= 90 ? 'text-emerald-400' : 'text-neutral-500'">NFT</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Декоративные элементы -->
                        <div
                            class="absolute -right-4 -top-4 h-32 w-32 rounded-full bg-primary/5 blur-2xl animate-pulse-slow">
                        </div>
                        <div
                            class="absolute -bottom-4 -left-4 h-32 w-32 rounded-full bg-emerald-500/5 blur-2xl animate-pulse-slower">
                        </div>

                        <!-- Вращающаяся орбита -->
                        <div class="absolute inset-0 pointer-events-none">
                            <div
                                class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[130%] h-[130%] border border-primary/10 rounded-full animate-spin-slow">
                            </div>
                            <div
                                class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[160%] h-[160%] border border-primary/5 rounded-full animate-spin-slower">
                            </div>
                            <div
                                class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[190%] h-[190%] border border-emerald-500/5 rounded-full animate-spin-medium">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
// Используем правильные имена иконок из @tabler/icons-vue
import {
    IconLock,
    IconShoppingCart,
    IconArrowRight,
    IconCoins,
    IconCircleCheck,
    IconSmartHome,
    IconCertificate,
    IconShieldCheck,
    IconDots,
    IconDeviceLaptop,
    IconClock,
    IconPackage,
    IconCheck
} from '@tabler/icons-vue'

const router = useRouter()

// Анимированный прогресс
const progress = ref(0)
const deliveryProgress = ref(0)
const estimatedTime = ref(2)

// Запускаем анимации при монтировании
onMounted(() => {
    // Анимация прогресса NFT
    const progressInterval = setInterval(() => {
        if (progress.value < 75) {
            progress.value += Math.random() * 3 + 1
            if (progress.value > 75) progress.value = 75
        } else {
            clearInterval(progressInterval)
        }
    }, 300)

    // Анимация доставки
    const deliveryInterval = setInterval(() => {
        if (deliveryProgress.value < 100) {
            deliveryProgress.value += Math.random() * 2 + 0.5
            if (deliveryProgress.value > 100) deliveryProgress.value = 100
        } else {
            clearInterval(deliveryInterval)
        }
    }, 500)

    // Таймер обратного отсчета
    const timerInterval = setInterval(() => {
        if (estimatedTime.value > 0) {
            estimatedTime.value = Number((estimatedTime.value - 0.1).toFixed(1))
        } else {
            clearInterval(timerInterval)
        }
    }, 6000)
})

const handleIntent = (role: 'buyer' | 'seller') => {
    localStorage.setItem('userIntent', role)
    router.push('/auth')
}
</script>

<style scoped>
@keyframes spin-slow {
    from {
        transform: translate(-50%, -50%) rotate(0deg);
    }

    to {
        transform: translate(-50%, -50%) rotate(360deg);
    }
}

@keyframes spin-slower {
    from {
        transform: translate(-50%, -50%) rotate(0deg);
    }

    to {
        transform: translate(-50%, -50%) rotate(-360deg);
    }
}

@keyframes spin-medium {
    from {
        transform: translate(-50%, -50%) rotate(0deg);
    }

    to {
        transform: translate(-50%, -50%) rotate(180deg);
    }
}

@keyframes pulse-slow {

    0%,
    100% {
        opacity: 0.3;
        transform: scale(1);
    }

    50% {
        opacity: 0.6;
        transform: scale(1.1);
    }
}

@keyframes pulse-slower {

    0%,
    100% {
        opacity: 0.2;
        transform: scale(1);
    }

    50% {
        opacity: 0.5;
        transform: scale(1.2);
    }
}

.animate-spin-slow {
    animation: spin-slow 20s linear infinite;
}

.animate-spin-slower {
    animation: spin-slower 30s linear infinite;
}

.animate-spin-medium {
    animation: spin-medium 25s linear infinite;
}

.animate-pulse-slow {
    animation: pulse-slow 4s ease-in-out infinite;
}

.animate-pulse-slower {
    animation: pulse-slower 5s ease-in-out infinite;
}
</style>