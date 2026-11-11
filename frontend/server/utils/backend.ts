import type { H3Event } from 'h3'
import { createError, getHeader, getRequestHeaders, setResponseStatus } from 'h3'

interface BackendRequestOptions {
  method?: 'GET' | 'POST' | 'PATCH' | 'DELETE'
  body?: unknown
  query?: Record<string, string | string[]>
  forwardSession?: boolean
  successStatus?: number
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
    const response = await $fetch<T>(path, {
      baseURL: config.apiBase,
      method: options.method,
      body: options.body,
      query: options.query,
      headers,
    })

    if (options.successStatus !== undefined) {
      setResponseStatus(event, options.successStatus)
    }

    return response
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
