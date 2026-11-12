<template>
    <div class="min-h-screen bg-background text-foreground">
        <LandingFAQ />
    </div>
</template>

<script setup lang="ts">
definePageMeta({
    layout: 'landing'
})

import LandingFAQ from '~/components/landing/LandingFAQ.vue'
</script>