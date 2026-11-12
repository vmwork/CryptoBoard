<template>
  <div class="min-h-screen bg-background text-foreground">
    <div class="mx-auto flex w-full max-w-6xl flex-col gap-10 px-4 py-8 sm:px-6 lg:px-8">
      <header
        class="rounded-[32px] border border-border bg-card/90 px-5 py-6 shadow-[0_20px_60px_rgba(5,120,87,0.12)] backdrop-blur">
        <div class="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
          <NuxtLink to="/" class="flex items-center gap-3">
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-emerald-500/10 text-emerald-400 shadow-inner">
              <span class="text-lg font-semibold">CB</span>
            </div>
            <div>
              <p class="text-xs font-semibold uppercase tracking-[0.4em] text-muted-foreground">Classifyd</p>
              <p class="text-[11px] uppercase tracking-[0.4em] text-muted-foreground/80">Marketplace-first</p>
            </div>
          </NuxtLink>
          <div
            class="flex flex-1 items-center gap-3 rounded-2xl border border-border bg-background/60 px-3 py-2 shadow-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-muted-foreground" fill="none"
              viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 6.05 6.05a7.5 7.5 0 0 0 10.6 10.6z" />
            </svg>
            <input type="search" placeholder="Найти GPU, ферму, скрипт или продавца"
              class="flex-1 bg-transparent text-sm font-medium placeholder:text-muted-foreground focus:outline-none" />
            <button type="button"
              class="rounded-2xl border border-border px-3 py-1 text-[11px] font-semibold uppercase tracking-[0.3em] text-foreground transition hover:border-emerald-400/80 hover:text-emerald-400">
              Поиск
            </button>
          </div>
          <div class="flex flex-wrap items-center justify-end gap-2">
            <button type="button" :aria-label="toggleLabel"
              class="rounded-full border border-border bg-background/60 p-2 text-sm text-muted-foreground transition hover:border-emerald-400/70 hover:text-emerald-300"
              @click="toggleTheme">
              <span v-if="isDark" aria-hidden="true">🌙</span>
              <span v-else aria-hidden="true">☀️</span>
            </button>
            <NuxtLink to="/auth"
              class="rounded-full border border-border px-4 py-2 text-xs font-semibold uppercase tracking-[0.3em] text-muted-foreground transition hover:border-emerald-400/70 hover:text-foreground">
              SIWE
            </NuxtLink>
            <a href="https://t.me/classifyd_market" target="_blank" rel="noopener noreferrer"
              class="rounded-full border border-border px-4 py-2 text-xs font-semibold uppercase tracking-[0.3em] text-muted-foreground transition hover:border-emerald-400/70 hover:text-foreground">
              Telegram
            </a>
            <NuxtLink to="/market/new"
              class="rounded-full bg-emerald-500 px-4 py-2 text-xs font-semibold uppercase tracking-[0.3em] text-white transition hover:bg-emerald-500/90">
              Создать объявление
            </NuxtLink>
          </div>
        </div>
        <div
          class="mt-5 grid grid-cols-2 gap-3 text-[11px] font-semibold uppercase tracking-[0.4em] text-muted-foreground sm:grid-cols-5">
          <NuxtLink v-for="category in categoryGrid" :key="category.id" :to="category.href"
            class="flex items-center justify-between rounded-2xl border border-border bg-background/40 px-3 py-2 transition hover:border-emerald-400/80 hover:text-emerald-300">
            <span>{{ category.name }}</span>
            <span aria-hidden="true">↗</span>
          </NuxtLink>
        </div>
      </header>


      <section v-for="section in sections" :key="section.id" :id="section.id"
        class="space-y-4 border-b border-border/20 py-12 last:border-b-0 last:pb-6">
        <div class="flex flex-wrap items-end justify-between gap-3">
          <div>
            <p class="text-xs uppercase tracking-[0.4em] text-muted-foreground">Категория</p>
            <h2 class="text-2xl font-semibold text-foreground">{{ section.title }}</h2>
          </div>
          <NuxtLink :to="section.href"
            class="text-sm font-semibold uppercase tracking-[0.3em] text-[#10B981] transition hover:text-emerald-200">
            Смотреть всё
            <span aria-hidden="true">↗</span>
          </NuxtLink>
        </div>
        <p class="text-sm text-muted-foreground">{{ section.description }}</p>
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3" role="list"
          :aria-label="`${section.title} — отобранные объявления`">
          <ListingCard v-for="listing in section.listings" :key="listing.id" :title="listing.title"
            :subtitle="listing.subtitle" :image="listing.image" :price="listing.price" :seller="listing.seller"
            :status="listing.status" :href="listing.href" :badge="listing.badge" />
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
import { computed } from 'vue'
import ListingCard from '@/components/ListingCard.vue'
import { useTheme } from '~/composables/useTheme'

