<script setup lang="ts">
import { useAttrs } from 'vue'

const attrs = useAttrs()
</script>

<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="1.5"
    stroke-linecap="round"
    stroke-linejoin="round"
    role="img"
    aria-hidden="true"
    focusable="false"
    :class="['icon-nft', attrs.class]"
    v-bind="attrs"
  >
    <rect x="3" y="3" width="18" height="18" rx="3.5" />
    <path d="M7.5 17.5V7.5" />
    <path d="M7.5 7.5L11.5 17.5" />
    <path d="M11.5 7.5V17.5" />
    <path d="M12.5 7.5V17.5" />
    <path d="M12.5 7.5H15.5" />
    <path d="M12.5 12.25H15" />
    <path d="M17.5 7.5V17.5" />
    <path d="M14.5 7.5H20.5" />
  </svg>
</template>
