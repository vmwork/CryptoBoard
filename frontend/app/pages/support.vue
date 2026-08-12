<template>
    <div class="min-h-screen bg-neutral-50">
        <div class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
            <!-- Навигация назад -->
            <div class="mb-8">
                <NuxtLink to="/"
                    class="inline-flex items-center gap-2 text-sm text-neutral-600 transition hover:text-neutral-900">
                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    На главную
                </NuxtLink>
            </div>

            <!-- Контент -->
            <div class="overflow-hidden rounded-2xl bg-white shadow-sm">
                <div class="border-b border-neutral-100 px-6 py-8 sm:px-10 sm:py-10">
                    <div class="flex items-center gap-3">
                        <div class="rounded-full bg-primary/10 p-3 text-primary">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                            </svg>
                        </div>
                        <div>
                            <h1 class="text-3xl font-bold text-neutral-900 sm:text-4xl">
                                Служба поддержки
                            </h1>
                            <p class="mt-1 text-neutral-600">
                                Мы ответим в течение 24 часов
                            </p>
                        </div>
                    </div>
                </div>

                <div class="px-6 py-8 sm:px-10 sm:py-10">
                    <!-- Альтернативные контакты -->
                    <div class="mb-8 grid gap-4 sm:grid-cols-3">
                        <div class="rounded-xl border border-neutral-100 bg-neutral-50 p-4 text-center">
                            <svg class="mx-auto h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                            <p class="mt-1 text-sm font-medium text-neutral-900">Email</p>
                            <a href="mailto:support@cryptoboard.com" class="text-sm text-primary hover:underline">
                                support@cryptoboard.com
                            </a>
                        </div>

                        <div class="rounded-xl border border-neutral-100 bg-neutral-50 p-4 text-center">
                            <svg class="mx-auto h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                            </svg>
                            <p class="mt-1 text-sm font-medium text-neutral-900">Telegram</p>
                            <a href="#" class="text-sm text-primary hover:underline">
                                @cryptoboard_support
                            </a>
                        </div>

                        <div class="rounded-xl border border-neutral-100 bg-neutral-50 p-4 text-center">
                            <svg class="mx-auto h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <p class="mt-1 text-sm font-medium text-neutral-900">Время ответа</p>
                            <p class="text-sm text-neutral-600">Обычно в течение 24 ч</p>
                        </div>
                    </div>

                    <!-- Форма обратной связи -->
                    <form @submit.prevent="handleSubmit" class="space-y-6">
                        <div class="grid gap-6 sm:grid-cols-2">
                            <!-- Имя -->
                            <div>
                                <label for="name" class="block text-sm font-medium text-neutral-700">
                                    Ваше имя <span class="text-red-500">*</span>
                                </label>
                                <input id="name" v-model="form.name" type="text" required
                                    class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                    placeholder="Иван Иванов" />
                            </div>

                            <!-- Email -->
                            <div>
                                <label for="email" class="block text-sm font-medium text-neutral-700">
                                    Email <span class="text-red-500">*</span>
                                </label>
                                <input id="email" v-model="form.email" type="email" required
                                    class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                    placeholder="example@email.com" />
                            </div>
                        </div>

                        <!-- Тема -->
                        <div>
                            <label for="subject" class="block text-sm font-medium text-neutral-700">
                                Тема обращения <span class="text-red-500">*</span>
                            </label>
                            <select id="subject" v-model="form.subject" required
                                class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20">
                                <option value="">Выберите тему</option>
                                <option value="technical">Техническая проблема</option>
                                <option value="transaction">Вопрос по сделке</option>
                                <option value="account">Проблемы с аккаунтом</option>
                                <option value="payment">Платежи и кошельки</option>
                                <option value="verification">Верификация</option>
                                <option value="other">Другое</option>
                            </select>
                        </div>

                        <!-- Сообщение -->
                        <div>
                            <label for="message" class="block text-sm font-medium text-neutral-700">
                                Сообщение <span class="text-red-500">*</span>
                            </label>
                            <textarea id="message" v-model="form.message" rows="6" required
                                class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                placeholder="Опишите вашу проблему подробнее..." />
                        </div>

                        <!-- Приоритет -->
                        <div>
                            <label class="block text-sm font-medium text-neutral-700">Приоритет</label>
                            <div class="mt-2 flex flex-wrap gap-4">
                                <label class="flex items-center gap-2">
                                    <input v-model="form.priority" type="radio" value="low"
                                        class="h-4 w-4 text-primary focus:ring-primary" />
                                    <span class="text-sm text-neutral-600">Низкий</span>
                                </label>
                                <label class="flex items-center gap-2">
                                    <input v-model="form.priority" type="radio" value="medium"
                                        class="h-4 w-4 text-primary focus:ring-primary" />
                                    <span class="text-sm text-neutral-600">Средний</span>
                                </label>
                                <label class="flex items-center gap-2">
                                    <input v-model="form.priority" type="radio" value="high"
                                        class="h-4 w-4 text-primary focus:ring-primary" />
                                    <span class="text-sm text-neutral-600">Высокий</span>
                                </label>
                                <label class="flex items-center gap-2">
                                    <input v-model="form.priority" type="radio" value="urgent"
                                        class="h-4 w-4 text-primary focus:ring-primary" />
                                    <span class="text-sm text-neutral-600">Срочно</span>
                                </label>
                            </div>
                        </div>

                        <!-- Прикрепить файл -->
                        <div>
                            <label for="file" class="block text-sm font-medium text-neutral-700">
                                Прикрепить файл (опционально)
                            </label>
                            <div class="mt-1 flex items-center gap-3">
                                <input id="file" ref="fileInput" type="file" accept="image/*,.pdf,.doc,.docx,.txt"
                                    class="hidden" @change="handleFileUpload" />
                                <button type="button" @click="fileInput?.click()"
                                    class="inline-flex items-center gap-2 rounded-xl border border-neutral-300 px-4 py-2.5 text-sm text-neutral-600 transition hover:border-primary hover:bg-primary/5 hover:text-primary">
                                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                                    </svg>
                                    Выбрать файл
                                </button>
                                <span v-if="form.fileName" class="text-sm text-neutral-600">
                                    {{ form.fileName }}
                                </span>
                            </div>
                            <p class="mt-1 text-xs text-neutral-400">
                                Поддерживаемые форматы: JPG, PNG, PDF, DOC, TXT. Максимум 5MB.
                            </p>
                        </div>

                        <!-- Отправить -->
                        <button type="submit" :disabled="isSubmitting"
                            class="flex w-full items-center justify-center gap-2 rounded-xl bg-primary px-6 py-3.5 text-sm font-semibold text-white transition hover:bg-primary/80 focus:outline-none focus:ring-2 focus:ring-primary/20 disabled:cursor-not-allowed disabled:opacity-50 sm:w-auto sm:px-8">
                            <span v-if="!isSubmitting">Отправить сообщение</span>
                            <span v-else>Отправка...</span>
                            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M14 5l7 7m0 0l-7 7m7-7H3" />
                            </svg>
                        </button>
                    </form>

                    <!-- Успешная отправка -->
                    <div v-if="isSuccess" class="mt-6 rounded-xl bg-emerald-50 p-4 text-emerald-700">
                        <div class="flex items-center gap-3">
                            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd"
                                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                    clip-rule="evenodd" />
                            </svg>
                            <span>Сообщение отправлено! Мы свяжемся с вами в ближайшее время.</span>
                        </div>
                    </div>

                    <!-- Ошибка -->
                    <div v-if="isError" class="mt-6 rounded-xl bg-red-50 p-4 text-red-700">
                        <div class="flex items-center gap-3">
                            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd"
                                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                                    clip-rule="evenodd" />
                            </svg>
                            <span>Что-то пошло не так. Попробуйте еще раз или напишите нам на email.</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
