import { proxyToBackend } from '../../utils/backend'

export default defineEventHandler(async (event) => {
  return await proxyToBackend(event, '/api/v1/auth/me', {
    forwardSession: true,
  })
})
