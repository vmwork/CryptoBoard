import { deleteCookie } from 'h3'
import { proxyToBackend } from '../../utils/backend'

export default defineEventHandler(async (event) => {
  const response = await proxyToBackend(event, '/api/v1/auth/logout', {
    method: 'POST',
    forwardSession: true,
  })
  const config = useRuntimeConfig(event)

  deleteCookie(event, config.sessionCookieName, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    path: '/',
  })

  return response
})
