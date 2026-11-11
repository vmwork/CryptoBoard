import { d as defineEventHandler, r as readBody, u as useRuntimeConfig, s as setCookie } from '../../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const verify_post = defineEventHandler(async (event) => {
  const body = await readBody(event);
  const response = await proxyToBackend(
    event,
    "/api/v1/auth/verify",
    { method: "POST", body }
  );
  const config = useRuntimeConfig(event);
  setCookie(event, config.sessionCookieName, response.session_id, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    path: "/",
    maxAge: response.expires_in
  });
  return { user: response.user, expires_in: response.expires_in };
});

export { verify_post as default };
//# sourceMappingURL=verify.post.mjs.map