definePageMeta({
  title: 'Marketplace — Classifyd',
  layout: 'default'
})

interface Listing {
  id: string
  title: string
  subtitle: string
  price: number
  seller: string
  status: string
  image?: string
  badge?: string
  href: string
}

interface Section {
  id: string
  title: string
  description: string
  href: string
  listings: Listing[]
}

const { isDark, toggleTheme } = useTheme()
const toggleLabel = computed(() => (isDark.value ? 'Переключить на светлую тему' : 'Переключить на тёмную тему'))

const sections: Section[] = [
  {
    id: 'gpu',
    title: 'GPU и фермы',
    description: 'High-end видеокарты и собранные фермы с Eliminator-контролями и преднастройками для USDT эскроу.',
    href: '/market/gpu',
    listings: [
      {
        id: 'gpu-rtx4090',
        title: 'NVIDIA RTX 4090 Founders Edition',
        subtitle: '520W mining-ready card',
        price: 3850,
        seller: 'HydraPool Oxide',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1200&q=80',
        href: '/market/gpu/rtx-4090'
      },
      {
        id: 'gpu-farm-12x3080',
        title: 'Ферма 12x RTX 3080 Ti',
        subtitle: 'Lithium battery-friendly frame',
        price: 21800,
        seller: 'Avalanche Rigs',
        status: 'Ожидается пополнение',
        image: 'https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=1200&q=80',
        href: '/market/gpu/farm-12x3080'
      },
      {
        id: 'gpu-4090-ds',
        title: 'Dual-slot GPU rig (2x 4090)',
        subtitle: 'Silent cooling + MSRP bundle',
        price: 7290,
        seller: 'SilentFuse',
        status: 'Подтвердили доставку',
        image: 'https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1200&q=80',
        href: '/market/gpu/dual-4090'
      }
    ]
  },
  {
    id: 'asic',
    title: 'ASIC-майнеры',
    description: 'Управляемые фермы на Antminer, Obelisk и DragonMint с собственным NFT-Deal Certificate.',
    href: '/market/asic',
    listings: [
      {
        id: 'asic-s21',
        title: 'Antminer S21+ 120 TH',
        subtitle: 'С UPS и тепловым обменом',
        price: 5200,
        seller: 'HashFrontier',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1581092124619-4f6f8bec66d4?auto=format&fit=crop&w=1200&q=80',
        href: '/market/asic/antminer-s21'
      },
      {
        id: 'asic-d12',
        title: 'DragonMint D12 300 TH',
        subtitle: 'СЕРВЕР-стойка PRE-ORDER',
        price: 14500,
        seller: 'Molten Labs',
        status: 'Предзаказ',
        image: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?auto=format&fit=crop&w=1200&q=80',
        href: '/market/asic/dragonmint-d12'
      },
      {
        id: 'asic-obs-1',
        title: 'Obelisk SC-1 с liquid cooling',
        subtitle: 'Поставка в течение 7 дней',
        price: 3300,
        seller: 'Noble Mines',
        status: 'Готовится к доставке',
        image: 'https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=1200&q=80',
        href: '/market/asic/obelisk-sc1'
      }
    ]
  },
  {
    id: 'smartphones',
    title: 'Смартфоны и гаджеты',
    description: 'Флагманские смартфоны с аппаратным кошельком и поддержкой SIWE + Telegram Mini App.',
    href: '/market/smartphones',
    listings: [
      {
        id: 'phone-pixel',
        title: 'Google Pixel 8 Pro 512ГБ',
        subtitle: 'Монтаж в заводской коробке',
        price: 999,
        seller: 'SignalGear',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=780&q=80',
        href: '/market/smartphones/pixel-8-pro'
      },
      {
        id: 'phone-iphone',
        title: 'iPhone 15 Pro Max | Siwe Ready',
        subtitle: 'Ботовой проверкой',
        price: 1250,
        seller: 'NeonBox',
        status: 'Ограниченный выпуск',
        image: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=780&q=80',
        href: '/market/smartphones/iphone-15-pro'
      },
      {
        id: 'phone-telegram',
        title: 'Telegram Mini App Phone Pack',
        subtitle: 'Deeplink + ICP',
        price: 860,
        seller: 'ChainMobile',
        status: 'Скоро',
        image: 'https://images.unsplash.com/photo-1510557880182-3b7a2b7b9d06?auto=format&fit=crop&w=780&q=80',
        href: '/market/smartphones/telegram-pack'
      }
    ]
  },
  {
    id: 'cpu',
    title: 'Процессоры и память',
    description: 'Бесшумные комплекты с ECC RAM и SKU, подготовленные под CSI (Cold Storage Infra).',
    href: '/market/cpu',
    listings: [
      {
        id: 'cpu-7950x3d',
        title: 'AMD Ryzen 9 7950X3D',
        subtitle: 'Стерильный SO-DIMM набор',
        price: 800,
        seller: 'Quantum Vault',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1451680093337-1ff1a011cdd7?auto=format&fit=crop&w=1200&q=80',
        href: '/market/cpu/ryzen-7950x3d'
      },
      {
        id: 'ram-lpddr5x',
        title: '64ГБ DDR5 ECC 6400',
        subtitle: 'Встроенный Shield-Passport',
        price: 420,
        seller: 'Element42',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80',
        href: '/market/cpu/ddr5-ecc'
      },
      {
        id: 'cpu-intel',
        title: 'Intel Core i9-14900K',
        subtitle: 'OEM + thermal paste bundle',
        price: 670,
        seller: 'DarkGrid',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1481277542470-605612bd2d61?auto=format&fit=crop&w=1200&q=80',
        href: '/market/cpu/intel-i9-14900k'
      }
    ]
  },
  {
    id: 'software',
    title: 'Софт и скрипты',
    description: 'Скрипты управления фермами, auto-reprice, QA-статусы и white-label бэкенды под NFT Deal Certificate.',
    href: '/market/software',
    listings: [
      {
        id: 'soft-reprice',
        title: 'Auto-Reprice Suite v1.2',
        subtitle: 'Бот фиксирует цены в реальном времени',
        price: 299,
        seller: 'ScriptCraft',
        status: 'Предзаказ',
        image: 'https://images.unsplash.com/photo-1502880195258-7d8b531d07b2?auto=format&fit=crop&w=1200&q=80',
        href: '/market/software/auto-reprice'
      },
      {
        id: 'soft-escrow',
        title: 'Escrow Monitor Dashboard',
        subtitle: 'Webhook + SIWE session guard',
        price: 420,
        seller: 'NodeForge',
        status: 'В наличии',
        image: 'https://images.unsplash.com/photo-1517430816045-df4b93c5e4a0?auto=format&fit=crop&w=1200&q=80',
        href: '/market/software/escrow-monitor'
      },
      {
        id: 'soft-inventory',
        title: 'Immutable Inventory Sync',
        subtitle: 'Cloudflare Worker + Dragonfly cache',
        price: 180,
        seller: 'CacheCrafters',
        status: 'Пилотное',
        image: 'https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=1200&q=80',
        href: '/market/software/inventory-sync'
      }
    ]
  }
]

const categoryGrid = sections.map((section) => ({
  id: section.id,
  name: section.title,
  href: `#${section.id}`
}))
</script>
