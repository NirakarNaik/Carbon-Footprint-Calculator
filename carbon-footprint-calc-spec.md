# Project Brief: Carbon Footprint Calculator v2 (Rebuild)

## Context
This is a rebuild of an existing NLP-based carbon footprint calculator (originally built ~2 years ago). The original flow: user answers input questions → app calculates a carbon footprint score → app shows a recommendations page with ways to reduce the footprint.

This rebuild keeps that core flow but modernizes both frontend and backend, with two hard constraints below.

## Hard Constraints (non-negotiable)
- **No accounts, no login, no signup.** The tool must be usable anonymously, start to finish.
- **No database.** No persistent storage of user data, no user table, no server-side history. Any state needed during a session should live in memory on the server (if at all) or in the browser (session-only, cleared on refresh/tab close is fine — do NOT use this to reintroduce persistence via localStorage as a workaround for "no DB").
- If any feature seems to require persistence (e.g. "save my results," "compare over time"), it should be solved client-side (e.g. a downloadable/shareable result, a PDF export, a shareable URL with encoded answers) — not a database.

## Goals
1. Rebuild the calculator so it's faster, cleaner, and easier to maintain.
2. Rebuild the frontend with a genuinely distinctive visual identity — see "Design direction" below. This is a firm requirement, not a nice-to-have.
3. Rebuild/clean the backend: keep the NLP-driven input parsing (users can describe things in natural language, not just dropdowns) and the recommendation engine, but make the code modular, testable, and easy to extend with new emission factors or new recommendation rules.

## Design direction — avoid "AI slop" aesthetics
The single biggest ask for this project: the frontend must NOT look like a generic AI-generated SaaS landing page. Explicitly avoid:
- Warm cream background + high-contrast serif headline + terracotta/clay accent color combo
- Near-black background with one neon/acid-green or vermilion accent
- Identical rounded "SaaS cards" with the same soft grey box-shadow on everything
- Tracked-out ALL-CAPS eyebrow labels above headings, meta text joined by middle dots ("A · B · C"), arrows tacked onto every button/link ("Learn more →"), monospace font used just for "flair" on labels
- Generic hero pattern: big number + small label + gradient wash

Instead:
- Ground the visual language in the actual subject matter — carbon, emissions, climate, resource use. Think in terms of physical/tangible metaphors: weight, scale, breath, cycles, seasons, material intensity — rather than generic tech/startup visual language. Pick ONE concrete metaphor and commit to it rather than sprinkling several.
- Pick a deliberate, specific color palette (name 4–6 actual hex values) and one or two typefaces used with intention — not defaults reached for on any project.
- The results/recommendations page is the emotional core of the product — it should feel like a considered, specific artifact, not a stat-card dashboard. Treat the user's footprint number as something worth designing around, not just displaying.
- Motion should be used sparingly: one well-orchestrated moment (e.g. how the result reveals itself) rather than fade-in-on-scroll everywhere.
- Fully responsive, keyboard accessible, respects prefers-reduced-motion.
- Write real, specific copy for every screen (questions, empty states, result explanations, recommendation text) in a plain, direct voice — no filler, no marketing tone.

Deliverable expectation: before writing code, produce a short design plan (color tokens, type choices, layout concept with a quick ASCII wireframe, and 2-3 guiding principles specific to this product) and sanity-check it isn't a generic default before building.

## Core User Flow
1. **Landing** — brief framing of what the tool does and why (no login prompt, no gated content).
2. **Input** — user answers a set of questions about their lifestyle (transport, home energy, diet, consumption habits, travel, etc.). Support natural-language free-text input where reasonable (e.g. "I drive about 40km a day and mostly eat vegetarian") in addition to/instead of rigid form fields, parsed via NLP on the backend.
3. **Calculation** — backend computes an estimated carbon footprint (e.g. in kg CO2e/year) from parsed inputs using emission factor data.
4. **Results** — show the footprint number with context (e.g. comparison to national/global average, breakdown by category: transport, home, food, consumption).
5. **Recommendations** — personalized, prioritized list of actions to reduce footprint, tied to the user's specific inputs (e.g. if transport is the biggest category, lead with transport recommendations).
6. **Optional: export/share** — let the user download their result (e.g. as an image or PDF) or get a shareable link that re-encodes their inputs in the URL (no server storage) so they can revisit or share without an account.

## Backend Requirements
- Stateless API — each request is self-contained (input in, result out). No session persisted server-side beyond the life of a single request.
- Keep/rebuild the NLP layer that extracts structured data (distances, frequencies, diet type, energy usage, etc.) from free-text input. Fall back gracefully to structured form inputs if NLP parsing is ambiguous or fails — ask a clarifying question rather than guessing silently.
- Emission factor data (transport, energy, diet, goods) should live in clearly organized config/data files, not hardcoded inline, so factors can be updated without touching logic.
- Recommendation engine should be rule-based and transparent (e.g. a mapping of footprint-driver → ranked recommendations), not a black box, and easy to extend with new rules.
- Modular structure: separate input parsing, calculation, and recommendation logic into distinct modules/services.
- Include basic input validation and sensible error handling (e.g. nonsensical numbers, empty input).

## Frontend Requirements
- No auth UI of any kind.
- Single-page flow or lightweight multi-step flow (client-side routing is fine); no need for a persistent backend session.
- Support both structured inputs (sliders, selects, number fields) and a free-text/natural-language input mode — let the user pick whichever feels natural per question, or offer one unified free-text entry point per section.
- Results and recommendations page should be shareable/exportable as described above without needing a database.
- Should work well on mobile.

## Non-Goals (explicitly out of scope)
- User accounts, authentication, or profiles
- Any persistent database (SQL, NoSQL, or otherwise)
- Server-side storage of user history or analytics tied to individuals
- Admin dashboards / multi-user features

## Suggested Tech Stack (flexible — adjust if you have a better fit)
- Frontend: React or vanilla JS/HTML/CSS, whichever keeps the design intent easiest to execute; avoid heavy UI kit defaults (e.g. out-of-the-box Bootstrap/Material look) since that fights the design goal above.
- Backend: Lightweight API (e.g. FastAPI/Flask/Express) — stateless, no ORM/DB layer needed.
- NLP: Reuse a lightweight approach appropriate to the original project's scale (e.g. spaCy/regex-and-rules hybrid, or a small LLM call for parsing) — keep it fast and avoid unnecessary heavy dependencies.
- Emission factor data: JSON/YAML config files bundled with the backend.

## Deliverables
1. Short design plan (palette, type, layout concept, guiding principles) before build.
2. Rebuilt frontend implementing the flow above with the distinctive design direction.
3. Rebuilt backend: NLP input parsing, calculation engine, recommendation engine — modular and documented.
4. Brief README covering setup/run instructions and how to update emission factors or recommendation rules.
