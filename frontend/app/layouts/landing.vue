<template>
    <div class="relative isolate min-h-screen bg-white">
        <!-- Легкий градиентный фон вместо звезд -->
        <div class="absolute inset-0 z-0 overflow-hidden">
            <div class="absolute -top-40 -right-40 h-96 w-96 rounded-full bg-primary/5 blur-3xl"></div>
            <div class="absolute -bottom-40 -left-40 h-96 w-96 rounded-full bg-blue-500/5 blur-3xl"></div>
        </div>

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