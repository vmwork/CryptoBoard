<script setup lang="ts">
import { computed } from 'vue'
import type { PropType } from 'vue'

const variantClasses: Record<"accent" | "ghost" | "solid", string> = {
  accent:
    'border border-emerald-500/70 bg-white text-foreground shadow-[0_10px_30px_rgba(16,185,129,0.15)] transition duration-200 hover:border-emerald-400/80 hover:bg-emerald-50 hover:text-foreground dark:border-emerald-500/60 dark:bg-emerald-500/20 dark:text-emerald-100 dark:hover:border-emerald-400/90 dark:hover:bg-emerald-400/30',
  ghost:
    'border border-border/60 bg-background/70 text-foreground/90 hover:border-emerald-500/80 hover:bg-emerald-500/10 hover:text-foreground dark:border-emerald-500/60 dark:bg-card/20 dark:text-emerald-100 dark:hover:border-emerald-400/80 dark:hover:bg-emerald-400/20',
  solid:
    'border border-emerald-600 bg-emerald-500 text-white hover:border-emerald-400 hover:bg-emerald-400'
}

const sizeClasses: Record<"sm" | "md" | "lg", string> = {
  sm: 'px-4 py-2 text-[11px]',
  md: 'px-5 py-3 text-xs',
  lg: 'px-6 py-3.5 text-sm'
}

const props = defineProps({
  variant: {
    type: String as PropType<'accent' | 'ghost' | 'solid'>,
    default: 'accent'
  },
  size: {
    type: String as PropType<'sm' | 'md' | 'lg'>,
    default: 'md'
  },
  to: String,
  href: String,
  type: {
    type: String as PropType<'button' | 'submit' | 'reset'>,
    default: 'button'
  },
  disabled: Boolean,
  fullWidth: Boolean
})

const classes = computed(() =>
  [
    'inline-flex items-center justify-center gap-2 rounded-full font-semibold uppercase tracking-[0.3em] transition shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-300/80',
    variantClasses[props.variant],
    sizeClasses[props.size],
    props.fullWidth ? 'w-full' : ''
  ]
    .filter(Boolean)
    .join(' ')
)
</script>

<template>
  <NuxtLink
    v-if="props.to"
    :to="props.to"
    :class="classes"
    v-bind="$attrs"
  >
    <slot />
  </NuxtLink>
  <a
    v-else-if="props.href"
    :href="props.href"
    :class="classes"
    v-bind="$attrs"
  >
    <slot />
  </a>
  <button
    v-else
    :type="props.type"
    :disabled="props.disabled"
    :class="classes"
    v-bind="$attrs"
  >
    <slot />
  </button>
</template>
