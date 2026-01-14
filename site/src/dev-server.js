/**
 * AI Cosmetics Journal - Development Server
 * Simple HTTP server for local development
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const BUILD_DIR = path.join(__dirname, '../build');

// MIME types
const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.xml': 'application/xml',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2'
};

// Run build first
console.log('\\n🔨 Building site...\\n');
require('./build.js');

// Create server
const server = http.createServer((req, res) => {
  // Parse URL
  let urlPath = req.url.split('?')[0];
  
  // Default to index.html for root
  if (urlPath === '/') {
    urlPath = '/index.html';
  }
  
  // Add .html extension if no extension
  if (!path.extname(urlPath) && !urlPath.endsWith('/')) {
    urlPath += '.html';
  }
  
  const filePath = path.join(BUILD_DIR, urlPath);
  const ext = path.extname(filePath);
  const mimeType = MIME_TYPES[ext] || 'application/octet-stream';
  
  // Check if file exists
  fs.access(filePath, fs.constants.F_OK, (err) => {
    if (err) {
      // 404 Not Found
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.end(`
        <!DOCTYPE html>
        <html>
        <head>
          <title>404 - Not Found</title>
          <style>
            body { font-family: system-ui; max-width: 600px; margin: 100px auto; padding: 20px; text-align: center; }
            h1 { color: #6366f1; }
            a { color: #6366f1; }
          </style>
        </head>
        <body>
          <h1>404</h1>
          <p>Page not found: ${urlPath}</p>
          <a href="/">← Back to Home</a>
        </body>
        </html>
      `);
      return;
    }
    
    // Read and serve file
    fs.readFile(filePath, (err, content) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error');
        return;
      }
      
      res.writeHead(200, { 
        'Content-Type': mimeType,
        'Cache-Control': 'no-cache'
      });
      res.end(content);
    });
  });
});

// Start server
server.listen(PORT, () => {
  console.log(`\\n🚀 Development server running at:`);
  console.log(`   http://localhost:${PORT}`);
  console.log(`\\nPress Ctrl+C to stop\\n`);
});

// Watch for file changes (simple file watcher)
const watchDirs = [
  path.join(__dirname, '../../content'),
  path.join(__dirname, 'pages'),
  path.join(__dirname, '../public')
];

let rebuildTimeout = null;

watchDirs.forEach(dir => {
  if (fs.existsSync(dir)) {
    fs.watch(dir, { recursive: true }, (eventType, filename) => {
      if (filename && !filename.startsWith('.')) {
        // Debounce rebuilds
        clearTimeout(rebuildTimeout);
        rebuildTimeout = setTimeout(() => {
          console.log(`\\n📝 Change detected: ${filename}`);
          console.log('🔨 Rebuilding...\\n');
          try {
            require('./build.js');
            console.log('✅ Rebuild complete\\n');
          } catch (err) {
            console.error('❌ Build error:', err.message);
          }
        }, 500);
      }
    });
  }
});
