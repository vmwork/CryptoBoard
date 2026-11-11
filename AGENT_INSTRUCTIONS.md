# Classifyd: Agent System Instructions

## Project Overview & Domain Rules
* **Product:** **Classifyd** — a non-custodial Web3 P2P marketplace (crypto classifieds) for buying and selling physical goods (MVP focus: PC hardware, GPUs, RAM, CPUs, mining gear, and flagship smartphones) using **USDT** via escrow smart contracts and minting **NFT Deal Certificates** (digital receipts/provenance passports).
* **Legal & Non-Custodial Model:** The platform acts strictly as a software provider and decentralized notary. The platform NEVER holds user funds (non-custodial), requires NO KYC/email/passwords, and locks funds exclusively inside autonomous EVM smart contracts until delivery confirmation.
* **MVP Scope & Fake Door Teasers:** Active MVP categories are PC hardware & smartphones. Future features ("Verified Source Code Marketplace", "Pro Market Analytics", "Auto-Repricer", and "New Token Voting") MUST be implemented as UI teasers (`Coming Soon` / `Pro`) connected to a `feature_waitlist` / `token_votes` counter.

## Architecture & Tech Stack
* **Backend:** Python 3.12, FastAPI, Pydantic v2, synchronous SQLAlchemy 2.x, PostgreSQL 15, Alembic. Configuration loaded via `python-dotenv`.
* **Frontend:** Nuxt 4, Vue 3, TypeScript, Nitro SSR, Pinia, VueUse, Tailwind CSS, `@nuxtjs/i18n`. Form handling relies on installed `vee-validate` and `Zod`.
* **Web3 / Smart Contracts:** Solidity (OpenZeppelin: `IERC20`, `ERC721`, `ReentrancyGuard`, `Ownable`) targeting low-fee EVM chains (Arbitrum / Polygon / Base). Frontend wallet connection via `wagmi` / `viem` / Reown AppKit (WalletConnect) with future Telegram Mini App (`initData` + TON Connect) extensibility.
* **Cache & Rate Limiting:** Dragonfly (Redis protocol), client via `redis` / `fastapi-limiter`.
* **Backend Directory Layout:** `backend/app/api/v1/endpoints/` (HTTP endpoints), `backend/app/api/v1/router.py` (v1 router registration), `backend/app/services/` (business logic), `backend/app/schemas/` (Pydantic schemas), `backend/app/models/` (SQLAlchemy models), `backend/app/core/` (global config), `backend/app/db/` (database connection and sessions), `contracts/` (Solidity smart contracts & tests).
* **Frontend Directory Layout:** Application UI/logic in `frontend/app`; server-side Nitro API handlers in `frontend/server/api`; Markdown knowledge base in `frontend/content/guides`.

## Networking & Service Interoperability
* **Production Routing:** External HTTP(S) traffic is terminated by Caddy on ports 80 and 443. Backend, Nuxt, PostgreSQL, and Dragonfly do NOT publish ports to the host; `expose` keeps services internal to the Docker network. Never expose internal database or backend ports externally.
* **BFF Pattern & Route Obfuscation:** Browser requests client API via `/api/...`. Requests are processed by Nitro BFF in `frontend/server/api/***`; BFF calls FastAPI via internal address `NUXT_API_BASE` (`http://classifyd_api:8000` in production) using internal `/api/v1/...` namespaces (e.g., `/api/v1/hi/common/...`) and passes `X-Internal-Bff-Secret` header.
* **BFF Responsibility:** Acts as the frontend/backend boundary. Strips internal/sensitive fields, passes auth credentials (`httpOnly` session cookie) and locale headers, adapts request/response payloads. Core business rules MUST remain in the backend.
* **Dual-Path useApi:** Browser requests go to `/api/...` via BFF. During SSR, composables may query `NUXT_API_BASE` directly over the internal Docker network. Preserve this behavior for SSR, auth, and routing integrity.
* **Upload Routes:** Caddy proxies `/api/uploads/**` directly to backend (stripping `/api`). Nuxt also maintains a Nitro handler for `/api/uploads/***`.
* **API URLs:** Use relative/public config for client calls; use private `NUXT_API_BASE` for server-side calls to FastAPI. Never route SSR to the public website URL or use `localhost` for container-to-container communication.
* **Compose Files:** `docker-compose.yml` (production), `docker-compose.dev.yml` (staging/dev), `docker-compose.local.yml` (local overrides). Do not mix configurations. Host port exposure is only permitted in local overrides.

