#!/usr/bin/env python3
"""
Obsidian + GitHub + Vercel CMS Setup Script
============================================
Interactive setup script to configure your zero-cost CMS.

Requirements:
- Python 3.8+
- Git installed
- Node.js 18+ installed

Usage:
    python setup.py
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path


# ANSI Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 50}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}  {text}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 50}{Colors.END}\n")


def print_step(text):
    print(f"{Colors.CYAN}>> {text}{Colors.END}")


def print_success(text):
    print(f"{Colors.GREEN}[OK] {text}{Colors.END}")


def print_error(text):
    print(f"{Colors.RED}[ERROR] {text}{Colors.END}")


def print_warning(text):
    print(f"{Colors.YELLOW}[!] {text}{Colors.END}")


def ask(prompt, default=None, required=True):
    """Ask user for input with optional default value."""
    if default:
        prompt_text = f"{Colors.BOLD}{prompt}{Colors.END} [{Colors.CYAN}{default}{Colors.END}]: "
    else:
        prompt_text = f"{Colors.BOLD}{prompt}{Colors.END}: "
    
    while True:
        answer = input(prompt_text).strip()
        if not answer and default:
            return default
        if answer or not required:
            return answer
        print_warning("This field is required.")


def ask_yes_no(prompt, default=True):
    """Ask yes/no question."""
    default_str = "Y/n" if default else "y/N"
    prompt_text = f"{Colors.BOLD}{prompt}{Colors.END} [{Colors.CYAN}{default_str}{Colors.END}]: "
    answer = input(prompt_text).strip().lower()
    
    if not answer:
        return default
    return answer in ('y', 'yes', 'true', '1')


def check_prerequisites():
    """Check if required tools are installed."""
    print_header("Checking Prerequisites")
    
    # Check Git
    print_step("Checking Git installation...")
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        print_success(f"Git found: {result.stdout.strip()}")
    except FileNotFoundError:
        print_error("Git is not installed. Please install Git first.")
        print("  Download: https://git-scm.com/downloads")
        sys.exit(1)
    
    # Check Node.js
    print_step("Checking Node.js installation...")
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        version = result.stdout.strip()
        print_success(f"Node.js found: {version}")
        
        # Check version >= 18
        major_version = int(version.lstrip('v').split('.')[0])
        if major_version < 18:
            print_warning(f"Node.js 18+ recommended. You have {version}")
    except FileNotFoundError:
        print_error("Node.js is not installed. Please install Node.js 18+ first.")
        print("  Download: https://nodejs.org/")
        sys.exit(1)
    
    # Check npm
    print_step("Checking npm installation...")
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        print_success(f"npm found: v{result.stdout.strip()}")
    except FileNotFoundError:
        print_error("npm is not installed.")
        sys.exit(1)
    
    print()


def get_user_config():
    """Interactive configuration gathering."""
    print_header("Project Configuration")
    
    config = {}
    
    # Basic Info
    print(f"{Colors.BOLD}--- Basic Information ---{Colors.END}\n")
    
    config['site_name'] = ask("Site Name", "My Obsidian Blog")
    config['site_description'] = ask("Site Description", "A zero-cost CMS powered by Obsidian")
    config['author'] = ask("Author Name", os.environ.get('USER', os.environ.get('USERNAME', 'author')))
    
    # GitHub Info
    print(f"\n{Colors.BOLD}--- GitHub Configuration ---{Colors.END}\n")
    
    config['github_username'] = ask("GitHub Username")
    config['github_repo'] = ask("GitHub Repository Name", config['site_name'].lower().replace(' ', '-'))
    config['github_branch'] = ask("Default Branch", "main")
    
    # Site URL (for Vercel or custom domain)
    default_url = f"https://{config['github_repo']}.vercel.app"
    config['site_url'] = ask("Site URL (Vercel or custom domain)", default_url)
    
    # Categories
    print(f"\n{Colors.BOLD}--- Content Categories ---{Colors.END}\n")
    print("Default categories: posts, tutorials, notes")
    print("Enter custom categories (comma-separated) or press Enter for defaults")
    
    categories_input = ask("Categories", "posts, tutorials, notes", required=False)
    config['categories'] = [c.strip() for c in categories_input.split(',')]
    
    # Personas (optional)
    print(f"\n{Colors.BOLD}--- Author Personas ---{Colors.END}\n")
    config['use_personas'] = ask_yes_no("Use multiple author personas?", default=False)
    
    if config['use_personas']:
        print("\nYou can customize personas later in site/src/build.js")
    
    # Obsidian Plugins
    print(f"\n{Colors.BOLD}--- Obsidian Plugins ---{Colors.END}\n")
    config['setup_plugins'] = ask_yes_no("Configure recommended Obsidian plugins?", default=True)
    
    return config


def update_package_json(config, project_dir):
    """Update package.json with user config."""
    package_path = project_dir / 'package.json'
    
    with open(package_path, 'r', encoding='utf-8') as f:
        package = json.load(f)
    
    package['name'] = config['github_repo']
    package['description'] = config['site_description']
    package['author'] = config['author']
    
    # Update repository field
    package['repository'] = {
        'type': 'git',
        'url': f"https://github.com/{config['github_username']}/{config['github_repo']}.git"
    }
    
    with open(package_path, 'w', encoding='utf-8') as f:
        json.dump(package, f, indent=2)
    
    print_success("Updated package.json")


def update_build_js(config, project_dir):
    """Update build.js configuration."""
    build_path = project_dir / 'site' / 'src' / 'build.js'
    
    with open(build_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update site URL
    content = re.sub(
        r"siteUrl: process\.env\.SITE_URL \|\| '[^']*'",
        f"siteUrl: process.env.SITE_URL || '{config['site_url']}'",
        content
    )
    
    # Update site name
    content = re.sub(
        r"siteName: '[^']*'",
        f"siteName: '{config['site_name']}'",
        content
    )
    
    # Update categories
    categories_js = "{\n"
    colors = ['#6366f1', '#ec4899', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444']
    for i, cat in enumerate(config['categories']):
        slug = cat.lower().replace(' ', '-')
        name = cat.title()
        color = colors[i % len(colors)]
        categories_js += f"  {slug}: {{ name: '{name}', description: 'Articles about {cat}', color: '{color}' }},\n"
    categories_js += "}"
    
    content = re.sub(
        r"const CATEGORIES = \{[^}]+\};",
        f"const CATEGORIES = {categories_js};",
        content,
        flags=re.DOTALL
    )
    
    # If not using personas, simplify to single author
    if not config['use_personas']:
        simple_persona = f"""const PERSONAS = {{
  'author': {{
    name: '{config['author']}',
    role: 'Author',
    avatar: '/assets/personas/default.svg',
    bio: '{config['site_description']}'
  }}
}};"""
        content = re.sub(
            r"const PERSONAS = \{[\s\S]*?\n\};",
            simple_persona,
            content
        )
    
    with open(build_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print_success("Updated build.js")


def setup_obsidian_plugins(config, project_dir):
    """Configure Obsidian plugin settings."""
    if not config['setup_plugins']:
        return
    
    obsidian_dir = project_dir / '.obsidian'
    plugins_dir = obsidian_dir / 'plugins'
    
    # Ensure directories exist
    obsidian_dir.mkdir(exist_ok=True)
    plugins_dir.mkdir(exist_ok=True)
    
    # GitHub Sync plugin settings
    github_sync_dir = plugins_dir / 'github-sync'
    github_sync_dir.mkdir(exist_ok=True)
    
    github_sync_config = {
        "gitPath": "",
        "remoteUrl": f"https://github.com/{config['github_username']}/{config['github_repo']}.git",
        "syncOnStartup": False,
        "showRibbonIcon": True
    }
    
    with open(github_sync_dir / 'data.json', 'w', encoding='utf-8') as f:
        json.dump(github_sync_config, f, indent=2)
    
    # Paste Image Rename plugin settings
    paste_image_dir = plugins_dir / 'obsidian-paste-image-rename'
    paste_image_dir.mkdir(exist_ok=True)
    
    paste_image_config = {
        "imageNamePattern": "{{fileName}}_{{DATE:YYYYMMDD}}_{{NNNNN}}",
        "dupNumberAtStart": False,
        "dupNumberDelimiter": "_",
        "autoRename": True,
        "handleAllAttachments": False
    }
    
    with open(paste_image_dir / 'data.json', 'w', encoding='utf-8') as f:
        json.dump(paste_image_config, f, indent=2)
    
    # Update community plugins list
    community_plugins = [
        "github-sync",
        "obsidian-paste-image-rename",
        "templater-obsidian",
        "obsidian-linter"
    ]
    
    with open(obsidian_dir / 'community-plugins.json', 'w', encoding='utf-8') as f:
        json.dump(community_plugins, f, indent=2)
    
    # Update app.json for attachment settings
    app_config = {
        "attachmentFolderPath": "content/_assets/images",
        "showUnsupportedFiles": False,
        "userIgnoreFilters": ["site/", "node_modules/", ".git/"]
    }
    
    with open(obsidian_dir / 'app.json', 'w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=2)
    
    print_success("Configured Obsidian plugin settings")


def setup_content_folders(config, project_dir):
    """Create content category folders."""
    content_dir = project_dir / 'content'
    
    # Create category folders
    for category in config['categories']:
        slug = category.lower().replace(' ', '-')
        cat_dir = content_dir / slug
        cat_dir.mkdir(parents=True, exist_ok=True)
        
        # Create sample post
        sample_post = f"""---
