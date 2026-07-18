# ATHENA Project Rules

- Keep deployable services in `apps/` and shared code in `packages/`.
- Keep domain logic out of platform packages.
- Do not introduce market, scanner, or AI capabilities without an approved milestone.
- Protect environment values: commit only `.env.example`, never local secrets.
- Every service dependency must have an observable health or readiness strategy.
