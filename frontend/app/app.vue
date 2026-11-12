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
    class: theme.value
  },
  bodyAttrs: {
    class: theme.value
  }
}))
</script>