title: "Welcome to {category.title()}"
slug: "welcome-to-{slug}"
journalist: "author"
category: "{slug}"
tags: ["welcome", "sample"]
date: "{get_today_date()}"
excerpt: "This is a sample post in the {category} category."
status: "published"
featured: false
reading_time: "2 min"
---

# Welcome to {category.title()}!

This is a sample post. You can delete this and start writing your own content.

## How to Write

1. Create a new `.md` file in this folder
2. Add the YAML frontmatter at the top
3. Write your content in Markdown
4. Set `status: "published"` when ready

Happy writing!
"""
        
        sample_path = cat_dir / f"welcome-to-{slug}.md"
        if not sample_path.exists():
            with open(sample_path, 'w', encoding='utf-8') as f:
                f.write(sample_post)
    
    # Create _assets/images folder
    assets_dir = content_dir / '_assets' / 'images'
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    print_success(f"Created content folders: {', '.join(config['categories'])}")


def get_today_date():
    """Get today's date in YYYY-MM-DD format."""
    from datetime import date
    return date.today().isoformat()


def update_readme(config, project_dir):
    """Update README with project-specific info."""
    readme_path = project_dir / 'README.md'
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update title
    content = re.sub(
        r"# AI Cosmetics Innovation Journal",
        f"# {config['site_name']}",
        content
    )
    
    # Update repository URL
    content = re.sub(
        r"https://github\.com/passeth/ai-diven_cos",
        f"https://github.com/{config['github_username']}/{config['github_repo']}",
        content,
        flags=re.IGNORECASE
    )
    
    # Update clone command
    content = re.sub(
        r"git clone https://github\.com/passeth/ai-diven_cos\.git",
        f"git clone https://github.com/{config['github_username']}/{config['github_repo']}.git",
        content
    )
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print_success("Updated README.md")


