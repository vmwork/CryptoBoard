import { d as defineEventHandler, b as getQuery } from '../../nitro/nitro.mjs';
import { p as proxyToBackend } from '../../_/backend.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'node:crypto';
import 'node:url';

const index_get = defineEventHandler((event) => {
  const query = getQuery(event);
  const forwardedQuery = {};
  for (const key of [
    "category",
    "condition",
    "min_price",
    "max_price",
    "page",
    "page_size"
  ]) {
    const value = query[key];
    if (typeof value === "string" || Array.isArray(value)) {
      forwardedQuery[key] = value;
    }
  }
  return proxyToBackend(event, "/api/v1/listings", {
    query: forwardedQuery
  });
});

export { index_get as default };
//# sourceMappingURL=index.get.mjs.map
