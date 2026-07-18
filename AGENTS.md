# ATHENA Repository Guidance

## Scope

Sprint 001 is platform-only. Preserve the modular application and package boundaries.

## Validation

Run `pnpm lint`, `pnpm test`, and `pnpm build` for workspace changes. For API changes, run `pytest` in `apps/api`. Use `docker compose up --build` for full-stack validation when Docker is available.
