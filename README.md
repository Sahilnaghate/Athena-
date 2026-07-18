# ATHENA

ATHENA is an enterprise platform foundation. Sprint 001 contains only the platform skeleton; it intentionally contains no market, scanner, or AI logic.

## Prerequisites

- Docker Desktop with Docker Compose
- Node.js 22 and pnpm 9 (for local frontend development)
- Python 3.12 (for local API development)

## Run the platform

```bash
cp .env.example .env
docker compose up --build
```

Services:

- Web: http://localhost:3000
- API health: http://localhost:8000/health
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## Local workspace commands

```bash
pnpm install
pnpm lint
pnpm test
pnpm build
```

## Structure

- `apps/`: deployable API, web, worker, and admin applications
- `packages/`: shared platform contracts and reusable modules
- `infrastructure/`: infrastructure documentation and future definitions
- `docs/`: architecture and sprint documentation
