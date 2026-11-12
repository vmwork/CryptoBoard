<template>
  <div class="min-h-screen bg-background text-foreground">
    <Header :category-links="categoryLinks" />
    <main class="min-h-full">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import Header from '@/components/Header.vue'
import { categoryLinks } from '@/data/sections'
</script>
