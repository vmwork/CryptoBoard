import { d as defineEventHandler, r as readBody, g as getRouterParam } from '../../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const _id__patch = defineEventHandler(
  async (event) => proxyToBackend(event, `/api/v1/listings/${getRouterParam(event, "id")}`, {
    method: "PATCH",
    body: await readBody(event),
    forwardSession: true
  })
);

export { _id__patch as default };
//# sourceMappingURL=_id_.patch.mjs.map
