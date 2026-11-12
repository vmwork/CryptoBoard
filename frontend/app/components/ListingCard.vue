<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from '#imports'
import TagBadge from '@/components/ui/TagBadge.vue'
import AppButton from '@/components/ui/AppButton.vue'

interface ListingCardProps {
  title: string
  subtitle?: string
  description?: string
  price: number
  currency?: string
  seller: string
  condition?: 'new' | 'used'
  image?: string
  tags?: string[]
  href?: string
}

const props = withDefaults(defineProps<ListingCardProps>(), {
  currency: 'USDT',
  condition: 'new',
  tags: [],
  description: '',
  href: '/market'
})

const router = useRouter()

const formattedPrice = computed(() => {
  const amount = Number(props.price)
  if (Number.isNaN(amount)) {
    return `${props.price} ${props.currency}`
  }
  const formatter = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: amount % 1 === 0 ? 0 : 2,
    maximumFractionDigits: 2
  })
  return `${formatter.format(amount)} ${props.currency}`
})

const displayTags = computed(() => {
  const filtered = (props.tags ?? []).map((tag) => tag.trim()).filter((tag) => tag.length)
  return filtered.length ? filtered.slice(0, 6) : ['#USDT', '#P2P']
})

const descriptionText = computed(() => (props.description ?? '').trim())
const conditionLabel = computed(() => (props.condition === 'used' ? 'Б/У' : 'НОВОЕ'))

const goToListing = () => {
  router.push(props.href ?? '/market')
}

const isFavorited = ref(false)
const toggleFavorite = () => {
  isFavorited.value = !isFavorited.value
}

const favoriteClasses = computed(() =>
  isFavorited.value
    ? 'text-rose-400 border-rose-500/50 bg-rose-500/20'
    : 'text-muted-foreground border-white/20 bg-transparent'
)
</script>

<template>
  <article role="button" tabindex="0"
    class="group flex h-full flex-col overflow-hidden rounded-[28px] border border-border bg-card text-card-foreground shadow-[0_20px_60px_rgba(0,0,0,0.45)] transition hover:-translate-y-0.5 hover:shadow-[0_30px_80px_rgba(16,185,129,0.35)]"
    @click="goToListing" @keyup.enter="goToListing">
    <div class="relative">
      <div class="aspect-[16/9] w-full overflow-hidden rounded-t-[28px] border-b border-border/20 bg-[#050b08]">
        <div v-if="props.image" class="h-full w-full">
          <img :src="props.image" :alt="props.title"
            class="h-full w-full object-cover transition duration-300 group-hover:scale-[1.03]" loading="lazy" />
        </div>
        <div v-else class="h-full w-full"
          style="background-image: repeating-linear-gradient(135deg, rgba(255, 255, 255, 0.03) 0 8px, transparent 8px 16px), radial-gradient(circle at 20% 20%, rgba(16, 185, 129, 0.5), transparent 40%); background-color: #040b08;" />
      </div>
      <span
        class="absolute left-3 top-3 inline-flex items-center justify-center rounded-full border border-white/15 bg-black/60 px-3 py-1 text-[11px] font-semibold tracking-[0.3em] text-foreground">
        {{ conditionLabel }}
      </span>
      <button type="button"
        class="absolute right-3 top-3 inline-flex h-10 items-center justify-center rounded-full border bg-white px-2 text-[11px] font-semibold uppercase tracking-[0.2em] transition"
        :class="favoriteClasses" aria-pressed="isFavorited" @click.stop="toggleFavorite">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"
          stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4">
          <path
            d="M12 21C12 21 4 13.5 4 8.5C4 6.29 5.79 4.5 8 4.5C9.5 4.5 10.88 5.24 11.5 6.41C12.12 5.24 13.5 4.5 15 4.5C17.21 4.5 19 6.29 19 8.5C19 13.5 12 21 12 21Z" />
        </svg>
      </button>
    </div>
    <div class="flex flex-1 flex-col gap-3 px-5 py-5">
      <div v-if="displayTags.length" class="flex flex-wrap gap-2">
        <TagBadge v-for="tag in displayTags" :key="tag">
          {{ tag }}
        </TagBadge>
      </div>
      <p v-if="descriptionText" class="text-sm text-muted-foreground"
        style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
        {{ descriptionText }}
      </p>
      <div v-if="props.subtitle" class="text-xs font-semibold text-muted-foreground">
        {{ props.subtitle }}
      </div>
      <div class="space-y-1">
        <p class="text-lg font-semibold leading-tight text-foreground">
          {{ props.title }}
        </p>
        <!-- <p class="text-2xl font-semibold text-[#10B981]">
          {{ formattedPrice }}
        </p> -->
      </div>
      <div class="mt-auto flex items-center justify-between gap-3 border-t border-border/20 pt-4">
        <AppButton variant="ghost" size="sm" @click.stop="goToListing">
          Детали
        </AppButton>
        <p class="text-lg font-semibold text-[#10B981]">
          {{ formattedPrice }}
        </p>
      </div>
    </div>
  </article>
</template>
