export interface Listing {
  id: string
  title: string
  subtitle: string
  price: number
  seller: string
  status: string
  image?: string
  href: string
}

export interface Section {
  id: string
  title: string
  description: string
  href: string
  iconPath?: string
  iconColor?: string
  listings: Listing[]
}

export const sections: Section[] = [
  {
    id: 'gpu',
    title: 'GPU и фермы',
    iconPath: 'M5 7h14v10H5z M7 11h2 M7 13h2 M15 11h2 M15 13h2',
    iconColor: '#34d399',
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
      },
      {
        id: 'gpu-farm-12x3080-2',
        title: 'Ферма 12x RTX 3080 Ti',
        subtitle: 'Lithium battery-friendly frame',
        price: 21800,
        seller: 'Avalanche Rigs',
        status: 'Ожидается пополнение',
        image: 'https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=1200&q=80',
        href: '/market/gpu/farm-12x3080'
      },
      {
        id: 'gpu-4090-ds-2',
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
    iconPath: 'M5 6h14v12H5z M8 9h8 M8 13h8',
    iconColor: '#22c55e',
    description: 'Управляемые фермы на Antminer, Obelisk и DragonMint с собственным NFT-Deal Certificate.',
    href: '/market/asic',
    listings: [
      {
        id: 'asic-s21',
        title: 'Bitmain Antminer S21 90TH/s',
        subtitle: 'Attack-proof hashing',
        price: 2980,
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
    iconPath: 'M10 4h4v16h-4z M11 18h2 M11 6h2',
    iconColor: '#14b8a6',
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
    iconPath: 'M7 8h10v8H7z M7 12h2 M15 12h2',
    iconColor: '#38bdf8',
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
    iconPath: 'M6 5h12l4 5v6l-4 5H6l-4-5V10z M9 8h6 M9 12h6',
    iconColor: '#a855f7',
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

export const categoryLinks = sections.map((section) => ({
  id: section.id,
  label: section.title,
  href: `#${section.id}`,
  iconPath: section.iconPath,
  iconColor: section.iconColor
}))
