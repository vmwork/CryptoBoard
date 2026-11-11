export default defineEventHandler((event) => {
  const query = getQuery(event)
  const forwardedQuery: Record<string, string | string[]> = {}

  for (const key of [
    'category',
    'condition',
    'min_price',
    'max_price',
    'page',
    'page_size',
  ]) {
    const value = query[key]
    if (typeof value === 'string' || Array.isArray(value)) {
      forwardedQuery[key] = value
    }
  }

  return proxyToBackend(event, '/api/v1/listings', {
    query: forwardedQuery,
  })
})
