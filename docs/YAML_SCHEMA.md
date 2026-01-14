# YAML Frontmatter Schema

This document defines the required YAML frontmatter schema for all markdown articles in the AI Cosmetics Journal.

## Required Fields

Every markdown article **must** have the following frontmatter:

```yaml
---
title: "Article Title"
slug: "url-friendly-slug"
journalist: "persona-id"
persona_role: "R&D Scientist"
category: "development"
tags: ["tag1", "tag2"]
date: "2025-01-15"
updated: "2025-01-15"
featured_image: "/assets/images/article-hero.jpg"
excerpt: "Brief 2-3 sentence summary for listings"
status: "published"
featured: false
homepage_priority: 5
reading_time: "5 min"
---
```

## Field Definitions

### Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Full article title (max 100 chars) |
| `slug` | string | Yes | URL-friendly identifier (lowercase, hyphens only) |
| `journalist` | string | Yes | Persona ID from PERSONAS.md |
| `persona_role` | string | Yes | Display role of the journalist |
| `category` | string | Yes | One of: development, products, ingredients, trends, tips |
| `tags` | array | Yes | 2-5 relevant tags |
| `date` | string | Yes | Publication date (YYYY-MM-DD) |
| `updated` | string | Yes | Last update date (YYYY-MM-DD) |
| `featured_image` | string | Yes | Path to hero image |
| `excerpt` | string | Yes | 150-200 character summary |
| `status` | string | Yes | One of: draft, published |
| `featured` | boolean | Yes | Show on homepage featured section |
| `homepage_priority` | number | Yes | 1-10 (1=highest priority) |
| `reading_time` | string | Yes | Estimated reading time |

## Category Values

| Category | Description | Primary Journalists |
|----------|-------------|---------------------|
| `development` | AI cosmetics R&D process, formulation development | Dr. Sarah Kim, Dr. James Park |
| `products` | Product reviews, launches, comparisons | Yuna Lee, Min-ji Kang |
| `ingredients` | Ingredient science, formulation tips | Dr. Sarah Kim, Dr. Emily Chen |
| `trends` | Industry trends, market research | Alex Thompson, Min-ji Kang |
| `tips` | Beauty tips, usage guides, tutorials | Yuna Lee, Min-ji Kang |

## Status Values

| Status | Description |
|--------|-------------|
| `draft` | Work in progress, not visible on site |
| `published` | Live and visible on the website |

## Homepage Priority

- `1` - Most important, featured prominently
- `2-3` - High priority, secondary features
- `4-6` - Medium priority, standard listings
- `7-10` - Lower priority, older content

## Tag Guidelines

### Recommended Tags by Category

**Development:**
- `ai-formulation`, `r&d`, `innovation`, `clinical-study`, `technology`

**Products:**
- `skincare`, `makeup`, `review`, `new-release`, `comparison`

**Ingredients:**
- `active-ingredients`, `natural`, `synthetic`, `safety`, `efficacy`

**Trends:**
- `market-trends`, `consumer-insights`, `k-beauty`, `sustainability`

**Tips:**
- `routine`, `how-to`, `skintype`, `seasonal`, `anti-aging`

## Example Complete Frontmatter

```yaml
---
title: "How AI is Revolutionizing Retinol Formulation"
slug: "ai-revolutionizing-retinol-formulation"
journalist: "dr-sarah-kim"
persona_role: "R&D Scientist"
category: "development"
tags: ["ai-formulation", "retinol", "innovation", "skincare"]
date: "2025-01-15"
updated: "2025-01-15"
featured_image: "/assets/images/ai-retinol-lab.jpg"
excerpt: "Discover how artificial intelligence is transforming the way we develop stable, effective retinol products. From molecular modeling to predictive stability testing."
status: "published"
featured: true
homepage_priority: 2
reading_time: "8 min"
---
```

## Validation Rules

1. **slug** must be unique across all articles
2. **journalist** must match a valid persona ID
3. **category** must be one of the five allowed values
4. **tags** array must contain 2-5 items
5. **date** and **updated** must be valid ISO dates
6. **featured_image** path must exist
7. **excerpt** must be 100-250 characters
8. **homepage_priority** must be 1-10

## File Naming Convention

Articles should be saved as:
```
content/{category}/{date}-{slug}.md
```

Example:
```
content/development/2025-01-15-ai-revolutionizing-retinol-formulation.md
```
