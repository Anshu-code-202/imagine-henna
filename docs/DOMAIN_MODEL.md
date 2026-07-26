# Imagine Henna – Domain Model

**Version:** 1.0  
**Status:** Approved  
**Owner:** Anshu Arora  
**Sprint:** Sprint 0

---
# Domain Overview

Imagine Henna is a decision-support platform that helps customers confidently choose mehendi designs before meeting an artist. The domain revolves around the Mehendi Design, which is classified by Occasion, Style, and Coverage, and is accessed through search, filtering, favorites, and recommendation sessions.

---

# 1. Purpose

This document defines the core business concepts of **Imagine Henna**. It establishes a shared vocabulary for the product and engineering teams before database schema, APIs, or implementation are designed.

The domain model focuses on **business meaning** rather than technical implementation.

---

# 2. Core Actors

These are the people who interact with the system.

| Actor | Description |
|--------|-------------|
| **Customer** | Primary MVP user who discovers and chooses mehendi designs. |
| **Administrator** | Manages the design catalog and platform. |
| **Artist (Future)** | Uploads and manages designs in future versions. |

---

# 3. Core Business Entities

## 3.1 Mehendi Design

### Description

The primary business entity representing a mehendi design available on the platform.

### Responsibilities

- Represent a mehendi design.
- Belong to one occasion.
- Belong to one style.
- Belong to one coverage.
- Appear in one or more collections.
- Be searchable.
- Be recommendable.

---

## 3.2 Occasion

### Examples

- Wedding
- Engagement
- Baby Shower
- Karva Chauth
- Teej
- Diwali
- Eid
- Anniversary

### Purpose

Represents the event for which a mehendi design is suitable.

---

## 3.3 Style

### Examples

- Arabic
- Traditional
- Minimal
- Indo-Arabic
- Mandala
- Gulf

### Purpose

Represents the artistic style of a mehendi design.

---

## 3.4 Coverage

### Examples

- Fingers
- Front Hand
- Back Hand
- Half Hand
- Full Hand
- Half Arm
- Full Arm

### Purpose

Represents the area of the hand or arm covered by the design.

---

## 3.5 Collection

### Examples

- Bridal Collection
- Festival Collection
- Trending Designs

### Purpose

Organizes related mehendi designs into curated groups for easier browsing.

---

## 3.6 Favorite

### Purpose

Allows customers to save mehendi designs for future comparison and decision-making.

---

## 3.7 Preference Profile

### Purpose

Represents a customer's preferences, such as preferred occasion, style, and coverage, to support personalization and future recommendations.

---

## 3.8 Recommendation Session

### Purpose

Represents a single recommendation request generated based on the customer's preferences and search filters.

> **Note:** Recommendation Sessions are generated dynamically and are **not permanently stored** in the MVP.

---

## 3.9 Try-On Session (Future)

### Purpose

Represents one virtual try-on request where a selected mehendi design is visualized on the customer's uploaded hand image.

---

# 4. Relationships

The following relationships describe how the core business concepts interact.

```text
Customer
│
├── saves ─────────────► Favorite
│
└── starts ────────────► Recommendation Session
                           │
                           ▼
                    Mehendi Design
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Occasion            Style             Coverage
                           │
                           ▼
                      Collection
```

---

# 5. Business Rules

## Customer

- A customer can save multiple favorite designs.
- A customer cannot save the same design more than once.
- A customer can perform multiple recommendation sessions.

---

## Mehendi Design

- Must belong to exactly one Occasion.
- Must belong to exactly one Style.
- Must belong to exactly one Coverage.
- May belong to one or more Collections.

---

## Favorite

- Must reference exactly one Customer.
- Must reference exactly one Mehendi Design.
- Duplicate favorites are not allowed.

---

## Recommendation Session

- Generated dynamically.
- Based on user preferences and selected filters.
- Results may change over time.
- Not permanently stored in the MVP.

---

## Collection

- Can contain multiple Mehendi Designs.
- Used only for organization and browsing.

---

# 6. Ubiquitous Language

The following terms have a single agreed meaning throughout the project.

| Term | Meaning |
|------|---------|
| **Design** | A mehendi design available in the catalog. |
| **Collection** | A curated group of related designs. |
| **Occasion** | The event for which the design is intended. |
| **Style** | The artistic category of the design. |
| **Coverage** | The area of the hand or arm covered by the design. |
| **Favorite** | A design saved by a customer. |
| **Recommendation Session** | One recommendation request generated for a customer. |

---

# 7. Future Domain Evolution

The following business concepts are intentionally excluded from the MVP and may be introduced in future versions.

- Artist Portfolio
- Artist Upload Portal
- Booking Management
- Reviews & Ratings
- Online Payments
- Chat with Artists
- Notifications

---

# 8. Summary

The **Mehendi Design** is the central business entity of Imagine Henna.

Every major feature—including search, filtering, favorites, recommendations, and future virtual try-on—depends on the Design Catalog.

This domain model serves as the foundation for future database design, API design, and implementation while remaining independent of any specific technology or programming language.