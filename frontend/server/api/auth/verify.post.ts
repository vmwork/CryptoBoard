import { readBody, setCookie } from 'h3'
import { proxyToBackend } from '../../utils/backend'

interface InternalVerifyResponse {
  user: unknown
  expires_in: number
  session_id: string
}

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const response = await proxyToBackend<InternalVerifyResponse>(
    event,
    '/api/v1/auth/verify',
    { method: 'POST', body },
  )
  const config = useRuntimeConfig(event)

  setCookie(event, config.sessionCookieName, response.session_id, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    path: '/',
    maxAge: response.expires_in,
  })

  return { user: response.user, expires_in: response.expires_in }
})