## Backend & API Guidelines
* **Database Model:** Maintain the synchronous SQLAlchemy session pattern. Do not introduce a secondary ORM or asynchronous paradigm without explicit architecture alignment.
* **Separation of Concerns:** Endpoints validate input and delegate to services; services handle business logic; ORM models represent storage; Pydantic schemas enforce API contracts.
* **Routing:** Attach endpoints from `backend/app/api/v1/endpoints/` in `backend/app/api/v1/router.py`. Preserve `/api/v1` versioning and response structures.
* **Data Validation:** Use Pydantic schemas for request validation and response serialization. Never return raw ORM models or leak wallet nonces, secrets, or internal fields.
* **Error Handling:** Return expected errors using `HTTPException` with proper HTTP status codes. Do not mask unexpected failures with broad `except` blocks or fake success responses. Log errors according to project standards without exposing sensitive data.
* **Transactions:** Explicitly commit or rollback transactions and close sessions via the `get_db` dependency.
* **Authentication (SIWE Stateful Sessions — No JWT in Client Storage):**
  * Users authenticate exclusively via **Sign-In with Ethereum (SIWE)** wallet signatures.
  * Nitro BFF generates a short-lived `nonce` stored in Dragonfly, verifies the cryptographic signature, creates a stateful `session_id` in Dragonfly (with TTL), and sets an `httpOnly; Secure; SameSite=Strict` cookie (`auth_token` / `session_id`). Do NOT use email/password auth or store tokens in `localStorage`.
* **Tiered Limits & Anti-Bot Rules (Business Logic in `backend/app/services`):**
  * **Free Tier:** Up to **3 active listings** for free. If a connected wallet has `0` historical on-chain transactions (verified via RPC and cached in Dragonfly), free slots are blocked and a Seller Passport is required immediately.
  * **Seller Passport Tier (\$1 one-time):** Minting a Soulbound NFT Seller Passport for **1 USDT** unlocks up to **10 active listings**, bypasses new-account pre-moderation, and splits payment 50/50 on-chain (**0.50 USDT** to `referrer`, **0.50 USDT** to platform treasury).
  * **Business / Pro Tier (11+ listings):** Subscription teaser / waitlist for MVP.
* **External Listing Import & Media Pipeline:**
  * User-initiated JSON import from external classifieds (e.g., OLX) is fetched via isolated **Cloudflare Workers** to protect server IPs and avoid CORS.
  * Upon saving a listing, `backend/app/services` downloads images to local/S3/R2 storage, strips all **EXIF metadata** (privacy protection), optionally removes corner competitor watermarks via OpenCV `inpaint`, applies the branded **Classifyd** watermark (with listing ID & Escrow badge), and converts to **WebP**.

## Database & Migrations
* **Source of Truth:** SQLAlchemy models in `backend/app/models` and Alembic migrations in `backend/alembic/versions`.
* **Identifiers:** Primary keys MUST use **UUID v7**. Never expose sequential integer IDs in public URLs or API responses. Preserve foreign keys, constraints, enums, and cascade rules.
* **Localization:** Use the existing `MultilingualText` type for localized fields.
* **Schema Modifications:** Every schema change requires a new Alembic migration. Never edit applied migrations or rely on `create_all`.
* **Migration Safety:** Test both upgrade and downgrade paths for data compatibility. Align seed data and execution with `backend/deploy.sh`.

