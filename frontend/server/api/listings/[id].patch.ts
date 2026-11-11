export default defineEventHandler(async (event) =>
  proxyToBackend(event, `/api/v1/listings/${getRouterParam(event, 'id')}`, {
    method: 'PATCH',
    body: await readBody(event),
    forwardSession: true,
  }),
)
