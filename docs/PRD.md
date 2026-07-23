# Product requirements Document (PRD)

## Document Information


| Field | Value |
|------|------|
| Project Name | Imagine Henna |
| Product Title | Imagine Henna – AI-powered Mehendi Discovery, Recommendation & Visualization Platform |
| Version | 1.0 |
| Status | Draft |
| Author | Anshu Arora |
| Reviewer | Engineering Manager |
| Created On | 23 July 2026 |
| Last Updated | 23 July 2026 |


---

## Document Purpose

This Product Requirements Document (PRD) defines the product vision, requirements, scope, constraints, success metrics, and engineering decisions for Imagine Henna.

It serves as the primary reference for product managers, software engineers, AI engineers, and future contributors during the development of the project.

---

## Related Documents

- PRODUCT_STRATEGY.md
- ARCHITECTURE.md
- DOMAIN_MODEL.md
- DATABASE.md
- API_SPEC.md
- TEST_PLAN.md
- DEPLOYMENT.md
- ADR-001 – Modular Monolith
- ADR-002 – Design Catalog Strategy

---

# Executive Summary

## Overview

Imagine Henna is an AI-powered Mehendi Discovery, Recommendation, and Visualization platform designed to help users confidently choose the right mehendi design before visiting a mehendi artist.

The product addresses a common problem faced by customers who spend significant time browsing social media platforms, searching through artist portfolios, and comparing hundreds of designs without confidence that a chosen design matches their occasion, preferences, or expectations.

Version 1 (MVP) focuses on helping brides preparing for their wedding discover suitable mehendi designs through structured search, filtering, rich design information, and explainable AI-powered recommendations.

Rather than replacing professional mehendi artists, Imagine Henna assists customers in making informed decisions before their appointment, reducing uncertainty and improving communication between customers and artists.

## Product Vision

Our long-term vision is to build the leading digital platform for mehendi discovery and decision support across weddings, festivals, cultural celebrations, and other special occasions.

While the initial release targets brides as the beachhead market, the platform is designed to expand into an occasion-based ecosystem supporting customers, professional artists, and future intelligent services such as virtual try-on, artist portfolio management, and personalized recommendations.

## Target Audience

### Primary Audience

Brides preparing for their wedding who need help selecting an appropriate mehendi design confidently and efficiently.

### Future Audiences

- Festival customers
- Professional mehendi artists
- Event-based customers
- Families assisting in design selection

## Product Value Proposition

Imagine Henna helps users confidently discover and choose mehendi designs that match their occasion, style, and preferences before visiting a mehendi artist, reducing hours of browsing and uncertainty through structured discovery and explainable recommendations.

## MVP Goal

The objective of Version 1 is to validate that curated design discovery, intelligent search, metadata-driven filtering, and explainable AI recommendations significantly improve the user's design selection experience without introducing unnecessary engineering complexity.

---

# Problem Statement

## Background

Choosing a mehendi design is an important decision for many customers, especially brides preparing for their wedding. A selected design reflects personal style, complements the occasion, and often becomes a memorable part of the celebration.

Despite the large number of mehendi designs available online, customers frequently experience difficulty finding a design that matches their preferences and requirements.

## Current User Workflow

Today, a typical customer follows a fragmented process:

1. Search Pinterest, Instagram, Google Images, or YouTube.
2. Browse hundreds of mehendi images.
3. Save screenshots across multiple platforms.
4. Ask friends and family for opinions.
5. Visit one or more mehendi artists.
6. Browse physical albums or WhatsApp galleries.
7. Compare multiple designs again.
8. Remain uncertain before making a final decision.

This process is repetitive, time-consuming, and often results in decision fatigue.

## Pain Points

The current workflow creates several problems:

- Customers spend hours searching across multiple platforms.
- Many designs lack structured information such as style, occasion, or coverage.
- Customers struggle to determine whether a design matches their personal preferences.
- It is difficult to compare similar designs objectively.
- Customers cannot easily visualize how a design may suit their own hands.
- Communication between customers and artists is often inefficient because preferences are not clearly defined before the appointment.

## Existing Alternatives

Customers currently rely on:

- Social media platforms (Pinterest, Instagram, Facebook)
- Google Image Search
- WhatsApp image collections shared by artists
- Physical design albums maintained by artists
- Recommendations from friends and family

While these sources provide inspiration, they are not designed to support confident decision-making.

## Problem Definition

The core problem is not the lack of mehendi designs.

The core problem is that customers lack an efficient and trustworthy way to discover, compare, and confidently choose a mehendi design that matches their occasion, preferences, and expectations before visiting an artist.

## Why This Problem Matters

For customers:

- Significant time is spent searching instead of deciding.
- Decision uncertainty creates unnecessary stress before important events.
- Customers may arrive at appointments without a clear design choice.

For artists:

- Time is spent repeatedly showing large collections of designs.
- Customers frequently change their preferences during consultations.
- Repeated discussions increase consultation time and reduce efficiency.

Solving this problem improves the experience for both customers and artists while enabling better communication before the mehendi application begins.

---

# User Personas

## Primary Persona – Bride Preparing for Her Wedding

### Overview

The primary user of Imagine Henna Version 1 is a bride preparing for her wedding who wants to confidently choose a mehendi design before visiting a mehendi artist.

### Goals

- Find a mehendi design suitable for her wedding.
- Reduce time spent browsing multiple platforms.
- Compare different design options.
- Understand design characteristics before making a decision.
- Feel confident about her final choice.

### Pain Points

- Too many designs spread across different platforms.
- Difficulty finding designs matching her preferences.
- Uncertainty about whether a design is the right choice.
- Difficulty communicating preferences to the artist.

### Success Criteria

A successful experience means the bride selects and saves a design she feels confident about before her appointment.

---

## Secondary Personas (Future Versions)

### Festival Customer

A customer looking for mehendi designs for occasions such as Karva Chauth, Diwali, Teej, Eid, or family celebrations.

This persona is outside the MVP but is part of the long-term product vision.

---

### Professional Mehendi Artist

A professional artist who wants to organize designs, showcase a portfolio, and eventually receive better-informed customers.

Artist-focused features are intentionally excluded from Version 1 and planned for future releases.