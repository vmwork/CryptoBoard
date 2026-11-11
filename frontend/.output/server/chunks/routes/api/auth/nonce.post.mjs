import { d as defineEventHandler, r as readBody } from '../../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const nonce_post = defineEventHandler(async (event) => {
  const body = await readBody(event);
  return await proxyToBackend(event, "/api/v1/auth/nonce", {
    method: "POST",
    body
  });
});

export { nonce_post as default };
//# sourceMappingURL=nonce.post.mjs.map
