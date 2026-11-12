<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { useHead } from '#imports'
import { useTheme } from '~/composables/useTheme'

const { theme } = useTheme()

useHead(() => ({
  htmlAttrs: {
    class: theme.value === 'dark' ? 'dark' : ''
  },
  bodyAttrs: {
    class: theme.value === 'dark' ? 'dark' : ''
  }
}))
</script>
