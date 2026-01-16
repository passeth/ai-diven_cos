# Quick Setup Guide

Get your **Zero-Cost CMS** running in 5 minutes.

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Node.js 18+](https://nodejs.org/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Obsidian](https://obsidian.md/)
- [GitHub Account](https://github.com/)

## Installation

### Step 1: Clone & Setup

```bash
# Clone this template
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git my-blog
cd my-blog

# Run interactive setup
python setup.py
```

The setup script will ask you:
- Site name & description
- GitHub username & repo name
- Content categories
- Plugin preferences

### Step 2: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Create a new repository with the name you specified
3. **Don't** initialize with README (we already have one)

### Step 3: Push to GitHub

```bash
git add .
git commit -m "Initial setup"
git push -u origin main
```

### Step 4: Deploy to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Deploy! (default settings work fine)

### Step 5: Open in Obsidian

1. Open Obsidian
2. "Open folder as vault"
3. Select your project folder

### Step 6: Install Obsidian Plugins

Go to **Settings > Community Plugins > Browse** and install:

| Plugin | Purpose |
|--------|---------|
| **GitHub Sync** | One-click push to GitHub |
| **Paste Image Rename** | Auto-name pasted images |
| **Templater** | Article templates |
| **Linter** | Auto-format YAML |

## Usage

### Writing Content

1. Create a new `.md` file in `content/[category]/`
2. Add frontmatter at the top:

```yaml
---
title: "My First Post"
slug: "my-first-post"
journalist: "author"
category: "posts"
tags: ["hello", "first"]
date: "2025-01-16"
excerpt: "A short summary"
status: "published"
reading_time: "3 min"
---

# My First Post

Content goes here...
```

3. Set `status: "published"` when ready

### Publishing

**From Obsidian:**
Click the GitHub Sync icon in the ribbon

**From Terminal:**
```bash
git add . && git commit -m "New post" && git push
```

Vercel will auto-deploy in ~30 seconds.

### Local Preview

```bash
npm run dev
```
Open http://localhost:3000

## Folder Structure

```
my-blog/
├── content/           # Your articles (Markdown)
│   ├── posts/
│   ├── tutorials/
│   └── _assets/images/
├── site/
│   ├── src/           # Build scripts
│   ├── public/        # Static assets
│   └── build/         # Generated HTML
├── .obsidian/         # Obsidian settings
└── setup.py           # This setup script
```

## Troubleshooting

### "Permission denied" on Git push
- Check if the repository exists on GitHub
- Verify your GitHub authentication

### Images not showing
- Place images in `content/_assets/images/`
- Use Paste Image Rename plugin for auto-naming

### Build errors
```bash
npm run build
```
Check the error output for details.

## Next Steps

- [ ] Customize `site/src/build.js` for your needs
- [ ] Add your logo to `site/public/assets/`
- [ ] Set up a custom domain in Vercel
- [ ] Write your first post!

---

**Cost: $0/month** | Built with Obsidian + GitHub + Vercel
