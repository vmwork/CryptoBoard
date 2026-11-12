import { computed } from 'vue'
import { useCookie, useState } from '#imports'

type Theme = 'light' | 'dark'
const THEME_STORAGE_KEY = 'classifyd_theme'
const DEFAULT_THEME: Theme = 'dark'
const isClient = process.client

let hasClientInitialized = false

const isValidTheme = (value: unknown): value is Theme => value === 'light' || value === 'dark'

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

export const useTheme = () => {
    const themeStateRef = useState<Theme>('classifyd_theme_state', () => DEFAULT_THEME)
    const themeCookie = useCookie<Theme | undefined>(THEME_STORAGE_KEY)

    if (process.server) {
        const persistedCookie = themeCookie.value
        themeStateRef.value = isValidTheme(persistedCookie) ? persistedCookie : DEFAULT_THEME
    }

    if (isClient && !hasClientInitialized) {
        hasClientInitialized = true

        const cookieTheme = isValidTheme(themeCookie.value) ? themeCookie.value : null
        let initialTheme: Theme = themeStateRef.value

        if (cookieTheme) {
            initialTheme = cookieTheme
        } else {
            const persistedStorage = localStorage.getItem(THEME_STORAGE_KEY)
            if (isValidTheme(persistedStorage)) {
                initialTheme = persistedStorage
            }
        }

        themeStateRef.value = initialTheme
        applyClasses(initialTheme)
        themeCookie.value = initialTheme
        localStorage.setItem(THEME_STORAGE_KEY, initialTheme)
    }

    const persistTheme = (value: Theme) => {
        themeCookie.value = value
        if (isClient) {
            localStorage.setItem(THEME_STORAGE_KEY, value)
        }
    }

    const setTheme = (value: Theme) => {
        if (themeStateRef.value !== value) {
            themeStateRef.value = value
        }

        if (isClient) {
            applyClasses(value)
        }
        persistTheme(value)
    }

    const toggleTheme = () => {
        const next: Theme = themeStateRef.value === 'dark' ? 'light' : 'dark'
        setTheme(next)
    }

    return {
        theme: computed(() => themeStateRef.value),
        isDark: computed(() => themeStateRef.value === 'dark'),
        setTheme,
        toggleTheme
    }
}
