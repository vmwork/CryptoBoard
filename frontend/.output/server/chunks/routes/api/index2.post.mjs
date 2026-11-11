import { d as defineEventHandler, r as readBody } from '../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const index_post = defineEventHandler(
  async (event) => proxyToBackend(event, "/api/v1/waitlist", {
    method: "POST",
    body: await readBody(event),
    forwardSession: true,
    successStatus: 201
  })
);

export { index_post as default };
//# sourceMappingURL=index2.post.mjs.map