definePageMeta({
    layout: 'landing'
})

const fileInput = ref<HTMLInputElement | null>(null)
const isSubmitting = ref(false)
const isSuccess = ref(false)
const isError = ref(false)

const form = reactive({
    name: '',
    email: '',
    subject: '',
    message: '',
    priority: 'medium',
    file: null as File | null,
    fileName: ''
})

const handleFileUpload = (event: Event) => {
    const target = event.target as HTMLInputElement
    const file = target.files?.[0]

    if (file) {
        // Проверка размера (5MB)
        if (file.size > 5 * 1024 * 1024) {
            alert('Файл слишком большой. Максимум 5MB.')
            return
        }

        form.file = file
        form.fileName = file.name
    }
}

const handleSubmit = async () => {
    isSubmitting.value = true
    isSuccess.value = false
    isError.value = false

    try {
        // Здесь будет реальный API запрос
        // const formData = new FormData()
        // formData.append('name', form.name)
        // formData.append('email', form.email)
        // formData.append('subject', form.subject)
        // formData.append('message', form.message)
        // formData.append('priority', form.priority)
        // if (form.file) formData.append('file', form.file)

        // const response = await $fetch('/api/support', {
        //   method: 'POST',
        //   body: formData
        // })

        // Имитация отправки
        await new Promise(resolve => setTimeout(resolve, 1500))

        console.log('Форма отправлена:', form)

        isSuccess.value = true

        // Сброс формы через 3 секунды
        setTimeout(() => {
            Object.assign(form, {
                name: '',
                email: '',
                subject: '',
                message: '',
                priority: 'medium',
                file: null,
                fileName: ''
            })
            if (fileInput.value) {
                fileInput.value.value = ''
            }
            isSuccess.value = false
        }, 5000)

    } catch (error) {
        console.error('Ошибка отправки:', error)
        isError.value = true

        setTimeout(() => {
            isError.value = false
        }, 5000)
    } finally {
        isSubmitting.value = false
    }
}
</script>