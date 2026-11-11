import type { H3Event } from 'h3'
import { createError, getHeader, getRequestHeaders } from 'h3'

interface BackendRequestOptions {
  method?: 'GET' | 'POST'
  body?: unknown
  forwardSession?: boolean
}

export async function proxyToBackend<T>(
  event: H3Event,
  path: string,
  options: BackendRequestOptions = {},
): Promise<T> {
  const config = useRuntimeConfig(event)
  const headers: Record<string, string> = {
    'X-Internal-Bff-Secret': config.internalBffSecret,
  }
  const acceptLanguage = getHeader(event, 'accept-language')

  if (acceptLanguage) {
    headers['Accept-Language'] = acceptLanguage
  }

  if (options.forwardSession) {
    const sessionCookie = getRequestHeaders(event).cookie
      ?.split(';')
      .map((cookie) => cookie.trim())
      .find((cookie) => cookie.startsWith(`${config.sessionCookieName}=`))

    if (sessionCookie) {
      headers.Cookie = sessionCookie
    }
  }

  try {
    return await $fetch<T>(path, {
      baseURL: config.apiBase,
      method: options.method,
      body: options.body,
      headers,
    })
  } catch (error: unknown) {
    const fetchError = error as {
      statusCode?: number
      statusMessage?: string
      data?: unknown
    }

    throw createError({
      statusCode: fetchError.statusCode || 502,
      statusMessage: fetchError.statusMessage || 'Backend request failed',
      data: fetchError.data,
    })
  }
}
