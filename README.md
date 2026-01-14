# AI Cosmetics Innovation Journal

A complete AI-powered journal platform for cosmetics innovation, connecting Obsidian vault → Git → Web publishing pipeline.

## 🧪 Overview

This project is a static site generator for a cosmetics innovation journal, featuring:

- **7 AI journalist personas** with distinct writing styles
- **5 content categories**: Development, Products, Ingredients, Trends, Tips
- **Full admin dashboard** for content management
- **Obsidian integration** with Claude Code skills
- **SEO-optimized** static HTML output

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/passeth/ai-diven_cos.git
cd ai-diven_cos

# Install dependencies
npm install

# Build the site
npm run build

# Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

## 📁 Project Structure

```
ai-diven_cos/
├── content/                    # Markdown articles
│   ├── development/            # AI cosmetics R&D
│   ├── products/               # Product reviews
│   ├── ingredients/            # Ingredient science
│   ├── trends/                 # Industry trends
│   └── tips/                   # Beauty tips
├── site/
│   ├── public/                 # Static assets
│   ├── src/                    # Build scripts & templates
│   ├── admin/                  # Admin dashboard
│   └── build/                  # Generated output
├── obsidian/
│   ├── .obsidian/             # Obsidian settings
│   └── skills/                # Claude Code skills
└── docs/                      # Documentation
```

## ✍️ Creating Content

### 1. Using Templates

Templates are located in `obsidian/.obsidian/templates/`:

- `template-article.md` - Standard article
- `template-product-review.md` - Product review
- `template-research.md` - Scientific article
- `template-tutorial.md` - How-to guide

### 2. YAML Frontmatter

Every article requires valid frontmatter:

```yaml
---
title: "Article Title"
slug: "url-friendly-slug"
journalist: "dr-sarah-kim"
category: "ingredients"
tags: ["tag1", "tag2"]
date: "2025-01-15"
excerpt: "Brief summary"
status: "published"
featured: false
homepage_priority: 5
reading_time: "5 min"
---
```

See [docs/YAML_SCHEMA.md](docs/YAML_SCHEMA.md) for complete schema.

### 3. Journalist Personas

Choose from 7 personas, each with a unique voice:

| Persona | Expertise | Style |
|---------|-----------|-------|
| Dr. Sarah Kim | Formulation science | Scientific yet accessible |
| Dr. James Park | Clinical research | Evidence-based |
| Dr. Emily Chen | Biotechnology | Tech-forward |
| Yuna Lee | Product reviews | Conversational |
| Alex Thompson | Market trends | Analytical |
| Min-ji Kang | Lifestyle | Elegant, mindful |
| Dr. David Rodriguez | Sustainability | Action-oriented |

See [docs/PERSONAS.md](docs/PERSONAS.md) for full details.

## 🔧 Claude Code Skills

Located in `obsidian/skills/`:

| Skill | Purpose |
|-------|---------|
| `journalist-writer.md` | Generate articles in persona voice |
| `image-generator.md` | Create article images |
| `article-publisher.md` | Validate and publish articles |
| `yaml-validator.md` | Check frontmatter validity |
| `seo-optimizer.md` | Optimize for search engines |

## 🎛️ Admin Dashboard

Access at `http://localhost:3000/admin/` to:

- Toggle article visibility (draft/published)
- Manage featured articles
- Set homepage priority order
- Preview articles before publishing

## 📦 Build Process

The build script (`site/src/build.js`) performs:

1. Scans `/content/` for markdown files
2. Parses YAML frontmatter
3. Converts Markdown → HTML via marked.js
4. Generates:
   - Homepage
   - Article pages
   - Category pages
   - Journalist pages
   - RSS feed
   - Sitemap

## 🚢 Deployment

### GitHub Pages

```bash
npm run deploy
```

### Manual

1. Run `npm run build`
2. Upload `site/build/` contents to your hosting
3. Configure domain/SSL

## 📝 Documentation

- [CLAUDE.md](docs/CLAUDE.md) - Project guidelines
- [YAML_SCHEMA.md](docs/YAML_SCHEMA.md) - Frontmatter specification
- [PERSONAS.md](docs/PERSONAS.md) - Journalist personas

## 🔗 Links

- **Repository**: https://github.com/passeth/ai-diven_cos
- **Documentation**: `/docs/`
- **Admin Dashboard**: `/admin/`

## 📄 License

MIT License - see LICENSE file for details.

---

Built with 🧪 by the AI Cosmetics Innovation team.
