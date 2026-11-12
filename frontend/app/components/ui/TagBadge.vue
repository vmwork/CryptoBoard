<script setup lang="ts">
import { computed } from 'vue'
import { useTheme } from '~/composables/useTheme'

type Props = {
  href?: string
  iconPath?: string
  iconColor?: string
}

const props = defineProps<Props>()
const { isDark } = useTheme()

const classes = computed(() =>
  [
    'flex items-center gap-2 whitespace-nowrap rounded-2xl border border-emerald-500/60 px-4 py-1.5 text-[12px] font-semibold uppercase tracking-[0.25em] leading-tight transition',
    isDark.value
      ? 'bg-emerald-700/30 text-emerald-100 hover:border-emerald-400/90 hover:bg-emerald-500/20'
      : 'bg-transparent text-emerald-600 hover:border-emerald-400 hover:bg-emerald-50',
    props.href ? 'cursor-pointer' : 'cursor-default'
  ].join(' ')
)

const strokeColor = computed(() => props.iconColor || 'currentColor')
</script>

<template>
  <NuxtLink v-if="props.href" :to="props.href" :class="classes">
    <svg v-if="props.iconPath" class="h-5 w-5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">
      <path :d="props.iconPath" :stroke="strokeColor" />
    </svg>
    <span>
      <slot />
    </span>
  </NuxtLink>
  <span v-else :class="classes">
    <svg v-if="props.iconPath" class="h-5 w-5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor"
      stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">
      <path :d="props.iconPath" :stroke="strokeColor" />
    </svg>
    <span>
      <slot />
    </span>
  </span>
</template>
