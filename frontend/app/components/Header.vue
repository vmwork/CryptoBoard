<script setup lang="ts">
import { computed, ref } from 'vue'
import { useTheme } from '~/composables/useTheme'
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent
} from '@/components/ui/dropdown-menu'
import TagBadge from '@/components/ui/TagBadge.vue'
import AppButton from '@/components/ui/AppButton.vue'

type CategoryLink = {
  id: string
  label: string
  href: string
  iconPath?: string
  iconColor?: string
}

type FilterTag = {
  label: string
  href: string
  iconPath?: string
  iconColor?: string
}

type FilterSection = {
  title: string
  tags: FilterTag[]
}

const { categoryLinks } = defineProps<{ categoryLinks: CategoryLink[] }>()

const searchQuery = ref('')
const hasSearch = computed(() => Boolean(searchQuery.value.trim()))
const clearSearch = () => {
  searchQuery.value = ''
}

const filterSections: FilterSection[] = [
  {
    title: 'Статус',
    tags: [
      { label: 'Новое', href: '/market?status=new', iconPath: 'M12 5v14m-7-7h14' },
      { label: 'Б/У', href: '/market?status=used', iconPath: 'M7 9.5l5 5 5-5' }
    ]
  },
  {
    title: 'Доставка',
    tags: [
      { label: 'USDT Escrow', href: '/market?delivery=escrow', iconPath: 'M5 12h8l-2-2m0 4l2-2H5' },
      { label: 'Самовывоз', href: '/market?delivery=pickup', iconPath: 'M5 6h14v12H5z' }
    ]
  },
  {
    title: 'Продавцы',
    tags: [
      { label: 'Проверенные продавцы', href: '/market?seller=verified', iconPath: 'M6 12l3 3 6-6' }
    ]
  }
]

const { isDark, toggleTheme } = useTheme()
const toggleLabel = computed(() =>
  isDark.value ? 'Переключиться на светлую тему' : 'Переключиться на тёмную тему'
)
</script>

