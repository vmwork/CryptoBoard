<template>
    <div class="absolute inset-0 pointer-events-none overflow-hidden">
        <div v-for="(particle, i) in particles" :key="i" class="absolute rounded-full" :style="{
            left: particle.x + '%',
            top: particle.y + '%',
            width: particle.size + 'px',
            height: particle.size + 'px',
            backgroundColor: particle.color,
            opacity: particle.opacity,
            animation: `float-particle-${i % 3} ${particle.duration}s ease-in-out infinite`,
            animationDelay: particle.delay + 's'
        }" />
    </div>
</template>

<script setup lang="ts">
const particles = Array.from({ length: 20 }, (_, i) => ({
    x: Math.random() * 100,
    y: Math.random() * 100,
    size: Math.random() * 4 + 2,
    color: ['#00DC82', '#34D399', '#6EE7B7', '#A7F3D0', '#D1FAE5'][Math.floor(Math.random() * 5)],
    opacity: Math.random() * 0.3 + 0.1,
    duration: Math.random() * 20 + 15,
    delay: Math.random() * 10
}))
</script>

<style scoped>
@keyframes float-particle-0 {

    0%,
    100% {
        transform: translate(0, 0);
    }

    25% {
        transform: translate(30px, -20px);
    }

    50% {
        transform: translate(-20px, 30px);
    }

    75% {
        transform: translate(10px, -10px);
    }
}

@keyframes float-particle-1 {

    0%,
    100% {
        transform: translate(0, 0);
    }

    33% {
        transform: translate(-25px, 15px);
    }

    66% {
        transform: translate(20px, -25px);
    }
}

@keyframes float-particle-2 {

    0%,
    100% {
        transform: translate(0, 0);
    }

    50% {
        transform: translate(15px, -30px);
    }
}
</style>