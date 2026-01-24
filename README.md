# Obsidian Zero-Cost CMS Template

**[한국어 README](README.ko.md)**

A complete **zero-cost CMS** connecting Obsidian → GitHub → Vercel. Write in Markdown, deploy automatically.

> **[Live Demo](https://ai-diven-cos.vercel.app)** | **[Sample Article](https://ai-diven-cos.vercel.app/articles/niacinamide-complete-guide.html)**

---

## 🚀 Getting Started (Use This Template)

### Step 1: Create Your Repository

Click the green **"Use this template"** button above, then select **"Create a new repository"**.

- Enter your repository name (e.g., `my-blog`)
- Choose public or private
- Click **"Create repository"**

### Step 2: Clone Your New Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 3: Install & Run

```bash
# Install dependencies
npm install

# Run interactive setup (optional)
python setup.py

# Start development server
npm run dev
```

### Step 4: Deploy to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Deploy (auto-configured)

**Done!** Your site is now live with automatic deployments on every push.

---

## What You Can Build

Use this template to create blogs, journals, documentation sites, or any content-driven website:

- Write content in **Obsidian** (offline, Markdown)
- Push to **GitHub** with one click
- Auto-deploy to **Vercel** (free hosting, SSL, CDN)
- **$0/month** infrastructure cost

## 💡 Zero-Cost CMS Architecture

This project demonstrates a modern **serverless CMS** that costs $0/month to operate.

```
┌─────────────────────────────────────────────────────────────┐
│                      WORKFLOW                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Obsidian            Claude Code           Vercel           │
│   ┌─────────┐         ┌───────────┐        ┌─────────┐      │
│   │ Write   │         │  Build    │        │ Deploy  │      │
│   │ Edit    │ ──────▶ │  Automate │ ─────▶ │ Host    │      │
│   │ Images  │ GitHub  │  Enhance  │  Auto  │ SSL     │      │
│   └─────────┘  Sync   └───────────┘        └─────────┘      │
│       ▲                                                      │
│       │ Obsidian Plugins                                     │
│       ├─ Obsidian Git (auto backup & sync)                   │
│       ├─ Paste Image Rename (auto image naming)              │
│       ├─ Templater (article templates)                       │
│       └─ Linter (YAML formatting)                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why This Stack?

| Feature | Traditional CMS | This System |
|---------|-----------------|-------------|
| Hosting Cost | $10~50/month | **Free** (Vercel) |
| Database | MySQL/PostgreSQL | **Git** (free, versioned) |
| Backup | Manual setup | **Automatic** (Git history) |
| Editor | Web-based only | **Obsidian** (offline capable) |
| Version Control | Limited or none | **Full Git history** |
| Deployment | Manual/complex | **Push = Auto deploy** |
| AI Integration | None | **Claude Code built-in** |
| Admin Panel | Separate system | **Obsidian IS the admin** |

### Key Benefits

- **Obsidian as Admin Panel**: Write, edit, and manage content locally with full Markdown support
- **GitHub as Database**: Free storage, automatic versioning, collaboration-ready
- **Vercel as Host**: Automatic SSL, CDN, zero-config deployment
- **Claude Code as Developer**: Build features, fix bugs, generate content on demand

## 🧪 Overview

This project is a static site generator for a cosmetics innovation journal, featuring:

- **7 AI journalist personas** with distinct writing styles
- **5 content categories**: Development, Products, Ingredients, Trends, Tips
- **Full admin dashboard** for content management
- **Obsidian integration** with Claude Code skills
- **SEO-optimized** static HTML output

## 🛠️ Prerequisites

- Python 3.8+
- Node.js 18+
- Git
- [Obsidian](https://obsidian.md/)

## ⚙️ Configuration

The `setup.py` script will configure:
- Site name & description
- Content categories
- Obsidian plugin settings

For manual setup, see **[SETUP.md](SETUP.md)**.

## 📁 Project Structure

```
ai-diven_cos/                   # Root = Obsidian Vault
├── content/                    # Markdown articles
│   ├── development/            # AI cosmetics R&D
│   ├── products/               # Product reviews
│   ├── ingredients/            # Ingredient science
│   ├── trends/                 # Industry trends
│   ├── tips/                   # Beauty tips
│   ├── videos/                 # YouTube embeds + notes
│   └── _assets/images/         # Article images
├── site/
│   ├── public/                 # Static assets (CSS, JS)
│   ├── src/                    # Build scripts & templates
│   └── build/                  # Generated output (deploy this)
├── .obsidian/                  # Obsidian settings & plugins
├── .claude/skills/             # Claude Code skills
├── docs/                       # Documentation
├── Home.md                     # Obsidian homepage
└── CLAUDE.md                   # Project guidelines for Claude
```

## ✍️ Creating Content

### 1. Using Templates

Templates are located in `.obsidian/templates/`:

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

Located in `.claude/skills/`:

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

### Vercel (Recommended)

This project is configured for **automatic Vercel deployment**:

1. Push to GitHub → Vercel builds automatically
2. Preview deployments for every branch
3. Production deployment on `master` branch

### From Obsidian (One-Click)

With **Obsidian Git** plugin installed:
1. `Cmd+P` → `Obsidian Git: Create backup`
2. Done! Vercel deploys automatically

Or wait for auto backup (runs every 10 minutes)

### Manual

1. Run `npm run build`
2. Upload `site/build/` contents to your hosting
3. Configure domain/SSL

## 🔌 Recommended Obsidian Plugins

| Plugin | Purpose |
|--------|---------|
| **Obsidian Git** | Auto backup & sync to GitHub |
| **Paste Image Rename** | Auto-name images: `{filename}_{date}_{n}.png` |
| **Templater** | Article templates with dynamic fields |
| **Linter** | Auto-format YAML frontmatter |
| **Homepage** | Set a default note on vault open |

### Plugin Setup Tips

- **Obsidian Git**: See Git Push Management section below
- **Paste Image Rename**: Pattern: `{{fileName}}_{{DATE:YYYYMMDD}}_{{NNNNN}}`
- **Images folder**: `content/_assets/images/`

## 🔄 Git Push Management

This project uses **Obsidian Git** plugin for automatic backup and GitHub sync.

### Default Settings

| Setting | Value | Description |
|---------|-------|-------------|
| **Auto backup interval** | 10 min | Auto commit + push every 10 minutes |
| **Auto pull on startup** | ✅ ON | Pull latest changes when Obsidian opens |
| **Push on backup** | ✅ ON | Auto push on backup |
| **Pull before push** | ✅ ON | Pull before push to prevent conflicts |
| **Auto backup after file change** | ✅ ON | Push immediately when file is saved |

### Auto-Push Behavior

By default, this template is configured for **instant push on save**:

- Create/edit a note → Save → Auto push to GitHub → Vercel deploys

If you prefer **interval-based backup** (less commits):

1. Open `.obsidian/plugins/obsidian-git/data.json`
2. Set `"autoBackupAfterFileChange": false`
3. Restart Obsidian

With this setting, backups happen every 10 minutes instead of on every save.

### Commands (Cmd+P / Ctrl+P)

| Command | Description |
|---------|-------------|
| `Obsidian Git: Create backup` | Instant commit + push (most used) |
| `Obsidian Git: Commit all changes` | Commit changes only |
| `Obsidian Git: Push` | Push to remote |
| `Obsidian Git: Pull` | Pull from remote |

### Commit Message Format

```
vault backup: 2026-01-16 22:07:32
```

### Status Bar

- Check Git status in Obsidian's bottom status bar
- ✓ = Synced
- Number = Changed files count

### Manual Push (Terminal)

```bash
cd "your-project-folder"
git add .
git commit -m "your message"
git push
```

### Plugin Settings Sync

Plugin settings (`data.json`) are included in Git for easy sharing:
- Settings auto-apply when cloned
- Changes sync with your pushes

## 📝 Documentation

- [CLAUDE.md](CLAUDE.md) - Project guidelines for Claude Code
- [WORKFLOW.md](docs/WORKFLOW.md) - Content creation workflow
- [YAML_SCHEMA.md](docs/YAML_SCHEMA.md) - Frontmatter specification
- [PERSONAS.md](docs/PERSONAS.md) - Journalist personas

## 🔗 Links

- **Live Demo**: https://ai-diven-cos.vercel.app
- **Sample Article**: https://ai-diven-cos.vercel.app/articles/niacinamide-complete-guide.html
- **Repository**: https://github.com/passeth/ai-diven_cos
- **Quick Setup Guide**: [SETUP.md](SETUP.md)

## 📄 License

MIT License - see LICENSE file for details.

---

Built with Obsidian + Claude Code + Vercel | Zero infrastructure cost
