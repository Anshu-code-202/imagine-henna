# ADR-001: Modular Monolith Architecture

## Status

Accepted

---

## Context

Imagine Henna is an MVP being developed by a single engineer.

The primary goals are:

- Deliver value quickly
- Maintain a clean codebase
- Keep deployment simple
- Support future growth

At this stage, the system has a limited number of business modules such as:

- Authentication
- Design Catalog
- Search
- Favorites
- Recommendation

---

## Decision

We will implement Imagine Henna as a Modular Monolith.

Each business capability will be implemented as an independent module inside one FastAPI application.

Modules communicate through internal interfaces rather than network calls.

---

## Alternatives Considered

### Traditional Monolith

Simple but risks becoming tightly coupled as the project grows.

### Microservices

Provides strong service isolation but introduces unnecessary operational complexity for a single-developer MVP.

---

## Consequences

### Positive

- Easier to develop and debug
- Simple deployment
- Clear module boundaries
- Supports future extraction into microservices if required

### Negative

- All modules share one deployment
- Requires discipline to avoid tight coupling

---

## Decision Rationale

This decision aligns with the Imagine Henna Engineering OS principles:

- Product before Technology
- Simplicity before Scale
- Measure Before Optimizing
- Build for Explainability