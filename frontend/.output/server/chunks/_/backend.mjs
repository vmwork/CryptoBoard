import { u as useRuntimeConfig, c as getHeader, e as getRequestHeaders, f as setResponseStatus, h as createError } from '../nitro/nitro.mjs';

async function proxyToBackend(event, path, options = {}) {
  var _a;
  const config = useRuntimeConfig(event);
  const headers = {
    "X-Internal-Bff-Secret": config.internalBffSecret
  };
  const acceptLanguage = getHeader(event, "accept-language");
  if (acceptLanguage) {
    headers["Accept-Language"] = acceptLanguage;
  }
  if (options.forwardSession) {
    const sessionCookie = (_a = getRequestHeaders(event).cookie) == null ? void 0 : _a.split(";").map((cookie) => cookie.trim()).find((cookie) => cookie.startsWith(`${config.sessionCookieName}=`));
    if (sessionCookie) {
      headers.Cookie = sessionCookie;
    }
  }
  try {
    const response = await $fetch(path, {
      baseURL: config.apiBase,
      method: options.method,
      body: options.body,
      query: options.query,
      headers
    });
    if (options.successStatus !== void 0) {
      setResponseStatus(event, options.successStatus);
    }
    return response;
  } catch (error) {
    const fetchError = error;
    throw createError({
      statusCode: fetchError.statusCode || 502,
      statusMessage: fetchError.statusMessage || "Backend request failed",
      data: fetchError.data
    });
  }
}

export { proxyToBackend as p };
//# sourceMappingURL=backend.mjs.map
