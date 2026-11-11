import { d as defineEventHandler, g as getRouterParam } from '../../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const _id__get = defineEventHandler(
  (event) => proxyToBackend(event, `/api/v1/listings/${getRouterParam(event, "id")}`)
);

export { _id__get as default };
//# sourceMappingURL=_id_.get.mjs.map
