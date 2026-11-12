<template>
    <div class="relative isolate min-h-screen bg-white dark:bg-neutral-950">
        <OnboardingModal />
        <!-- Фон -->
        <LandingBackground variant="default" :show-blob="true" />

        <!-- Контент -->
        <div class="relative z-10 flex min-h-screen flex-col">
            <LandingHeader />
            <main class="flex-1">
                <slot />
            </main>
            <LandingFooter />
        </div>
    </div>
</template>
<script setup lang="ts">
import OnboardingModal from '~/components/OnboardingModal.vue'

// ✅ Используем ref для звезд, чтобы инициализировать на клиенте
const stars = ref<Array<{ x: number; y: number; size: number; opacity: number }>>([])

// ✅ Генерируем звезды только на клиенте
onMounted(() => {
    stars.value = Array.from({ length: 50 }, () => ({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        size: Math.random() * 2 + 0.5,
        opacity: Math.random() * 0.5 + 0.3
    }))
})
</script>

<style scoped>
.stars {
    position: absolute;
    inset: 0;
}

.star {
    animation: twinkle 3s ease-in-out infinite;
}

@keyframes twinkle {

    0%,
    100% {
        opacity: 0.3;
    }

    50% {
        opacity: 1;
    }
}
</style>