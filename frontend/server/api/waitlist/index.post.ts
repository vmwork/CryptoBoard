export default defineEventHandler(async (event) =>
  proxyToBackend(event, '/api/v1/waitlist', {
    method: 'POST',
    body: await readBody(event),
    forwardSession: true,
    successStatus: 201,
  }),
)
