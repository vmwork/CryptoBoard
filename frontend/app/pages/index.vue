<template>
  <div class="min-h-screen bg-background text-foreground">
    <div class="mx-auto flex w-full max-w-6xl flex-col gap-10 px-4 py-8 sm:px-6 lg:px-8">
      <section v-for="section in sections" :key="section.id" :id="section.id"
        class="space-y-4 border-b border-border/20 py-12 last:border-b-0 last:pb-6">
        <div class="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h2 class="text-2xl font-semibold text-foreground">{{ section.title }}</h2>
          </div>
          <NuxtLink :to="section.href"
            class="text-sm font-semibold uppercase tracking-[0.3em] text-[#10B981] transition hover:text-emerald-200">
            Перейти в раздел
            <span aria-hidden="true">↗</span>
          </NuxtLink>
        </div>
        <p class="text-sm text-muted-foreground">{{ section.description }}</p>
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3" role="list"
          :aria-label="`${section.title} — отобранные объявления`">
          <ListingCard v-for="listing in section.listings" :key="listing.id" :title="listing.title"
            :subtitle="listing.subtitle" :image="listing.image" :price="listing.price" :seller="listing.seller"
            :status="listing.status" :href="listing.href" />
        </div>
      </section>
    </div>

    <footer class="mt-12 border-t border-border/30 bg-card/90 text-muted-foreground">
      <div class="mx-auto flex w-full max-w-6xl flex-col gap-6 px-4 py-8 sm:px-6 lg:px-8">
        <div class="flex flex-col gap-3 border-b border-border/40 pb-4 sm:flex-row sm:items-center sm:justify-between">
          <div class="flex items-center gap-3">
            <svg width="220" height="44" viewBox="0 0 220 44" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g transform="translate(0, 4)">
                <path d="M16 2L4 6V12C4 18 8 24 16 26C24 24 28 18 28 12V6L16 2Z" stroke="#00DC82" stroke-width="2"
                  stroke-linejoin="round" />
                <path d="M11 14L14 17L21 10" stroke="#00DC82" stroke-width="2.5" stroke-linecap="round"
                  stroke-linejoin="round" />
              </g>
              <text x="38" y="30" font-family="'Inter', 'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700"
                fill="#1A1A1A" letter-spacing="0">Crypto</text>
              <text x="124" y="30" font-family="'Inter', 'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700"
                fill="#00DC82" letter-spacing="0">Board</text>
            </svg>
            <div>
              <p class="text-xs font-semibold uppercase tracking-[0.3em] text-muted-foreground/70">© 2026 Classifyd</p>
              <p class="text-[11px] text-muted-foreground/80">Non-custodial escrow marketplace</p>
            </div>
          </div>
          <div class="flex flex-wrap items-center gap-4 text-xs font-semibold uppercase tracking-[0.3em]">
            <NuxtLink to="/terms" class="transition hover:text-foreground text-muted-foreground">Terms</NuxtLink>
            <NuxtLink to="/privacy" class="transition hover:text-foreground text-muted-foreground">Privacy</NuxtLink>
            <NuxtLink to="/faq" class="transition hover:text-foreground text-muted-foreground">FAQ</NuxtLink>
            <NuxtLink to="/support" class="transition hover:text-foreground text-muted-foreground">Support</NuxtLink>
          </div>
        </div>
        <div class="grid gap-3 md:grid-cols-2">
          <div class="flex flex-wrap items-center gap-2">
            <span class="text-[11px] font-semibold uppercase tracking-[0.3em] text-muted-foreground/70">Язык</span>
            <button
              class="rounded-full border border-border/70 px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.3em] text-muted-foreground transition hover:border-emerald-400/70">EN</button>
            <button
              class="rounded-full border border-border/70 px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.3em] text-muted-foreground transition hover:border-emerald-400/70">RU</button>
          </div>
          <div class="flex flex-wrap items-center gap-2">
            <span class="text-[11px] font-semibold uppercase tracking-[0.3em] text-muted-foreground/70">Сеть</span>
            <button
              class="rounded-full border border-border/70 px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.3em] text-muted-foreground transition hover:border-emerald-400/70">Mainnet</button>
            <button
              class="rounded-full border border-border/70 px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.3em] text-muted-foreground transition hover:border-emerald-400/70">Testnet</button>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import ListingCard from '@/components/ListingCard.vue'
import { sections as sectionsData } from '@/data/sections'

definePageMeta({
  title: 'Marketplace — Classifyd',
  layout: 'default'
})

const sections = sectionsData
</script>
