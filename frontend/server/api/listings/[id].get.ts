export default defineEventHandler((event) =>
  proxyToBackend(event, `/api/v1/listings/${getRouterParam(event, 'id')}`),
)