## Frontend, SEO & Nitro BFF
* **Structure:** Nuxt 4 layout with UI/composables in `frontend/app` and server API routes in `frontend/server/api`.
* **UI Architecture (Two Layouts):**
  * `default` layout: Explanatory Landing (`/`) with interactive JSON import input, comparison table, and `/guides` knowledge base; Public Marketplace (`/market`, `/market/[id]`) with dense hardware filters, FurMark/3DMark test links, serial numbers, and Escrow checkout.
  * `crm` layout: Dark-mode SaaS/ERP Dashboard (`/dashboard`) with left sidebar, bulk-action Data Grids for listings, Escrow deal status pipeline, NFT certificate gallery, and Pro/Waitlist teasers.
* **Data Fetching:** Components, pages, and stores MUST call frontend API via relative `/api/...` BFF routes. Never invoke FastAPI directly from client-side code.
* **Synchronized Endpoints:** New browser-facing endpoints must be implemented end-to-end: backend endpoint/schema/service + thin Nitro proxy handler forwarding to `/api/v1/...`.
* **SSR & AI Search Optimization (SEO):**
  * Public pages (`/`, `/market`, `/market/[id]`) MUST render via SSR.
  * Every `/market/[id]` page MUST inject valid **Schema.org JSON-LD** (`Product` + `Offer` with `priceCurrency: "USD"`, `UsedCondition`/`NewCondition`, and `FAQPage` blocks). Never use hidden/cloaked text.
  * Seller contact details MUST NOT be rendered in initial SSR HTML; fetch them via a dedicated protected BFF endpoint after Cloudflare Turnstile verification and wallet authentication.
* **HTTP Clients:** Reuse `useApi` and standard Nuxt `$fetch` / `useFetch` patterns. Do not add Axios or secondary HTTP libraries.
* **SSR Safety:** Preserve auth tokens and `Accept-Language` headers. Do not reference `window`, `document`, or browser storage during SSR execution.
• Localization: Interface strings MUST be localized for uk and en in frontend/i18n/locales. Maintain existing routes, middleware, and dashboard access control.
• TypeScript: Strict typing required. Avoid any. Follow .prettierrc and ESLint rules.

Smart Contracts (Solidity)

• Standards & Whitelist: Use OpenZeppelin (IERC20, ERC721, ReentrancyGuard, Ownable). Support a dynamic token whitelist mapping(address => bool) public allowedTokens (initialized with USDT; expandable via community polls).
• Core Functions:
	• createDeal / confirmDelivery / refund: Non-custodial USDT escrow with a inspection timelock (e.g., 24h post-delivery) that releases funds to the seller and automatically mints an NFT Deal Certificate storing transaction hash, listing UUID, and hardware serial number.
	• buySellerPassport(address referrer): Accepts 1 USDT, mints a non-transferable (Soulbound) Seller Passport NFT, and splits funds 50/50 between referrer and platform treasury.

Configuration & Secrets

• Environment Variables: Verify real usage in code before introducing new variables. Key backend vars: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB, SECRET_KEY, INTERNAL_BFF_SECRET, REDIS_URL, EVM_RPC_URL, ESCROW_CONTRACT_ADDRESS, CF_WORKER_IMPORT_URL.
• Nuxt Runtime Config: Uses NUXT_API_BASE, NUXT_PUBLIC_API_BASE, NUXT_PUBLIC_WALLETCONNECT_PROJECT_ID, and SITE_URL. Keep internal server addresses isolated from public configurations.
• Secrets Management: Never hardcode credentials, tokens, or private keys in code, tests, logs, or docs. Keep real .env files out of Git tracking. Keep .env.example safe with placeholder values.
• Environment Isolation: Use separate database instances for production, staging, and local testing. Never run tests or seeds against shared or production databases.

Docker, Deployment & CI/CD

• Runtime: Backend runs on Python 3.12; Frontend builds on Node.js 22. Maintain alignment across Dockerfile, Compose, Caddyfile, and Nuxt runtime config.
• Deployment Flow: backend/deploy.sh applies migrations before launching app services. Respect healthcheck ordering for PostgreSQL and Dragonfly.
• CI/CD: Managed via GitHub Actions on main and develop branches.
• Testing & Quality: Backend tests run via pytest (backend/pytest.ini) against an isolated test database. Enforce Python linter rules via Black and Flake8 (setup.cfg / .pre-commit-config.yaml). Frontend code must pass npm ESLint and Prettier checks.
