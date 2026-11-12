import { defineConfig } from 'tailwindcss'
import type { Config } from 'tailwindcss'

const variableColors = {
  background: 'var(--background)',
  foreground: 'var(--foreground)',
  card: 'var(--card)',
  'card-foreground': 'var(--card-foreground)',
  popover: 'var(--popover)',
  'popover-foreground': 'var(--popover-foreground)',
  border: 'var(--border)',
  ring: 'var(--ring)',
  input: 'var(--input)',
  muted: 'var(--muted)',
  'muted-foreground': 'var(--muted-foreground)',
  accent: 'var(--accent)',
  'accent-foreground': 'var(--accent-foreground)',
  primary: 'var(--primary)',
  'primary-foreground': 'var(--primary-foreground)',
  secondary: 'var(--secondary)',
  'secondary-foreground': 'var(--secondary-foreground)',
  destructive: 'var(--destructive)',
  sidebar: 'var(--sidebar)',
  'sidebar-foreground': 'var(--sidebar-foreground)',
  'sidebar-primary': 'var(--sidebar-primary)',
  'sidebar-primary-foreground': 'var(--sidebar-primary-foreground)',
  'sidebar-accent': 'var(--sidebar-accent)',
  'sidebar-accent-foreground': 'var(--sidebar-accent-foreground)',
  'sidebar-border': 'var(--sidebar-border)',
  'sidebar-ring': 'var(--sidebar-ring)',
  'chart-1': 'var(--chart-1)',
  'chart-2': 'var(--chart-2)',
  'chart-3': 'var(--chart-3)',
  'chart-4': 'var(--chart-4)',
  'chart-5': 'var(--chart-5)'
} as const

const config: Config = {
  content: [
    './app/**/*.{vue,ts,tsx,js,jsx}',
    './components/**/*.{vue,ts,tsx,js,jsx}',
    './layouts/**/*.{vue,ts,tsx,js,jsx}',
    './pages/**/*.{vue,ts,tsx,js,jsx}',
    './composables/**/*.{ts,js}',
    './server/**/*.{ts,js}',
    './nuxt.config.ts'
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: variableColors,
      fontFamily: {
        sans: ['Onest', 'DM Sans', 'sans-serif']
      }
    }
  },
  plugins: []
}

export default defineConfig(config)
