<template>
    <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
        <!-- Сетка с точками -->
        <div class="absolute inset-0 opacity-[0.08] dark:opacity-[0.12]">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <pattern id="dotGrid" x="0" y="0" width="50" height="50" patternUnits="userSpaceOnUse">
                        <circle cx="2" cy="2" r="1.5" fill="#00DC82" opacity="0.6">
                            <animate attributeName="opacity" values="0.3;0.9;0.3" dur="4s" repeatCount="indefinite" />
                        </circle>
                        <circle cx="27" cy="27" r="1" fill="#00DC82" opacity="0.4">
                            <animate attributeName="opacity" values="0.2;0.7;0.2" dur="6s" repeatCount="indefinite"
                                begin="1s" />
                        </circle>
                        <circle cx="12" cy="42" r="0.8" fill="#00DC82" opacity="0.3">
                            <animate attributeName="opacity" values="0.1;0.5;0.1" dur="5s" repeatCount="indefinite"
                                begin="2s" />
                        </circle>
                        <circle cx="42" cy="12" r="0.8" fill="#00DC82" opacity="0.3">
                            <animate attributeName="opacity" values="0.1;0.5;0.1" dur="7s" repeatCount="indefinite"
                                begin="0.5s" />
                        </circle>
                    </pattern>
                </defs>
                <rect width="100%" height="100%" fill="url(#dotGrid)" />
            </svg>
        </div>

        <!-- Размытые пятна в видимой области -->
        <!-- Большое пятно слева вверху -->
        <div v-if="showBlob"
            class="absolute top-10 left-10 h-[400px] w-[400px] rounded-full bg-primary/10 blur-3xl animate-float-slow">
        </div>

        <!-- Пятно справа внизу -->
        <div v-if="showBlob"
            class="absolute bottom-10 right-10 h-[350px] w-[350px] rounded-full bg-emerald-500/8 blur-3xl animate-float-slower">
        </div>

        <!-- Центральное пятно для Hero -->
        <div v-if="showBlob && variant === 'hero'"
            class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 h-[300px] w-[300px] rounded-full bg-primary/8 blur-3xl animate-pulse-slow">
        </div>

        <!-- Маленькое пятно для объема -->
        <div v-if="showBlob && variant === 'hero'"
            class="absolute top-1/3 right-1/4 h-[200px] w-[200px] rounded-full bg-emerald-400/6 blur-3xl animate-float-slower"
            style="animation-delay: 2s;"></div>

        <!-- Шестиугольники для Hero -->
        <div v-if="variant === 'hero'" class="absolute inset-0">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"
                class="opacity-[0.05] dark:opacity-[0.08]">
                <defs>
                    <pattern id="hexGrid" x="0" y="0" width="80" height="80" patternUnits="userSpaceOnUse">
                        <polygon points="40,0 80,23 80,69 40,92 0,69 0,23" fill="none" stroke="#00DC82"
                            stroke-width="0.8">
                            <animate attributeName="stroke-opacity" values="0.2;0.6;0.2" dur="8s"
                                repeatCount="indefinite" />
                        </polygon>
                        <polygon points="0,46 40,23 40,69 0,46" fill="none" stroke="#00DC82" stroke-width="0.5">
                            <animate attributeName="stroke-opacity" values="0.1;0.4;0.1" dur="10s"
                                repeatCount="indefinite" begin="2s" />
                        </polygon>
                    </pattern>
                </defs>
                <rect width="100%" height="100%" fill="url(#hexGrid)" />
            </svg>
        </div>
    </div>
</template>

<script setup lang="ts">
defineProps<{
    variant?: 'hero' | 'default' | 'minimal'
    showBlob?: boolean
}>()
</script>

<style scoped>
@keyframes float-slow {
    0% {
        transform: translate(0, 0) scale(1);
    }

    25% {
        transform: translate(40px, -30px) scale(1.05);
    }

    50% {
        transform: translate(-20px, 40px) scale(0.95);
    }

    75% {
        transform: translate(30px, 10px) scale(1.03);
    }

    100% {
        transform: translate(0, 0) scale(1);
    }
}

@keyframes float-slower {
    0% {
        transform: translate(0, 0) scale(1);
    }

    33% {
        transform: translate(-30px, 25px) scale(0.97);
    }

    66% {
        transform: translate(25px, -30px) scale(1.04);
    }

    100% {
        transform: translate(0, 0) scale(1);
    }
}

@keyframes pulse-slow {

    0%,
    100% {
        opacity: 0.3;
        transform: translate(-50%, -50%) scale(1);
    }

    50% {
        opacity: 0.7;
        transform: translate(-50%, -50%) scale(1.2);
    }
}

.animate-float-slow {
    animation: float-slow 15s ease-in-out infinite;
}

.animate-float-slower {
    animation: float-slower 18s ease-in-out infinite;
}

.animate-pulse-slow {
    animation: pulse-slow 8s ease-in-out infinite;
}
</style>