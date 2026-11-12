import { readBody } from 'h3'
import { proxyToBackend } from '../../utils/backend'

export default defineEventHandler(async (event) => {
  const body = await readBody(event)

  return await proxyToBackend(event, '/api/v1/auth/link-wallet', {
    method: 'POST',
    body,
    forwardSession: true,
  })
})