def init_git_repo(config, project_dir):
    """Initialize Git repository."""
    print_step("Initializing Git repository...")
    
    # Check if already a git repo
    git_dir = project_dir / '.git'
    if git_dir.exists():
        print_warning("Git repository already exists. Skipping init.")
    else:
        subprocess.run(['git', 'init'], cwd=project_dir, capture_output=True)
        print_success("Git repository initialized")
    
    # Set remote
    remote_url = f"https://github.com/{config['github_username']}/{config['github_repo']}.git"
    
    # Check existing remote
    result = subprocess.run(
        ['git', 'remote', 'get-url', 'origin'],
        cwd=project_dir,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        # Remote exists, update it
        subprocess.run(
            ['git', 'remote', 'set-url', 'origin', remote_url],
            cwd=project_dir,
            capture_output=True
        )
        print_success(f"Updated remote origin: {remote_url}")
    else:
        # Add new remote
        subprocess.run(
            ['git', 'remote', 'add', 'origin', remote_url],
            cwd=project_dir,
            capture_output=True
        )
        print_success(f"Added remote origin: {remote_url}")


def run_npm_install(project_dir):
    """Run npm install."""
    print_step("Installing npm dependencies...")
    
    result = subprocess.run(
        ['npm', 'install'],
        cwd=project_dir,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print_success("npm dependencies installed")
    else:
        print_warning("npm install had some issues. You may need to run it manually.")
        print(result.stderr[:500] if result.stderr else "")


def clean_sample_content(project_dir):
    """Remove sample cosmetics content."""
    content_dir = project_dir / 'content'
    
    # Remove cosmetics-specific folders if they exist
    cosmetics_folders = ['development', 'products', 'ingredients', 'trends', 'tips', 'videos']
    
    for folder in cosmetics_folders:
        folder_path = content_dir / folder
        if folder_path.exists():
            import shutil
            shutil.rmtree(folder_path)
    
    print_success("Cleaned sample content")


def print_next_steps(config):
    """Print next steps for the user."""
    print_header("Setup Complete!")
    
    print(f"{Colors.GREEN}Your Obsidian CMS is ready!{Colors.END}\n")
    
    print(f"{Colors.BOLD}Next Steps:{Colors.END}\n")
    
    print("1. Create GitHub Repository:")
    print(f"   Go to: https://github.com/new")
    print(f"   Name: {config['github_repo']}")
    print()
    
    print("2. Open in Obsidian:")
    print(f"   Open this folder as an Obsidian vault")
    print()
    
    print("3. Install Obsidian Plugins:")
    print("   Settings > Community Plugins > Browse")
    print("   - GitHub Sync")
    print("   - Paste Image Rename")
    print("   - Templater")
    print("   - Linter")
    print()
    
    print("4. Connect to Vercel:")
    print("   Go to: https://vercel.com/new")
    print("   Import your GitHub repository")
    print()
    
    print("5. Start Writing!")
    print(f"   Create .md files in content/{config['categories'][0]}/")
    print()
    
    print(f"{Colors.BOLD}Commands:{Colors.END}")
    print(f"  npm run dev    - Start local dev server")
    print(f"  npm run build  - Build static site")
    print()
    
    print(f"{Colors.CYAN}Happy blogging! {Colors.END}")


def main():
    """Main setup function."""
    print_header("Obsidian + GitHub + Vercel CMS Setup")
    
    print("This script will configure your zero-cost CMS.")
    print("You can change settings later in the config files.\n")
    
    # Get project directory
    project_dir = Path(__file__).parent.absolute()
    print(f"Project directory: {project_dir}\n")
    
    # Check prerequisites
    check_prerequisites()
    
    # Get user configuration
    config = get_user_config()
    
    # Confirm
    print_header("Configuration Summary")
    print(f"  Site Name:     {config['site_name']}")
    print(f"  GitHub User:   {config['github_username']}")
    print(f"  Repository:    {config['github_repo']}")
    print(f"  Site URL:      {config['site_url']}")
    print(f"  Categories:    {', '.join(config['categories'])}")
    print(f"  Use Personas:  {'Yes' if config['use_personas'] else 'No'}")
    print()
    
    if not ask_yes_no("Proceed with this configuration?", default=True):
        print("\nSetup cancelled.")
        sys.exit(0)
    
    # Apply configuration
    print_header("Applying Configuration")
    
    # Clean sample content first
    if ask_yes_no("Remove sample cosmetics content?", default=True):
        clean_sample_content(project_dir)
    
    # Update files
    update_package_json(config, project_dir)
    update_build_js(config, project_dir)
    update_readme(config, project_dir)
    setup_content_folders(config, project_dir)
    setup_obsidian_plugins(config, project_dir)
    
    # Git setup
    init_git_repo(config, project_dir)
    
    # npm install
    if ask_yes_no("Run npm install?", default=True):
        run_npm_install(project_dir)
    
    # Print next steps
    print_next_steps(config)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(0)
