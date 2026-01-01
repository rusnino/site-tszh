# Repository Guidelines

## Project Structure & Module Organization
This repository currently contains no tracked source files. When adding code, keep a clear, top-level layout such as:

- `src/` for application code.
- `tests/` or `__tests__/` for automated tests.
- `public/` or `assets/` for static files.
- `docs/` for design notes and operational docs.

If you introduce a framework, mirror its conventional structure (e.g., `src/components/`, `src/pages/`). Update this guide as soon as the structure becomes concrete.

## Build, Test, and Development Commands
No build or test tooling is defined yet. Once tooling is added, document the exact commands here. Examples to add (as applicable):

- `npm run dev` — start the local development server.
- `npm test` — run the test suite.
- `npm run build` — create a production build.

## Coding Style & Naming Conventions
No formatting or linting configuration is present yet. When you add tooling, document it here and keep it enforced in CI. Suggested defaults:

- Indentation: 2 spaces for JS/TS, 4 spaces for Python.
- Filenames: `kebab-case` for folders, `PascalCase` for React components, `camelCase` for variables/functions.
- Formatting: Prettier or equivalent; linting via ESLint or a language-appropriate linter.

## Testing Guidelines
No testing framework is configured. When tests are added, specify:

- Framework (e.g., Jest, Vitest, pytest).
- Naming pattern (e.g., `*.test.ts`, `*.spec.js`).
- Coverage expectations, if any (e.g., focus on core logic and critical paths).

## Commit & Pull Request Guidelines
There is no commit history to infer conventions from. Until conventions are established:

- Commit messages should be short, imperative, and scoped (e.g., `add homepage layout`).
- Pull requests should include a concise description, testing notes, and screenshots for UI changes.
- Link relevant issues or tickets when applicable.

## Security & Configuration Tips
Store secrets outside the repository (use `.env` files and keep them out of version control). If you add deployment or CI config, document required environment variables and safe defaults here.
