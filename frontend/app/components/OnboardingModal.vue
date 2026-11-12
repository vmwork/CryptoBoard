<template>
    <Teleport to="body">
        <transition name="fade" appear>
            <div
                v-if="isVisible"
                class="fixed inset-0 z-[60] flex items-center justify-center px-4"
                role="dialog"
                aria-modal="true"
                aria-label="Онбординг Classifyd"
            >
                <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" aria-hidden="true"></div>
                <div
                    class="relative z-10 w-full max-w-3xl rounded-3xl border border-white/10 bg-neutral-950/95 p-6 shadow-2xl"
                >
                    <div class="flex items-center justify-between gap-4">
                        <div>
                            <p class="text-xs uppercase tracking-[0.4em] text-neutral-500">Escrow Deal</p>
                            <h3 class="text-2xl font-semibold text-white">Заказ #421</h3>
                        </div>
                        <button
                            type="button"
                            class="text-neutral-400 transition hover:text-white"
                            @click="complete()"
                        >
                            <span class="sr-only">Закрыть подсказку</span>
                            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M4 4L16 16M16 4L4 16"
                                    stroke="currentColor"
                                    stroke-width="1.5"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                />
                            </svg>
                        </button>
                    </div>

                    <p class="mt-3 text-sm text-neutral-300">
                        Classifyd удерживает USDT в контракте-эскроу до подтверждения получения товара, а после
                        автоматически выпускает NFT Deal Certificate — цифровой паспорт сделки.
                    </p>

                    <div class="mt-6 space-y-5">
                        <div class="rounded-2xl border border-white/10 bg-white/5 p-5">
                            <div class="flex items-center justify-between text-[0.65rem] uppercase tracking-[0.3em] text-neutral-400">
                                <span>Статус escrow</span>
                                <span class="text-xs font-semibold text-primary-400">Escrow удерживает средства</span>
                            </div>
                            <div class="mt-3 h-2 rounded-full bg-white/10">
                                <div class="h-full rounded-full bg-gradient-to-r from-primary to-emerald-400" style="width: 75%"></div>
                            </div>
                            <p class="mt-2 text-[0.7rem] text-neutral-400">
                                Средства заблокированы до подтверждения доставки; если товар не пришёл — возврат
                                автоматически инициируется.
                            </p>
                        </div>

                        <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
                            <div
                                v-for="step in steps"
                                :key="step.label"
                                class="flex flex-col items-center gap-2"
                            >
                                <div
                                    :class="[
                                        'flex h-12 w-12 items-center justify-center rounded-2xl border text-[0.65rem] font-semibold uppercase tracking-wide',
                                        step.status === 'done'
                                            ? 'border-primary-300 bg-primary-300/10 text-primary-200'
                                            : step.status === 'current'
                                                ? 'border-white/40 bg-white/10 text-white'
                                                : 'border-white/10 text-neutral-500'
                                    ]"
                                >
                                    {{ step.label }}
                                </div>
                                <p class="text-[0.65rem] text-center text-neutral-400">
                                    {{ step.meta }}
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="mt-6 flex flex-col gap-3 rounded-2xl border border-white/10 bg-white/5 p-4 text-[0.75rem] text-neutral-300 sm:flex-row sm:items-center sm:justify-between">
                        <p>
                            Ваша сделка контролируется смарт-контрактом: продавец получает средства только после
                            подтверждения, а покупатель — NFT Deal Certificate как доказательство происхождения.
                        </p>
                        <button
                            type="button"
                            class="w-full rounded-2xl border border-white/20 bg-gradient-to-r from-primary to-emerald-400 px-5 py-2 text-sm font-semibold uppercase tracking-wide text-neutral-900 transition hover:from-primary/90 hover:to-emerald-300 sm:w-auto"
                            @click="complete()"
                        >
                            Понятно / Начать
                        </button>
                    </div>
                </div>
            </div>
        </transition>
    </Teleport>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

const storageKey = 'classifyd_onboarded'
const isVisible = ref(false)

const steps = [
    { label: 'Оплачено', meta: 'Средства зафиксированы', status: 'done' },
    { label: 'В пути', meta: 'Отправка подтверждена', status: 'done' },
    { label: 'Получено', meta: 'Подтверждение клиента', status: 'current' },
    { label: 'NFT', meta: 'Паспорт сделки', status: 'upcoming' }
]

const complete = () => {
    if (process.client) {
        window.localStorage.setItem(storageKey, 'true')
    }

    isVisible.value = false
}

onMounted(() => {
    const seen = process.client ? window.localStorage.getItem(storageKey) : null
    if (!seen) {
        isVisible.value = true
    }
})
</script>
