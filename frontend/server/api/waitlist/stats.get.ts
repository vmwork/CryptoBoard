export default defineEventHandler((event) =>
  proxyToBackend(event, '/api/v1/waitlist/stats'),
)
