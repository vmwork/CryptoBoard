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

const stats_get = defineEventHandler(
  (event) => proxyToBackend(event, "/api/v1/waitlist/stats")
);

export { stats_get as default };
//# sourceMappingURL=stats.get.mjs.map