<template>
  <header class="w-full border border-border/30 bg-card/90 shadow-[0_35px_70px_rgba(0,0,0,0.35)]">
    <div class="mx-auto flex max-w-[90vw] flex-col gap-5 px-4 py-6 sm:px-6 lg:px-8">
      <div class="flex w-full flex-wrap items-center gap-4">
        <NuxtLink to="/" class="flex shrink-0 items-center gap-3">
          <div
            class="flex h-12 w-12 items-center justify-center rounded-2xl bg-emerald-500/10 text-emerald-400 shadow-inner">
            <span class="text-lg font-semibold">CB</span>
          </div>
          <div class="flex flex-col text-[11px] uppercase tracking-[0.3em] text-muted-foreground">
            <span class="font-semibold">Classifyd</span>
            <span class="text-muted-foreground/80">Marketplace-first</span>
          </div>
        </NuxtLink>
        <div class="flex flex-[2] min-w-[260px] items-center gap-3">
          <div
            class="flex w-full flex-1 items-center gap-3 rounded-[32px] border border-border/60 bg-background/80 px-4 py-3 shadow-[0_25px_60px_rgba(16,185,129,0.2)] transition duration-200 dark:border-emerald-500/70 dark:bg-[#060b08]/40">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-muted-foreground" fill="none"
              viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 6.05 6.05a7.5 7.5 0 0 0 10.6 10.6z" />
            </svg>
            <input v-model="searchQuery" type="search" placeholder="Найти GPU, ферму, инженера или NFT Deal Certificate"
              class="search-input flex-1 rounded-[24px] border border-transparent bg-white/90 px-2 text-sm font-medium text-foreground placeholder:text-muted-foreground focus:outline-none dark:border-transparent dark:bg-transparent" />
            <button :tabindex="hasSearch ? 0 : -1" :aria-hidden="!hasSearch" type="button" @click="clearSearch"
              class="flex h-9 w-9 items-center justify-center rounded-full border border-emerald-500/70 bg-white text-emerald-600 transition hover:border-emerald-400/80 hover:bg-emerald-50 dark:border-emerald-400/90 dark:bg-emerald-500/20 dark:text-emerald-100"
              :class="hasSearch ? '' : 'opacity-0 pointer-events-none'">
              <span aria-hidden="true">✕</span>
              <span class="sr-only">Очистить запрос</span>
            </button>
          </div>
          <AppButton variant="accent" size="md" type="button">
            Поиск
          </AppButton>
        </div>
        <div class="flex items-center gap-2">
          <button type="button" :aria-label="toggleLabel"
            class="rounded-full border border-emerald-500/60 bg-[#060b08]/40 p-2 text-sm text-emerald-100 transition hover:bg-emerald-500/10 hover:text-white"
            @click="toggleTheme">
            <span v-if="isDark" aria-hidden="true">🌙</span>
            <span v-else aria-hidden="true">☀️</span>
          </button>
          <AppButton to="/auth" variant="ghost" size="md">
            Войти / Регистрация
          </AppButton>
        </div>
      </div>
      <div class="flex flex-wrap items-center gap-3">
        <DropdownMenu>
          <DropdownMenuTrigger
            class="flex items-center justify-between gap-2 rounded-[26px] border border-border bg-white px-4 py-3 text-[11px] font-semibold uppercase tracking-[0.3em] text-foreground transition duration-200 hover:border-emerald-400 hover:text-foreground dark:border-emerald-500/70 dark:bg-card/20 dark:text-emerald-100">
            <span>Категории</span>
            <svg aria-hidden="true" class="h-4 w-4 text-foreground/90 dark:text-emerald-100" viewBox="0 0 12 12"
              fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">
              <path d="M2 4.5 6 8.5 10 4.5" />
            </svg>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            class="w-[360px] min-w-[340px] max-w-[420px] overflow-hidden rounded-[26px] border border-border bg-white/95 p-4 text-foreground shadow-[0_30px_60px_rgba(5,120,87,0.15)] dark:border-border/20 dark:bg-card/90 dark:text-emerald-50">
            <div class="space-y-3">
              <p class="text-[10px] uppercase tracking-[0.4em] text-muted-foreground/70">Рынок</p>
              <div class="flex flex-wrap gap-2">
                <TagBadge v-for="link in categoryLinks" :key="link.id" :href="link.href" :icon-path="link.iconPath"
                  :icon-color="link.iconColor">
                  <span class="text-center leading-tight">{{ link.label }}</span>
                </TagBadge>
              </div>
            </div>
          </DropdownMenuContent>
        </DropdownMenu>
        <DropdownMenu>
          <DropdownMenuTrigger
            class="flex items-center justify-between gap-2 rounded-[26px] border border-border bg-white px-4 py-3 text-[11px] font-semibold uppercase tracking-[0.3em] text-foreground transition duration-200 hover:border-emerald-400 hover:text-foreground dark:border-emerald-500/70 dark:bg-card/20 dark:text-emerald-100">
            <span>Фильтры</span>
            <svg aria-hidden="true" class="h-4 w-4 text-foreground/90 dark:text-emerald-100" viewBox="0 0 12 12"
              fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">
              <path d="M2 4.5 6 8.5 10 4.5" />
            </svg>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            class="w-[380px] max-w-[420px] overflow-hidden rounded-[26px] border border-border bg-white/95 p-4 text-foreground shadow-[0_30px_60px_rgba(5,120,87,0.15)] dark:border-border/20 dark:bg-card/90 dark:text-emerald-50">
            <div class="project-scrollbar max-h-[320px] overflow-y-auto pr-1">
              <div class="space-y-4">
                <div v-for="section in filterSections" :key="section.title" class="space-y-2">
                  <p class="text-[10px] uppercase tracking-[0.4em] text-muted-foreground/70">{{ section.title }}</p>
                  <div class="flex flex-wrap gap-2">
                    <TagBadge v-for="tag in section.tags" :key="tag.label" :href="tag.href" :icon-path="tag.iconPath"
                      :icon-color="tag.iconColor">
                      {{ tag.label }}
                    </TagBadge>
                  </div>
                </div>
              </div>
            </div>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </div>
  </header>
</template>

<style scoped>
.search-input::-webkit-search-decoration,
.search-input::-webkit-search-cancel-button,
.search-input::-webkit-search-results-button,
.search-input::-webkit-search-results-decoration {
  -webkit-appearance: none;
  appearance: none;
}
</style>
