import { d as defineEventHandler } from '../../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const me_get = defineEventHandler(async (event) => {
  return await proxyToBackend(event, "/api/v1/auth/me", {
    forwardSession: true
  });
});

export { me_get as default };
//# sourceMappingURL=me.get.mjs.map
