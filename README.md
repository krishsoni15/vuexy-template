# Vuexy Admin Dashboard Template — Offline Archive & UI Kit

[![Pages](https://img.shields.io/badge/Pages-145%2B%20HTML%20Demos-7367f0?style=flat-square)](./index.html)
[![Harvest Tool](https://img.shields.io/badge/Harvested%20With-WebHarvest-28c76f?style=flat-square)](#-about-this-project)
[![UI Framework](https://img.shields.io/badge/UI-Bootstrap%205.3%20%2B%20Vuexy%20Theme-ff9f43?style=flat-square)](https://pixinvent.com/vuexy-bootstrap-html-admin-template/)
[![Next.js](https://img.shields.io/badge/Next.js-React%20Auth%20Demos-000000?style=flat-square)](./nextjs-login/)
[![Assets](https://img.shields.io/badge/Assets-100%25%20Offline%20%26%20Local-00bad1?style=flat-square)](#-key-features)
[![Theme](https://img.shields.io/badge/Theme-Light%20%26%20Dark%20Mode-ea5455?style=flat-square)](#-interactive-portal--explorer)

A complete, self-contained offline mirror and developer UI kit of the **Vuexy Admin Dashboard Template**, harvested using **WebHarvest**. Includes **145+ ready-to-run HTML pages**, full authentication flows (Bootstrap 5 & Next.js), 100% local self-hosted vendor assets, illustrations, and an interactive **Master Portal & Explorer** with instant search and live preview.

---

## 📌 Quick GitHub Info

- **Repository 1-Line Description**:
  > `Vuexy Admin Dashboard Template — complete offline mirror with 145+ HTML pages, Next.js auth screens, and interactive portal harvested using WebHarvest.`
- **Recommended GitHub Topics / Tags**:
  `vuexy`, `admin-dashboard`, `dashboard-template`, `bootstrap-5`, `nextjs`, `web-harvest`, `html-templates`, `ui-kit`, `offline-mirror`, `auth-templates`

---

## 🌟 About This Project

This repository serves as a self-contained offline reference, rapid prototyping library, and UI asset kit extracted from the PixInvent Vuexy demo mirror using **WebHarvest**.

Every asset—vendor stylesheets, JavaScript libraries, Tabler icon fonts, images, and light/dark vector illustrations—has been localized to eliminate external CDN dependencies, ensuring that all 145+ templates render reliably offline and in air-gapped development environments.

---

## ✨ Key Features

- **🚀 145+ Full-Featured HTML Templates (`html/vertical-menu-template/`)**:
  - Spans 16 categories: Dashboards, eCommerce, Apps, Users, Roles & Permissions, Invoices, Academy, Logistics, Cards, Charts, Forms, Wizards, DataTables, UI Components, and Pages.
- **🔍 Interactive Master Portal (`index.html`)**:
  - Live client-side search across all 145 templates with zero latency.
  - Category filter pills with dynamic page counts.
  - Real-time dark mode and light mode switcher.
  - Modal iframe preview and single-click direct launching.
- **🔐 Comprehensive Authentication Suite (`login/`)**:
  - Both **2-Column Split Cover** and **Centered Basic Card** layouts.
  - Pages for Login, Registration, Forgot Password, Reset Password, 2-Step Verification, and Email Verification.
- **⚛️ Next.js / React MUI Auth Templates (`nextjs-login/`)**:
  - Static export of Next.js login variations (v1 and v2) with bundled `_next` static assets, layouts, and SVG/PNG illustrations.
- **🎨 100% Self-Contained Assets (`assets/` -> `login/assets/`)**:
  - **CSS**: Bootstrap 5.3, Vuexy Core Theme, Page-specific styles, Tabler icons.
  - **JS**: Bootstrap bundle, Popper, jQuery, Perfect Scrollbar, Waves, Form Validation.
  - **Graphics**: High-resolution light and dark SVG/PNG illustrations, UI shapes, and logos.
- **🛠️ Built-in Portal Generator (`build_portal.py`)**:
  - Python build script that parses `pages_data.json` to automatically regenerate `index.html`.

---

## 📁 Directory Structure

```text
vuexy-template/
├── index.html                   # Master Portal & Explorer (Search, Filter, Launch Hub)
├── pages_data.json              # Structured metadata inventory for all 145 pages
├── build_portal.py              # Generator script to rebuild index.html from JSON
├── README.md                    # Repository documentation
├── assets/ -> login/assets/     # Symlink to shared assets directory
│
├── login/                       # Standalone Bootstrap 5 Auth Pages & Shared Assets
│   ├── index.html               # Main login page (Cover layout)
│   ├── auth-login-cover.html    # 2-column split cover layout with illustration
│   ├── auth-login-basic.html    # Centered card layout
│   ├── auth-register-cover.html # Registration cover page
│   ├── auth-register-basic.html # Registration card page
│   ├── auth-forgot-password-cover.html
│   ├── auth-reset-password-cover.html
│   └── assets/                  # 100% Local Self-Contained Vendor Assets
│       ├── css/                 # Demo styles
│       ├── js/                  # Config, main, and auth handlers
│       ├── img/                 # Illustrations, shapes, logos, favicons
│       └── vendor/              # Bootstrap 5, Tabler icons, Popper, jQuery, etc.
│
├── nextjs-login/                # Scraped Next.js (React / MUI) Auth Variants
│   ├── login.html               # Next.js main auth demo
│   ├── login-v1.html            # Variant 1 auth
│   ├── login-v2.html            # Variant 2 auth
│   ├── _next/static/            # Next.js static JS chunks & CSS bundles
│   └── images/                  # Categorized illustrations & brand assets
│
└── html/
    └── vertical-menu-template/  # 145+ Production HTML Pages
        ├── dashboards-crm.html
        ├── app-ecommerce-dashboard.html
        ├── app-logistics-dashboard.html
        ├── app-academy-dashboard.html
        ├── app-chat.html
        ├── app-calendar.html
        ├── app-kanban.html
        ├── app-invoice-list.html
        ├── app-user-list.html
        ├── app-access-roles.html
        ├── tables-datatables-basic.html
        ├── charts-apex.html
        ├── form-wizard-numbered.html
        └── ... (132 more pages)
```

---

## 📊 Category Breakdown (145 Pages)

| Category | Pages | Highlights |
| :--- | :---: | :--- |
| **UI Components** | 32 | Modals, Offcanvas, Toasts, Dropdowns, Badges, SweetAlert2, Drag-and-drop, Tour |
| **Pages** | 27 | Account Settings, Profiles, FAQ, Pricing, Error (404/500), Coming Soon, Maintenance |
| **eCommerce** | 19 | Product Catalog, Order Details, Customer Management, Reviews, Shipping, Checkout |
| **Forms** | 16 | Basic Inputs, Custom Options, Editors, File Upload, Input Groups, Pickers, Validation |
| **Authentication** | 13 | Login, Register, Forgot Password, Reset Password, 2-Step Verification, Multi-steps |
| **Users** | 6 | User List, Account View, Billing View, Security View, Notifications View |
| **Invoice** | 5 | Invoice List, Preview, Add, Edit, Print View |
| **Cards** | 5 | Basic, Advance, Statistics, Analytics, Card Actions |
| **Apps** | 4 | Real-time Chat, Calendar, Kanban Board, Email Client |
| **Tables** | 4 | Basic HTML Tables, DataTables Basic, DataTables Advanced, DataTables Extensions |
| **Academy** | 3 | Course Dashboard, Course Listing, Course Details |
| **Wizards** | 3 | Numbered Wizard, Icon Wizard, Property Listing & Checkout Wizards |
| **Roles & Permissions** | 2 | Role Cards & Permissions Matrix, Granular Access Control Table |
| **Logistics** | 2 | Fleet Tracking & Logistics Operations Dashboard |
| **Charts** | 2 | ApexCharts (Area, Bar, Donut, Candlestick), Chart.js |
| **Dashboards** | 2 | CRM Analytics, Default Analytics Overview |

---

## ⚡ Quick Start & How to Run

### Method 1: Open Directly in Browser
All paths are relative. You can simply double-click or open any file directly in Chrome, Firefox, Safari, or Edge:
- **Master Explorer**: Open `vuexy-template/index.html`
- **Auth Hub**: Open `vuexy-template/login/index.html`

### Method 2: Serve via Node.js Static Server
From within the `vuexy-template` directory:
```bash
npx serve . -p 3000
# Or using http-server
npx http-server -p 3000 -c-1
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### Method 3: Serve via Python
```bash
python3 -m http.server 3000
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### Method 4: VS Code / Cursor Live Server
Right-click on `index.html` and select **"Open with Live Server"**.

---

## 🔄 Regenerating the Master Portal

If you add new HTML files or modify page categories:
1. Update `pages_data.json` with the page details:
   ```json
   {
     "filename": "my-new-page.html",
     "title": "My New Page Title",
     "category": "Dashboards",
     "url": "html/vertical-menu-template/my-new-page.html",
     "size": 150000
   }
   ```
2. Run the build script:
   ```bash
   python3 build_portal.py
   ```
This updates `index.html` with updated counts, search indices, and filter pills.

---

## 💡 How to Extract & Integrate into React / Next.js

1. **Brand Illustrations & Icons**:
   - Copy SVG/PNG graphics from `login/assets/img/illustrations/` into your React/Next.js `public/images/illustrations/` directory.
   - Use them directly:
     ```tsx
     import Image from "next/image";

     <Image
       src="/images/illustrations/auth-login-illustration-light.png"
       alt="Login Graphic"
       width={500}
       height={450}
       priority
     />
     ```
2. **Form Elements & CSS Tokens**:
   - Inspect CSS variables in `login/assets/vendor/css/core.css` (`--primary: #7367f0`, `--border-color`, etc.) and adapt them into your Tailwind or vanilla CSS design tokens.
3. **Layout Blueprints**:
   - Check `login/auth-login-cover.html` or `html/vertical-menu-template/app-ecommerce-dashboard.html` for clean HTML5 grid structures, responsive breakpoints, and card hierarchy.

---

## ⚖️ Credits & Disclaimer

- **Harvesting Tool**: Scraped and downloaded using **WebHarvest**.
- **Original Template & Copyright**: Designed and copyrighted by **PixInvent**. Vuexy is a premium commercial template sold via Envato Market / ThemeForest.
- **Usage Notice**: This repository is assembled strictly for educational exploration, layout study, and offline development prototyping. If you plan to use Vuexy in a commercial production application, please purchase an official license from [PixInvent on ThemeForest](https://themeforest.net/item/vuexy-vuejs-html-laravel-admin-dashboard-template/23328599).
