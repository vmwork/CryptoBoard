import { d as defineEventHandler, u as useRuntimeConfig, a as deleteCookie } from '../../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const logout_post = defineEventHandler(async (event) => {
  const response = await proxyToBackend(event, "/api/v1/auth/logout", {
    method: "POST",
    forwardSession: true
  });
  const config = useRuntimeConfig(event);
  deleteCookie(event, config.sessionCookieName, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    path: "/"
  });
  return response;
});

export { logout_post as default };
//# sourceMappingURL=logout.post.mjs.map
