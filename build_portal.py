import json

with open('/home/krish/Desktop/project/socker-data/vuexy-template/pages_data.json') as f:
    pages = json.load(f)

cat_priority = {
    'Dashboards': 1,
    'Authentication': 2,
    'eCommerce': 3,
    'Apps': 4,
    'Users': 5,
    'Roles & Permissions': 6,
    'Invoice': 7,
    'Academy': 8,
    'Logistics': 9,
    'Cards': 10,
    'Charts': 11,
    'Forms': 12,
    'Wizards': 13,
    'Tables': 14,
    'UI Components': 15,
    'Pages': 16
}

pages.sort(key=lambda x: (cat_priority.get(x['category'], 99), x['title']))
pages_json = json.dumps(pages)

html_template = f"""<!DOCTYPE html>
<html lang="en" data-bs-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vuexy Master Portal & Explorer | Socker Data</title>
  <link rel="icon" type="image/x-icon" href="login/assets/img/favicon/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="login/assets/vendor/css/core.css">
  <link rel="stylesheet" href="login/assets/vendor/fonts/iconify-icons.css">
  <style>
    :root {{
      --primary: #7367f0;
      --primary-hover: #5e50ee;
      --primary-rgb: 115, 103, 240;
      --bg-body: #f8f7fa;
      --card-bg: #ffffff;
      --border-color: #e6e5ec;
      --text-main: #4b465c;
      --text-muted: #82808b;
    }}
    [data-theme="dark"] {{
      --bg-body: #171724;
      --card-bg: #232233;
      --border-color: #35344a;
      --text-main: #cfcde4;
      --text-muted: #8784a3;
    }}
    body {{
      font-family: 'Public Sans', -apple-system, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      margin: 0;
      transition: background-color 0.2s;
    }}
    .top-header {{
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    .hero-section {{
      background: linear-gradient(135deg, #7367f0 0%, #8f5fe8 100%);
      color: #fff;
      padding: 2.5rem 1.5rem 2rem;
      border-radius: 0 0 1.5rem 1.5rem;
      box-shadow: 0 8px 30px rgba(115, 103, 240, 0.25);
    }}
    .search-input-wrapper {{
      position: relative;
      max-width: 680px;
      margin: 0 auto;
    }}
    .search-input {{
      border-radius: 50px;
      padding: 14px 24px 14px 52px;
      border: 2px solid transparent;
      font-size: 1.05rem;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
      transition: all 0.2s;
      background: #fff;
      color: #333;
      width: 100%;
    }}
    .search-input:focus {{
      outline: none;
      box-shadow: 0 8px 32px rgba(115, 103, 240, 0.3);
      border-color: #ce9ffc;
    }}
    .search-icon-pos {{
      position: absolute;
      left: 20px;
      top: 50%;
      transform: translateY(-50%);
      color: #7367f0;
      font-size: 1.25rem;
    }}
    .cat-pill {{
      border: 1px solid var(--border-color);
      background: var(--card-bg);
      color: var(--text-main);
      border-radius: 50px;
      padding: 6px 14px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease-in-out;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      user-select: none;
    }}
    .cat-pill:hover {{
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-1px);
    }}
    .cat-pill.active {{
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
      box-shadow: 0 3px 12px rgba(115, 103, 240, 0.35);
    }}
    .cat-pill .count {{
      background: rgba(0,0,0,0.08);
      padding: 2px 7px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 600;
    }}
    .cat-pill.active .count {{
      background: rgba(255,255,255,0.25);
      color: #fff;
    }}
    .page-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 18px;
      height: 100%;
      display: flex;
      flex-direction: column;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .page-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(75, 70, 92, 0.1);
      border-color: var(--primary);
    }}
    .cat-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 4px 8px;
      border-radius: 6px;
    }}
    .cat-badge-Dashboards {{ background: rgba(115, 103, 240, 0.12); color: #7367f0; }}
    .cat-badge-Authentication {{ background: rgba(255, 76, 81, 0.12); color: #ff4c51; }}
    .cat-badge-eCommerce {{ background: rgba(40, 199, 111, 0.12); color: #28c76f; }}
    .cat-badge-Apps {{ background: rgba(0, 186, 209, 0.12); color: #00bad1; }}
    .cat-badge-Users {{ background: rgba(255, 159, 67, 0.12); color: #ff9f43; }}
    .cat-badge-Forms {{ background: rgba(102, 16, 242, 0.12); color: #6610f2; }}
    .cat-badge-Tables {{ background: rgba(32, 201, 151, 0.12); color: #20c997; }}
    .cat-badge-UIComponents {{ background: rgba(115, 103, 240, 0.12); color: #7367f0; }}
    .cat-badge-Cards {{ background: rgba(235, 61, 99, 0.12); color: #eb3d63; }}
    .cat-badge-Charts {{ background: rgba(255, 171, 29, 0.12); color: #ffab1d; }}
    .cat-badge-Pages {{ background: rgba(130, 128, 139, 0.12); color: #82808b; }}
    .cat-badge-Wizards {{ background: rgba(13, 147, 148, 0.12); color: #0d9394; }}
    .cat-badge-Invoice {{ background: rgba(40, 199, 111, 0.12); color: #28c76f; }}
    .cat-badge-Academy {{ background: rgba(115, 103, 240, 0.12); color: #7367f0; }}
    .cat-badge-Logistics {{ background: rgba(255, 159, 67, 0.12); color: #ff9f43; }}
    .cat-badge-RolesPermissions {{ background: rgba(0, 186, 209, 0.12); color: #00bad1; }}
    
    .btn-preview {{
      background: rgba(115, 103, 240, 0.1);
      color: #7367f0;
      font-weight: 600;
      border: none;
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .btn-preview:hover {{
      background: #7367f0;
      color: #fff;
    }}
    .btn-open {{
      border: 1px solid var(--border-color);
      background: var(--card-bg);
      color: var(--text-main);
      font-weight: 500;
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      text-decoration: none;
      transition: all 0.15s;
    }}
    .btn-open:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}
    
    /* Live Preview Modal Overlay */
    .preview-modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(15, 17, 26, 0.75);
      backdrop-filter: blur(6px);
      z-index: 2000;
      display: none;
      flex-direction: column;
    }}
    .preview-modal-overlay.active {{
      display: flex;
    }}
    .preview-header {{
      background: #1e1e2d;
      color: #fff;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    .preview-body {{
      flex: 1;
      background: #2b2c40;
      display: flex;
      justify-content: center;
      align-items: stretch;
      padding: 16px;
      overflow: hidden;
    }}
    .preview-frame-container {{
      width: 100%;
      height: 100%;
      background: #fff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0,0,0,0.5);
      transition: max-width 0.3s ease;
    }}
    .preview-frame {{
      width: 100%;
      height: 100%;
      border: none;
    }}
    .device-btn {{
      background: rgba(255,255,255,0.1);
      border: none;
      color: #ccc;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .device-btn.active, .device-btn:hover {{
      background: #7367f0;
      color: #fff;
    }}
  </style>
</head>
<body>

  <!-- Top Bar -->
  <header class="top-header px-4 py-3">
    <div class="container-fluid d-flex align-items-center justify-content-between">
      <div class="d-flex align-items-center gap-3">
        <span class="p-2 bg-primary rounded-3 text-white d-flex align-items-center justify-content-center" style="width: 38px; height: 38px;">
          <svg width="24" height="16" viewBox="0 0 32 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M0.00172773 0V6.85398C0.00172773 6.85398 -0.133178 9.01207 1.98092 10.8388L13.6912 21.9964L19.7809 21.9181L18.8042 9.88248L16.4951 7.17289L9.23799 0H0.00172773Z" fill="#fff"></path>
            <path opacity="0.1" fill-rule="evenodd" clip-rule="evenodd" d="M7.69824 16.4364L12.5199 3.23696L16.5541 7.25596L7.69824 16.4364Z" fill="#000"></path>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M7.77295 16.3566L23.6563 0H32V6.88383C32 6.88383 31.8262 9.17836 30.6591 10.4057L19.7824 22H13.6938L7.77295 16.3566Z" fill="#fff"></path>
          </svg>
        </span>
        <div>
          <h5 class="mb-0 fw-bold">Vuexy Master Portal</h5>
          <small class="text-muted">Socker Data &bull; 145 Fully Accessible Pages</small>
        </div>
      </div>
      <div class="d-flex align-items-center gap-2">
        <span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25 px-3 py-2 rounded-pill d-none d-md-inline-block">
          &bull; 100% Offline Compatible
        </span>
        <a href="login/auth-login-cover.html" class="btn btn-sm btn-primary">
          🔑 Flagship Login
        </a>
        <button id="themeToggle" class="btn btn-sm btn-outline-secondary" title="Toggle Dark/Light Mode">
          🌙
        </button>
      </div>
    </div>
  </header>

  <!-- Hero & Search -->
  <section class="hero-section text-center">
    <div class="container">
      <h2 class="fw-bold text-white mb-2">All 145 Vuexy Templates in One Place</h2>
      <p class="lead text-white text-opacity-75 mb-4 small">
        Search, filter, preview instantly in-browser, or open any page directly with offline styling & scripts.
      </p>
      <div class="search-input-wrapper mb-3">
        <span class="search-icon-pos">🔍</span>
        <input type="text" id="pageSearch" class="search-input" placeholder="Search any page (e.g. login, dashboard, invoice, ecommerce, datatables)..." autofocus>
      </div>
      <div class="text-white-50 small">
        Press <kbd class="bg-white bg-opacity-25 text-white border-0 px-2 py-1 rounded">/</kbd> to focus search &bull; Click <b>👁 Preview</b> on any card for instant in-page viewing
      </div>
    </div>
  </section>

  <!-- Categories Filter Bar -->
  <div class="container my-4">
    <div id="categoryFilters" class="d-flex flex-wrap gap-2 justify-content-center">
      <!-- Filter pills dynamically generated -->
    </div>
  </div>

  <!-- Page Results Grid -->
  <main class="container mb-5 flex-grow-1">
    <div class="d-flex align-items-center justify-content-between mb-3">
      <div id="resultsCount" class="text-muted small fw-semibold">Showing 145 pages</div>
      <div class="d-flex gap-2">
        <button id="sortToggle" class="btn btn-sm btn-outline-secondary">A-Z Alphabetical</button>
      </div>
    </div>
    
    <div id="pagesGrid" class="row g-3">
      <!-- Cards dynamically generated -->
    </div>
  </main>

  <!-- Live In-Page Preview Modal -->
  <div id="previewModal" class="preview-modal-overlay">
    <div class="preview-header">
      <div class="d-flex align-items-center gap-3">
        <span id="previewPageTitle" class="fw-bold fs-6">Page Title</span>
        <span id="previewPageFile" class="badge bg-secondary font-monospace small">filename.html</span>
      </div>
      
      <!-- Device viewport buttons -->
      <div class="d-flex align-items-center gap-2">
        <button class="device-btn active" data-width="100%">🖥️ Desktop</button>
        <button class="device-btn" data-width="768px">📱 Tablet</button>
        <button class="device-btn" data-width="375px">📱 Mobile</button>
        <a id="previewOpenTab" href="#" target="_blank" class="btn btn-sm btn-primary ms-2">
          Open Tab ↗
        </a>
        <button id="previewClose" class="btn btn-sm btn-outline-light ms-2">
          ✕ Close
        </button>
      </div>
    </div>
    <div class="preview-body">
      <div id="frameContainer" class="preview-frame-container" style="max-width: 100%;">
        <iframe id="previewIframe" class="preview-frame" src="about:blank"></iframe>
      </div>
    </div>
  </div>

  <footer class="bg-white border-top py-3 text-center text-muted small mt-auto">
    <div class="container">
      Vuexy Admin Template Master Explorer &bull; Socker Data Project &bull; Extracted from PixInvent mirror
    </div>
  </footer>

  <script>
    const PAGES = {pages_json};

    let currentCategory = 'all';
    let searchQuery = '';
    let sortMode = 'priority';

    const grid = document.getElementById('pagesGrid');
    const searchInput = document.getElementById('pageSearch');
    const catContainer = document.getElementById('categoryFilters');
    const resultsCount = document.getElementById('resultsCount');
    const modal = document.getElementById('previewModal');
    const iframe = document.getElementById('previewIframe');
    const previewTitle = document.getElementById('previewPageTitle');
    const previewFile = document.getElementById('previewPageFile');
    const previewTabBtn = document.getElementById('previewOpenTab');
    const frameContainer = document.getElementById('frameContainer');

    const categories = ['all'];
    const catCounts = {{ 'all': PAGES.length }};
    PAGES.forEach(p => {{
      catCounts[p.category] = (catCounts[p.category] || 0) + 1;
      if (!categories.includes(p.category)) categories.push(p.category);
    }});

    function renderCategoryPills() {{
      catContainer.innerHTML = categories.map(cat => `
        <button class="cat-pill ${{cat === currentCategory ? 'active' : ''}}" data-cat="${{cat}}">
          ${{cat === 'all' ? '🌟 All Pages' : cat}}
          <span class="count">${{catCounts[cat]}}</span>
        </button>
      `).join('');

      catContainer.querySelectorAll('.cat-pill').forEach(btn => {{
        btn.addEventListener('click', () => {{
          currentCategory = btn.getAttribute('data-cat');
          renderCategoryPills();
          renderGrid();
        }});
      }});
    }}

    function renderGrid() {{
      let filtered = PAGES.filter(p => {{
        const matchesCat = (currentCategory === 'all' || p.category === currentCategory);
        const q = searchQuery.toLowerCase().trim();
        const matchesQuery = !q || 
          p.title.toLowerCase().includes(q) || 
          p.filename.toLowerCase().includes(q) || 
          p.category.toLowerCase().includes(q);
        return matchesCat && matchesQuery;
      }});

      if (sortMode === 'alpha') {{
        filtered.sort((a,b) => a.title.localeCompare(b.title));
      }}

      resultsCount.textContent = `Showing ${{filtered.length}} of ${{PAGES.length}} pages`;

      if (filtered.length === 0) {{
        grid.innerHTML = `
          <div class="col-12 text-center py-5">
            <div class="fs-1 mb-2">🔍</div>
            <h5 class="text-muted">No pages found matching "${{searchQuery}}"</h5>
            <button class="btn btn-sm btn-outline-primary mt-2" onclick="resetSearch()">Clear search</button>
          </div>
        `;
        return;
      }}

      grid.innerHTML = filtered.map(item => `
        <div class="col-sm-6 col-md-4 col-lg-3">
          <div class="page-card">
            <div class="d-flex justify-content-between align-items-start mb-2">
              <span class="cat-badge cat-badge-${{item.category.replace(/[^a-zA-Z0-9]/g, '')}}">${{item.category}}</span>
              <small class="text-muted font-monospace" style="font-size: 0.7rem;">${{(item.size / 1024).toFixed(0)}} KB</small>
            </div>
            
            <h6 class="fw-bold mb-1 text-truncate" title="${{item.title}}">${{item.title}}</h6>
            <div class="text-muted small font-monospace text-truncate mb-3" style="font-size: 0.75rem;" title="${{item.filename}}">
              ${{item.filename}}
            </div>

            <div class="mt-auto d-flex gap-2 pt-2 border-top">
              <button class="btn-preview flex-grow-1 justify-content-center" onclick="openPreview('${{item.url}}', '${{item.title.replace(/'/g, "\\\\\\'")}}', '${{item.filename}}')">
                👁 Preview
              </button>
              <a href="${{item.url}}" target="_blank" class="btn-open" title="Open full page in new tab">
                ↗
              </a>
            </div>
          </div>
        </div>
      `).join('');
    }}

    function openPreview(url, title, filename) {{
      previewTitle.textContent = title;
      previewFile.textContent = filename;
      previewTabBtn.href = url;
      iframe.src = url;
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closePreview() {{
      modal.classList.remove('active');
      iframe.src = 'about:blank';
      document.body.style.overflow = '';
    }}

    document.getElementById('previewClose').addEventListener('click', closePreview);
    modal.addEventListener('click', (e) => {{
      if (e.target === modal || e.target.classList.contains('preview-body')) {{
        closePreview();
      }}
    }});

    document.querySelectorAll('.device-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.device-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        frameContainer.style.maxWidth = btn.getAttribute('data-width');
      }});
    }});

    function resetSearch() {{
      searchInput.value = '';
      searchQuery = '';
      currentCategory = 'all';
      renderCategoryPills();
      renderGrid();
    }}

    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      renderGrid();
    }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === '/' && document.activeElement !== searchInput) {{
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      }} else if (e.key === 'Escape' && modal.classList.contains('active')) {{
        closePreview();
      }}
    }});

    document.getElementById('sortToggle').addEventListener('click', function() {{
      sortMode = sortMode === 'priority' ? 'alpha' : 'priority';
      this.textContent = sortMode === 'alpha' ? 'Categorized' : 'A-Z Alphabetical';
      renderGrid();
    }});

    const themeToggle = document.getElementById('themeToggle');
    let isDark = localStorage.getItem('vuexy-hub-theme') === 'dark';
    function applyTheme() {{
      document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
      document.documentElement.setAttribute('data-bs-theme', isDark ? 'dark' : 'light');
      themeToggle.textContent = isDark ? '☀️' : '🌙';
    }}
    applyTheme();
    themeToggle.addEventListener('click', () => {{
      isDark = !isDark;
      localStorage.setItem('vuexy-hub-theme', isDark ? 'dark' : 'light');
      applyTheme();
    }});

    renderCategoryPills();
    renderGrid();
  </script>
</body>
</html>
"""

with open('/home/krish/Desktop/project/socker-data/vuexy-template/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Generated Vuexy Master Portal at vuexy-template/index.html')
