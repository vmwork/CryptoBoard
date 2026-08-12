<template>
    <div class="flex min-h-screen  justify-center bg-neutral-50 px-4 py-12 sm:px-6 lg:px-8">
        <div class="w-full max-w-md">
            <!-- Контейнер с флип-эффектом -->
            <div class="relative perspective-1000">
                <!-- Карточка-контейнер -->
                <div class="flip-container transition-all duration-700 ease-in-out" :class="{ 'flipped': !isLogin }">
                    <!-- Передняя сторона (Вход) -->
                    <div class="flip-card front w-full space-y-8">
                        <div class="text-center">
                            <h2 class="mt-6 text-3xl font-bold text-neutral-900">Вход</h2>
                            <p class="mt-2 text-sm text-neutral-600">Войдите в свой аккаунт</p>

                            <div v-if="userIntent"
                                class="mt-3 inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-1.5 text-sm text-primary">
                                <span>Вы выбрали роль:</span>
                                <span class="font-semibold">{{ userIntent === 'buyer' ? 'Покупатель' : 'Продавец'
                                }}</span>
                            </div>
                        </div>

                        <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
                            <div class="space-y-4">
                                <div>
                                    <label for="email-login"
                                        class="block text-sm font-medium text-neutral-700">Email</label>
                                    <input id="email-login" v-model="loginForm.email" type="email" required
                                        class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                        placeholder="example@email.com" />
                                </div>

                                <div>
                                    <label for="password-login"
                                        class="block text-sm font-medium text-neutral-700">Пароль</label>
                                    <input id="password-login" v-model="loginForm.password"
                                        :type="showPassword ? 'text' : 'password'" required
                                        class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                        placeholder="••••••••" />
                                    <button type="button" @click="showPassword = !showPassword"
                                        class="mt-1 text-sm text-neutral-500 transition hover:text-neutral-700">
                                        {{ showPassword ? 'Скрыть' : 'Показать' }}
                                    </button>
                                </div>

                                <div class="text-right">
                                    <a href="#" class="text-sm text-primary transition hover:text-primary/80">
                                        Забыли пароль?
                                    </a>
                                </div>
                            </div>

                            <button type="submit"
                                class="flex w-full items-center justify-center rounded-xl bg-primary px-4 py-3 text-sm font-semibold text-white transition hover:bg-primary/80 focus:outline-none focus:ring-2 focus:ring-primary/20">
                                Войти
                            </button>

                            <p class="text-center text-sm text-neutral-600">
                                Нет аккаунта?
                                <button type="button" @click="isLogin = false"
                                    class="font-medium text-primary transition hover:text-primary/80">
                                    Зарегистрироваться
                                </button>
                            </p>
                        </form>
                    </div>

                    <!-- Задняя сторона (Регистрация) -->
                    <div class="flip-card back w-full space-y-8">
                        <div class="text-center">
                            <h2 class="mt-6 text-3xl font-bold text-neutral-900">Создать аккаунт</h2>
                            <p class="mt-2 text-sm text-neutral-600">Начните торговать уже сегодня</p>

                            <div v-if="userIntent"
                                class="mt-3 inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-1.5 text-sm text-primary">
                                <span>Вы выбрали роль:</span>
                                <span class="font-semibold">{{ userIntent === 'buyer' ? 'Покупатель' : 'Продавец'
                                }}</span>
                            </div>
                        </div>

                        <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
                            <div class="space-y-4">
                                <div>
                                    <label for="name" class="block text-sm font-medium text-neutral-700">Имя
                                        пользователя</label>
                                    <input id="name" v-model="registerForm.name" type="text" required
                                        class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                        placeholder="Введите ваше имя" />
                                </div>

                                <div>
                                    <label for="email-register"
                                        class="block text-sm font-medium text-neutral-700">Email</label>
                                    <input id="email-register" v-model="registerForm.email" type="email" required
                                        class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                        placeholder="example@email.com" />
                                </div>

                                <div>
                                    <label for="password-register"
                                        class="block text-sm font-medium text-neutral-700">Пароль</label>
                                    <input id="password-register" v-model="registerForm.password"
                                        :type="showPassword ? 'text' : 'password'" required
                                        class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                        placeholder="••••••••" />
                                </div>

                                <div>
                                    <label for="confirm-password"
                                        class="block text-sm font-medium text-neutral-700">Подтвердите пароль</label>
                                    <input id="confirm-password" v-model="registerForm.confirmPassword"
                                        :type="showPassword ? 'text' : 'password'" required
                                        class="mt-1 block w-full rounded-xl border border-neutral-300 px-4 py-3 text-neutral-900 placeholder-neutral-400 transition focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
                                        placeholder="••••••••" />
                                </div>

                                <div class="flex items-start gap-2">
                                    <input id="terms" v-model="registerForm.agreeTerms" type="checkbox" required
                                        class="mt-1 h-4 w-4 rounded border-neutral-300 text-primary focus:ring-primary" />
                                    <label for="terms" class="text-sm text-neutral-600">
                                        Я согласен с
                                        <a href="/terms" class="text-primary hover:underline">условиями
                                            использования</a>
                                        и
                                        <a href="/privacy" class="text-primary hover:underline">политикой
                                            конфиденциальности</a>
                                    </label>
                                </div>
                            </div>

                            <button type="submit"
                                class="flex w-full items-center justify-center rounded-xl bg-primary px-4 py-3 text-sm font-semibold text-white transition hover:bg-primary/80 focus:outline-none focus:ring-2 focus:ring-primary/20">
                                Зарегистрироваться
                            </button>

                            <p class="text-center text-sm text-neutral-600">
                                Уже есть аккаунт?
                                <button type="button" @click="isLogin = true"
                                    class="font-medium text-primary transition hover:text-primary/80">
                                    Войти
                                </button>
                            </p>
                        </form>
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

const isLogin = ref(true)
const showPassword = ref(false)
const userIntent = ref<string | null>(null)

const loginForm = reactive({
    email: '',
    password: ''
})

const registerForm = reactive({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    agreeTerms: false
})

onMounted(() => {
    userIntent.value = localStorage.getItem('userIntent')
})

const handleLogin = () => {
    console.log('Логин:', loginForm)
    console.log('Выбранная роль:', userIntent.value)
    // navigateTo('/dashboard')
}

const handleRegister = () => {
    if (registerForm.password !== registerForm.confirmPassword) {
        alert('Пароли не совпадают!')
        return
    }

    if (!registerForm.agreeTerms) {
        alert('Необходимо согласиться с условиями использования')
        return
    }

    console.log('Регистрация:', registerForm)
    console.log('Выбранная роль:', userIntent.value)
    // navigateTo('/dashboard')
}
</script>

<style scoped>
.perspective-1000 {
    perspective: 1000px;
}

.flip-container {
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}

.flip-container.flipped {
    transform: rotateY(180deg);
}

.flip-card {
    position: relative;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    min-height: 400px;
}

.flip-card.front {
    z-index: 2;
}

.flip-card.back {
    position: absolute;
    top: 0;
    left: 0;
    transform: rotateY(180deg);
    z-index: 1;
}

/* Анимация для плавного появления */
.flip-card {
    transition: opacity 0.3s ease-in-out;
}

.flip-container.flipped .flip-card.front {
    opacity: 0.7;
}

.flip-container.flipped .flip-card.back {
    opacity: 1;
}

.flip-container:not(.flipped) .flip-card.back {
    opacity: 0;
}

.flip-container:not(.flipped) .flip-card.front {
    opacity: 1;
}
</style>