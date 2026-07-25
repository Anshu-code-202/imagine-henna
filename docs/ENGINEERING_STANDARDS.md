# Engineering Standards

## Git Workflow

- main → stable releases
- develop → integration branch
- feature/* → new features

---

## Commit Convention

docs:
feat:
fix:
refactor:
test:
chore:

Example:

feat: implement design catalog search
docs: add architecture overview

---

## Branch Naming

feature/search
feature/recommendation
fix/login-validation
docs/prd-update

---

## Code Style

- Meaningful variable names
- Small functions
- Single Responsibility Principle
- Type hints where applicable
- Clear comments only when necessary

---

## Documentation Rules

Every major feature must update:

- PRD (if product changes)
- Architecture (if system changes)
- ADR (if architectural decision changes)

---

## Testing

Every business module should include:

- Unit tests
- Integration tests where appropriate

---

## Definition of Done

A feature is complete only when:

- Code works
- Tests pass
- Documentation updated
- Code reviewed