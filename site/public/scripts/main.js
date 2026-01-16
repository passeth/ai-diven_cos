/**
 * AI Cosmetics Journal - Main JavaScript
 */

(function() {
  'use strict';

  // Mobile Menu Toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const siteNav = document.querySelector('.site-nav');
  
  if (menuToggle && siteNav) {
    menuToggle.addEventListener('click', function() {
      siteNav.classList.toggle('active');
      menuToggle.setAttribute('aria-expanded', 
        siteNav.classList.contains('active') ? 'true' : 'false'
      );
    });
  }

  // Copy Link Button
  const copyButtons = document.querySelectorAll('.share-btn--copy');
  
  copyButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      const url = this.dataset.url || window.location.href;
      
      navigator.clipboard.writeText(url).then(function() {
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        btn.style.background = '#10b981';
        
        setTimeout(function() {
          btn.textContent = originalText;
          btn.style.background = '';
        }, 2000);
      }).catch(function(err) {
        console.error('Failed to copy:', err);
      });
    });
  });

  // Lazy Loading Images
  if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');
    
    const imageObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.classList.add('loaded');
          imageObserver.unobserve(img);
        }
      });
    });
    
    lazyImages.forEach(function(img) {
      imageObserver.observe(img);
    });
  }

  // Newsletter Form (placeholder handler)
  const newsletterForm = document.querySelector('.newsletter-form');
  
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const emailInput = this.querySelector('input[type="email"]');
      const submitBtn = this.querySelector('button[type="submit"]');
      const email = emailInput.value;
      
      // Placeholder - replace with actual newsletter service integration
      submitBtn.textContent = 'Subscribing...';
      submitBtn.disabled = true;
      
      setTimeout(function() {
        submitBtn.textContent = 'Subscribed!';
        submitBtn.style.background = '#10b981';
        emailInput.value = '';
        
        setTimeout(function() {
          submitBtn.textContent = 'Subscribe';
          submitBtn.style.background = '';
          submitBtn.disabled = false;
        }, 2000);
      }, 1000);
    });
  }

  // Smooth Scroll for Anchor Links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // Reading Progress Bar (for article pages)
  const articleContent = document.querySelector('.article-content');
  
  if (articleContent) {
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    progressBar.innerHTML = '<div class="reading-progress__bar"></div>';
    document.body.appendChild(progressBar);
    
    const bar = progressBar.querySelector('.reading-progress__bar');
    
    // Add styles dynamically
    progressBar.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      z-index: 101;
      background: rgba(0, 0, 0, 0.1);
    `;
    
    bar.style.cssText = `
      height: 100%;
      background: linear-gradient(90deg, #6366f1, #ec4899);
      width: 0%;
      transition: width 0.1s ease;
    `;
    
    window.addEventListener('scroll', function() {
      const windowHeight = window.innerHeight;
      const documentHeight = document.documentElement.scrollHeight - windowHeight;
      const scrolled = window.scrollY;
      const progress = Math.min((scrolled / documentHeight) * 100, 100);
      bar.style.width = progress + '%';
    });
  }

  // External Links - Open in New Tab
  document.querySelectorAll('a[href^="http"]').forEach(function(link) {
    if (!link.href.includes(window.location.hostname)) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });

  // Table of Contents (auto-generate for articles)
  const articleBody = document.querySelector('.article-content');
  
  if (articleBody) {
    const headings = articleBody.querySelectorAll('h2');
    
    if (headings.length >= 3) {
      const toc = document.createElement('nav');
      toc.className = 'table-of-contents';
      toc.innerHTML = '<h4>Table of Contents</h4><ul></ul>';
      
      const tocList = toc.querySelector('ul');
      
      headings.forEach(function(heading, index) {
        const id = 'section-' + (index + 1);
        heading.id = id;
        
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + id;
        a.textContent = heading.textContent;
        li.appendChild(a);
        tocList.appendChild(li);
      });
      
      // Add styles (dark theme)
      toc.style.cssText = `
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border: 1px dashed #333;
        margin-bottom: 2rem;
      `;
      
      toc.querySelector('h4').style.cssText = `
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #888;
        margin-bottom: 1rem;
      `;
      
      toc.querySelector('ul').style.cssText = `
        list-style: none;
        padding: 0;
        margin: 0;
      `;
      
      toc.querySelectorAll('li').forEach(function(li) {
        li.style.cssText = `margin-bottom: 0.5rem;`;
      });
      
      toc.querySelectorAll('a').forEach(function(a) {
        a.style.cssText = `
          color: #fff;
          text-decoration: none;
          font-size: 0.9375rem;
        `;
      });
      
      // Insert at the beginning of article content
      const container = articleBody.querySelector('.container');
      if (container) {
        container.insertBefore(toc, container.firstChild);
      }
    }
  }

  // Console message
  console.log('%cAI Cosmetics Innovation Journal', 
    'font-size: 18px; font-weight: bold; color: #fff;');
  console.log('%cPowered by AI-driven insights', 
    'font-size: 12px; color: #6b7280;');

})();
