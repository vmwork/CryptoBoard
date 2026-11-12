import { computed, ref } from 'vue'

type Theme = 'light' | 'dark'
const THEME_STORAGE_KEY = 'classifyd_theme'
const DEFAULT_THEME: Theme = 'dark'
const isClient = process.client

const themeState = ref<Theme>(DEFAULT_THEME)

if (isClient) {
    const persisted = localStorage.getItem(THEME_STORAGE_KEY) as Theme | null
    if (persisted === 'light' || persisted === 'dark') {
        themeState.value = persisted
    }
}

const applyClasses = (value: Theme) => {
    if (!isClient) {
        return
    }

    const root = document.documentElement
    root.classList.toggle('dark', value === 'dark')
    root.classList.toggle('light', value === 'light')
    document.body?.classList.toggle('dark', value === 'dark')
    document.body?.classList.toggle('light', value === 'light')
}

const persist = (value: Theme) => {
    if (!isClient) {
        return
    }

    localStorage.setItem(THEME_STORAGE_KEY, value)
}

applyClasses(themeState.value)
persist(themeState.value)

const setTheme = (value: Theme) => {
    if (themeState.value !== value) {
        themeState.value = value
    }

    applyClasses(value)
    persist(value)
}

const toggleTheme = () => {
    const next: Theme = themeState.value === 'dark' ? 'light' : 'dark'
    setTheme(next)
}

export const useTheme = () => ({
    theme: computed(() => themeState.value),
    isDark: computed(() => themeState.value === 'dark'),
    setTheme,
    toggleTheme
})
