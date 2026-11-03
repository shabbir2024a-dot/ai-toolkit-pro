import json
import os
import re
from generate_gear_assets import GEAR_PRODUCTS

ASIN_UPDATES = {
    "dji-osmo-pocket-3-creator-combo": "B0FKT9K6CB",
    "shure-mv7-plus-podcast-microphone": "B0CTJ7PVN1",
    "rode-podmic-dynamic-podcasting-mic": "B0CKPTX13H",
    "elgato-wave-3-premium-usb-mic": "B08SD8P1V2",
    "logitech-mx-master-3s-wireless-mouse": "B0FPM2VC6Q",
    "focusrite-scarlett-2i2-studio-bundle": "B07QR6Z1JB",
    "fifine-k688-usb-xlr-podcast-mic": "B0D458QDVN",
    "rode-psa1-plus-professional-boom-arm": "B09JBVR5B4",
    "sony-alpha-zve10-with-zoom-lens": "B0DJSLJYCF",
    "godox-sl60w-continuous-led-video-light": "B0FWRVVZJL",
    "neewer-660-led-video-light-2pack-kit": "B0DNFW6NSP",
    "elgato-cam-link-4k-usb-capture": "B07K3FN5MR",
    "ulanzi-vl49-rgb-pocket-led-light": "B08MDQ3CJY",
    "zotac-rtx-4060-twin-edge-gpu": "B0FH6JPVZB",
    "corsair-vengeance-ddr5-32gb-ram": "B0GGJ79NR3",
    "samsung-odyssey-g7-32-inch-curved-gaming-monitor": "B0FDL66T4D",
    "lg-ultragear-27-inch-qhd-nano-ips-monitor": "B0H451STZ4",
    "keychron-k2-wireless-mechanical-keyboard": "B0DXZ97PCG",
    "asus-rog-strix-850w-gold-psu": "B0F5WSDWZQ",
    "ant-esports-ice-511mt-mesh-cabinet": "B0CRNQJBWB",
    "green-soul-monster-ultimate-creator-chair": "B085NPF8BK",
    "featherlite-liberate-high-back-chair": "B08T7HGNMB",
    "jin-office-motorized-electric-standing-desk": "B0FGJXBHS1",
    "benq-screenbar-halo-wireless-monitor-light": "B0DK59YKRS",
    "elgato-prompter-studio-teleprompter": "B0CH3P9K1X",
    "huion-kamvas-16-graphics-drawing-tablet": "B0FBKF1899",
    "rife-dual-monitor-arm-gas-spring": "B0CKW835X3",
    "portronics-clamp-x-laptop-stand": "B0C9J63G2F"
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Amazon Creator Store | 70+ Battle-Tested Tech Rigs | AI Toolkit Pro</title>
  <meta name="description" content="Shop official Amazon India creator gear: Shure studio mics, Sony 4K cameras, DJI Osmo Pocket 3, RTX GPUs, ergonomic standing desks, and SaaS tools. Store ID: aitoolkitpro-21.">
  <meta name="keywords" content="Amazon India, Creator Gear, Shure SM7B, Fifine AM8, Sony ZV-E10, DJI Osmo Pocket 3, RTX 4070, Studio Microphones, Ergonomic Chair, AI Toolkit Pro">
  <link rel="canonical" href="https://ai-toolkit-pro-eta.vercel.app/creator-gear">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Amazon Creator Gear Store | AI Toolkit Pro">
  <meta property="og:description" content="Shop verified creator gear with live Amazon India discounts & Prime 1-day delivery. Official Amazon Associates partner.">
  <meta property="og:image" content="https://ai-toolkit-pro-eta.vercel.app/assets/products/shure-sm7b-dynamic-vocal-mic.jpg">
  <meta property="og:url" content="https://ai-toolkit-pro-eta.vercel.app/creator-gear">
  <meta property="og:type" content="website">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-dark: #031716;
      --card-bg: #042426;
      --card-hover: #07383a;
      --border-teal: rgba(12, 150, 156, 0.25);
      --border-glow: rgba(12, 150, 156, 0.55);
      --accent-cyan: #0C969C;
      --accent-emerald: #0A7075;
      --amazon-orange: #FF9900;
      --amazon-yellow: #ffd814;
      --amazon-yellow-hover: #f7ca00;
      --amazon-red: #cc0c39;
      --amazon-blue: #007185;
      --amazon-prime: #00A8E1;
      --text-main: #FFFFFF;
      --text-muted: #94A3B8;
      --chip-bg: #1B3847;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(1200px 600px at 50% -50px, rgba(12, 150, 156, 0.22), transparent 75%),
        radial-gradient(800px 500px at 90% 400px, rgba(10, 112, 117, 0.14), transparent 70%);
      background-attachment: fixed;
      color: var(--text-main);
      font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    a { color: var(--accent-cyan); text-decoration: none; transition: all 0.2s; }
    a:hover { color: #FFFFFF; }

    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 20px;
      width: 100%;
    }

    /* Header */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(3, 23, 22, 0.95);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-teal);
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    .nav-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 72px;
      gap: 16px;
    }

    .logo-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Bricolage Grotesque', sans-serif;
      font-size: 1.35rem;
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: -0.02em;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .logo-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--amazon-orange);
      box-shadow: 0 0 14px var(--amazon-orange);
      flex-shrink: 0;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 18px;
    }

    .nav-link {
      color: #CBD5E1;
      font-weight: 500;
      font-size: 0.90rem;
      transition: color 0.2s;
      white-space: nowrap;
    }
    .nav-link:hover { color: #FFFFFF; }
    .nav-link.active {
      color: #031716;
      background: var(--amazon-orange);
      padding: 6px 14px;
      border-radius: 20px;
      font-weight: 700;
    }

    .btn-header-cta {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
      color: #FFFFFF !important;
      font-weight: 700;
      font-size: 0.88rem;
      padding: 8px 18px;
      border-radius: 24px;
      box-shadow: 0 4px 16px rgba(12, 150, 156, 0.35);
      transition: all 0.25s ease;
      white-space: nowrap;
    }

    /* Mobile Hamburger & Drawer */
    .mobile-menu-btn {
      display: none;
      flex-direction: column;
      justify-content: space-between;
      width: 26px;
      height: 19px;
      background: transparent;
      border: none;
      cursor: pointer;
      padding: 0;
      z-index: 101;
    }
    .mobile-menu-btn span {
      width: 100%;
      height: 2.5px;
      background-color: #FFFFFF;
      border-radius: 2px;
      transition: all 0.3s ease;
    }

    .mobile-drawer {
      position: fixed;
      top: 0;
      right: -320px;
      width: 300px;
      height: 100vh;
      background: #042426;
      border-left: 1px solid var(--border-teal);
      padding: 24px;
      z-index: 1000;
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: -8px 0 30px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
    }
    .mobile-drawer.open { right: 0; }
    .mobile-drawer-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid rgba(12, 150, 156, 0.2);
    }
    .mobile-drawer-close {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #FFFFFF;
      font-size: 1.2rem;
      width: 36px;
      height: 36px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .mobile-drawer-links {
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex: 1;
    }
    .mobile-drawer-links a {
      color: #CBD5E1;
      font-size: 0.98rem;
      font-weight: 500;
      padding: 10px 14px;
      border-radius: 8px;
      transition: all 0.2s;
    }
    .mobile-drawer-links a:hover, .mobile-drawer-links a.active {
      background: rgba(12, 150, 156, 0.18);
      color: var(--accent-cyan);
    }
    .mobile-drawer-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 999;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }
    .mobile-drawer-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    /* Amazon Subheader Ribbon */
    .amazon-subnav {
      background: #021211;
      border-bottom: 1px solid rgba(12, 150, 156, 0.2);
      padding: 10px 0;
      font-size: 0.85rem;
    }
    .amazon-subnav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
    }
    .deliver-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #CBD5E1;
    }
    .deliver-pill svg { color: var(--amazon-orange); }
    .storefront-verified {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'IBM Plex Mono', monospace;
      color: var(--accent-cyan);
      font-size: 0.78rem;
      background: rgba(12, 150, 156, 0.12);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(12, 150, 156, 0.3);
    }

    /* Hero Banner */
    .hero {
      padding: 44px 0 28px;
      text-align: center;
    }

    .amazon-hero-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 153, 0, 0.12);
      border: 1px solid rgba(255, 153, 0, 0.35);
      padding: 6px 18px;
      border-radius: 30px;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--amazon-orange);
      margin-bottom: 16px;
      letter-spacing: 0.04em;
    }

    .hero-title {
      font-family: 'Bricolage Grotesque', sans-serif;
      font-size: clamp(2.2rem, 4.5vw, 3.6rem);
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: 16px;
      max-width: 980px;
      margin-left: auto;
      margin-right: auto;
    }
    .hero-title span {
      background: linear-gradient(135deg, #FF9900 20%, #F59E0B 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-sub {
      color: #94A3B8;
      font-size: 1.1rem;
      max-width: 820px;
      margin: 0 auto 28px;
      line-height: 1.6;
    }

    .trust-strip {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 36px;
    }

    .trust-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(4, 36, 38, 0.85);
      border: 1px solid var(--border-teal);
      padding: 7px 16px;
      border-radius: 20px;
      font-size: 0.84rem;
      color: #CBD5E1;
    }
    .trust-badge-pill strong { color: #FFFFFF; }

    /* Amazon Search & Category Bar */
    .controls-wrapper {
      background: rgba(4, 36, 38, 0.95);
      border: 1px solid var(--border-teal);
      border-radius: 16px;
      padding: 20px;
      margin-bottom: 36px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }

    .search-row {
      display: flex;
      gap: 12px;
      margin-bottom: 16px;
    }

    .search-input-box {
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
    }
    .search-input-box svg {
      position: absolute;
      left: 16px;
      color: var(--amazon-orange);
      pointer-events: none;
    }
    .search-input-box input {
      width: 100%;
      height: 48px;
      background: #FFFFFF;
      border: 2px solid transparent;
      border-radius: 10px;
      padding: 0 16px 0 46px;
      color: #0F172A;
      font-size: 0.95rem;
      font-weight: 500;
      outline: none;
      transition: all 0.25s;
    }
    .search-input-box input:focus {
      border-color: var(--amazon-orange);
      box-shadow: 0 0 16px rgba(255, 153, 0, 0.4);
    }
    .search-input-box input::placeholder {
      color: #64748B;
    }

    .sort-select {
      height: 48px;
      background: rgba(3, 23, 22, 0.95);
      border: 1px solid var(--border-teal);
      border-radius: 10px;
      padding: 0 16px;
      color: #FFFFFF;
      font-size: 0.9rem;
      outline: none;
      cursor: pointer;
    }

    .category-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tab-btn {
      background: rgba(3, 23, 22, 0.8);
      border: 1px solid var(--border-teal);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .tab-btn:hover {
      color: #FFFFFF;
      border-color: var(--amazon-orange);
    }
    .tab-btn.active {
      background: var(--amazon-orange);
      color: #031716;
      border-color: var(--amazon-orange);
      font-weight: 700;
      box-shadow: 0 4px 14px rgba(255, 153, 0, 0.35);
    }

    /* Product Grid */
    .gear-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 24px;
      margin-bottom: 60px;
    }

    /* Amazon-Kind Product Card */
    .gear-card {
      background: var(--card-bg);
      border: 1px solid var(--border-teal);
      border-radius: 18px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .gear-card:hover {
      transform: translateY(-5px);
      border-color: rgba(255, 153, 0, 0.5);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6), 0 0 20px rgba(255, 153, 0, 0.15);
    }

    /* Clean White Studio Product Photo Canvas */
    .product-photo-card {
      width: 100%;
      height: 250px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      padding: 16px;
    }

    .product-real-img {
      max-width: 85%;
      max-height: 215px;
      width: auto;
      height: auto;
      object-fit: contain;
      transition: transform 0.4s ease;
      filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.15));
    }
    .gear-card:hover .product-real-img {
      transform: scale(1.06);
    }

    /* Amazon Badges */
    .badge-best-seller {
      position: absolute;
      top: 12px;
      left: 12px;
      background: #e67a00;
      color: #ffffff;
      font-size: 0.70rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      letter-spacing: 0.02em;
      z-index: 2;
    }
    .badge-limited-deal {
      position: absolute;
      top: 12px;
      left: 12px;
      background: #cc0c39;
      color: #ffffff;
      font-size: 0.70rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      letter-spacing: 0.02em;
      z-index: 2;
    }
    .badge-overall-pick {
      position: absolute;
      top: 12px;
      left: 12px;
      background: #002f36;
      color: #ffffff;
      font-size: 0.70rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      z-index: 2;
    }

    .discount-floating-pill {
      position: absolute;
      top: 12px;
      right: 12px;
      background: #22c55e;
      color: #031716;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 4px 8px;
      border-radius: 6px;
      z-index: 2;
    }

    /* Card Details */
    .card-body {
      padding: 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .brand-store-link {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 6px;
    }

    .card-title {
      font-family: 'Bricolage Grotesque', sans-serif;
      font-size: 1.18rem;
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1.35;
      margin-bottom: 6px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      min-height: 48px;
    }

    /* Star Rating */
    .amazon-rating-row {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
    }
    .amazon-stars {
      color: #ffa41c;
      font-size: 0.92rem;
      letter-spacing: 1px;
    }
    .amazon-rating-score {
      font-size: 0.85rem;
      font-weight: 700;
      color: #FFFFFF;
    }
    .amazon-rating-count {
      font-size: 0.80rem;
      color: var(--accent-cyan);
    }

    .social-proof-line {
      font-size: 0.78rem;
      color: #94A3B8;
      margin-bottom: 12px;
    }

    /* Pricing Section */
    .amazon-price-row {
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 2px;
    }
    .amazon-discount-rate {
      font-size: 1.4rem;
      font-weight: 300;
      color: #ef4444;
    }
    .amazon-price-main {
      font-family: 'Bricolage Grotesque', sans-serif;
      font-size: 1.6rem;
      font-weight: 800;
      color: #FFFFFF;
      display: flex;
      align-items: flex-start;
    }
    .amazon-currency {
      font-size: 0.95rem;
      font-weight: 600;
      margin-right: 2px;
      position: relative;
      top: 3px;
    }
    .amazon-mrp {
      font-size: 0.82rem;
      color: #64748B;
      margin-bottom: 10px;
    }
    .amazon-mrp span {
      text-decoration: line-through;
    }

    /* Prime delivery tag */
    .prime-delivery-tag {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.82rem;
      color: #CBD5E1;
      margin-bottom: 6px;
    }
    .prime-logo-badge {
      display: inline-flex;
      align-items: center;
      font-size: 0.85rem;
      font-weight: 900;
      color: #00A8E1;
      font-style: italic;
      letter-spacing: -0.04em;
    }
    .prime-check {
      color: #FF9900;
      font-style: normal;
      margin-right: 2px;
      font-weight: 900;
    }

    .in-stock-line {
      font-size: 0.82rem;
      font-weight: 700;
      color: #22c55e;
      margin-bottom: 12px;
    }

    /* Specs List */
    .card-specs-list {
      list-style: none;
      margin-bottom: 18px;
      border-top: 1px dashed rgba(12, 150, 156, 0.2);
      padding-top: 12px;
      flex: 1;
    }

    .card-spec-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.78rem;
      color: #94A3B8;
      margin-bottom: 4px;
    }
    .card-spec-item::before {
      content: "•";
      color: var(--amazon-orange);
      font-weight: 800;
    }

    /* Actions */
    .card-actions {
      display: flex;
      gap: 8px;
      margin-top: auto;
    }

    .btn-amazon-primary {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: #ffd814;
      border: 1px solid #fcd200;
      border-radius: 20px;
      color: #0f1111 !important;
      font-weight: 800;
      font-size: 0.90rem;
      padding: 10px 16px;
      box-shadow: 0 2px 5px rgba(213,217,217,.3);
      transition: all 0.2s ease;
      letter-spacing: -0.01em;
    }
    .btn-amazon-primary:hover {
      background: #f7ca00;
      border-color: #f2c200;
      box-shadow: 0 4px 14px rgba(247, 202, 0, 0.4);
      transform: translateY(-1px);
    }

    .btn-buy-saas {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
      color: #FFFFFF !important;
      font-weight: 800;
      font-size: 0.90rem;
      padding: 10px 16px;
      border-radius: 20px;
      box-shadow: 0 4px 14px rgba(12, 150, 156, 0.35);
      transition: all 0.2s ease;
    }
    .btn-buy-saas:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(12, 150, 156, 0.55);
    }

    .btn-copy-link {
      background: rgba(3, 23, 22, 0.9);
      border: 1px solid var(--border-teal);
      color: var(--text-muted);
      width: 42px;
      height: 42px;
      border-radius: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
      flex-shrink: 0;
    }
    .btn-copy-link:hover {
      color: #FFFFFF;
      border-color: var(--amazon-orange);
      background: rgba(255, 153, 0, 0.15);
    }

    /* Disclosure box */
    .disclosure-box {
      background: rgba(4, 36, 38, 0.5);
      border: 1px dashed var(--border-teal);
      border-radius: 14px;
      padding: 18px 24px;
      font-size: 0.80rem;
      color: #94A3B8;
      line-height: 1.6;
      margin-bottom: 60px;
    }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: #042426;
      border: 1px solid var(--amazon-orange);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      color: #FFFFFF;
      padding: 14px 22px;
      border-radius: 12px;
      font-size: 0.90rem;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }
    .toast.show {
      transform: translateY(0);
      opacity: 1;
      pointer-events: auto;
    }

    /* Footer */
    footer {
      background: #020f0e;
      border-top: 1px solid var(--border-teal);
      padding: 60px 0 30px;
      margin-top: auto;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 36px;
      margin-bottom: 40px;
    }

    .footer-col h4 {
      font-family: 'Bricolage Grotesque', sans-serif;
      font-size: 1.1rem;
      color: #FFFFFF;
      margin-bottom: 16px;
    }
    .footer-col ul { list-style: none; }
    .footer-col li { margin-bottom: 8px; }
    .footer-col a { color: var(--text-muted); font-size: 0.88rem; }
    .footer-col a:hover { color: var(--amazon-orange); }

    .footer-bottom {
      text-align: center;
      padding-top: 24px;
      border-top: 1px solid rgba(12, 150, 156, 0.15);
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    @media (max-width: 900px) {
      .nav-links { display: none; }
      .mobile-menu-btn { display: flex; }
    }

    @media (max-width: 768px) {
      .gear-grid { grid-template-columns: 1fr; }
      .trust-strip { gap: 10px; }
      .search-row { flex-direction: column; }
    }
  </style>
</head>
<body>

  <!-- Sticky Navbar -->
  <header>
    <div class="container nav-bar">
      <a href="/" class="logo-badge">
        <span class="logo-dot"></span>
        AI Toolkit Pro
      </a>
      <nav class="nav-links">
        <a href="/" class="nav-link">Home</a>
        <a href="/source-codes" class="nav-link">⚡ 33+ Source Codes</a>
        <a href="/creator-gear" class="nav-link active">🛒 Amazon Store</a>
        <a href="https://shorts-output.vercel.app/" target="_blank" rel="noopener" class="nav-link">🎬 Shorts Hub ↗</a>
        <a href="/free-claude-opus-5" class="nav-link">🧠 Claude Studio</a>
        <a href="/#contact" class="nav-link">Contact</a>
      </nav>
      <div style="display: flex; gap: 12px; align-items: center;">
        <a href="https://wa.me/916900077102" target="_blank" rel="noopener" class="btn-header-cta">
          💬 WhatsApp
        </a>
        <button class="mobile-menu-btn" onclick="toggleMobileDrawer()" aria-label="Open menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Amazon Subnav Strip -->
  <div class="amazon-subnav">
    <div class="container amazon-subnav-inner">
      <div class="deliver-pill">
        <svg width="15" height="15" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
        </svg>
        <span>Delivering to <strong>India & Worldwide</strong> with Amazon Prime</span>
      </div>
      <div class="storefront-verified">
        ✔ OFFICIAL AMAZON ASSOCIATES STOREFRONT • STORE ID: aitoolkitpro-21
      </div>
    </div>
  </div>

  <!-- Mobile Drawer -->
  <div id="mobile-drawer" class="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="logo-badge" style="font-size: 1.15rem;">
        <span class="logo-dot"></span> AI Toolkit Pro
      </div>
      <button class="mobile-drawer-close" onclick="toggleMobileDrawer()" aria-label="Close menu">✕</button>
    </div>
    <div class="mobile-drawer-links">
      <a href="/">Home</a>
      <a href="/source-codes">⚡ 33+ Source Codes</a>
      <a href="/creator-gear" class="active">🛒 Amazon Creator Store</a>
      <a href="https://shorts-output.vercel.app/" target="_blank" rel="noopener">🎬 Shorts Hub ↗</a>
      <a href="/free-claude-opus-5">🧠 Claude Studio</a>
      <a href="/#contact">Contact & Hire</a>
    </div>
    <div style="margin-top: auto; padding-top: 16px; border-top: 1px solid rgba(12,150,156,0.2);">
      <a href="https://wa.me/916900077102" target="_blank" rel="noopener" class="btn-header-cta" style="width: 100%; justify-content: center; padding: 12px;">
        💬 WhatsApp (+91 69000 77102)
      </a>
    </div>
  </div>
  <div id="mobile-drawer-backdrop" class="mobile-drawer-backdrop" onclick="toggleMobileDrawer()"></div>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="amazon-hero-pill">
        🛒 OFFICIAL AMAZON INFLUENCER & ASSOCIATES STOREFRONT
      </div>
      <h1 class="hero-title">
        The Creator & Studio <span>Hardware Store</span>
      </h1>
      <p class="hero-sub">
        Explore 70+ battle-tested rigs curated for 3D animators, YouTubers, livestreamers, and AI developers. Real authentic photos, live festive discounts, and Prime 1-day delivery across India.
      </p>

      <div class="trust-strip">
        <div class="trust-badge-pill">
          <span>📦</span> <strong>70 Verified Rigs</strong>
        </div>
        <div class="trust-badge-pill">
          <span>🚚</span> <strong>Amazon Prime 1-Day Express</strong>
        </div>
        <div class="trust-badge-pill">
          <span>🛡️</span> <strong>100% Genuine Brand Warranty</strong>
        </div>
        <div class="trust-badge-pill">
          <span>🏷️</span> <strong>Up to 75% Off Live Deals</strong>
        </div>
      </div>
    </div>
  </section>

  <!-- Filter & Search Controls -->
  <section class="container">
    <div class="controls-wrapper">
      <div class="search-row">
        <div class="search-input-box">
          <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <input type="text" id="searchInput" placeholder="Search Amazon rigs: Shure SM7B, Sony ZV-E10, DJI Pocket 3, RTX 4070, Fifine, Green Soul..." oninput="handleSearch()">
        </div>
        <select class="sort-select" id="sortSelect" onchange="handleSort()">
          <option value="featured">Featured Creator Picks</option>
          <option value="price-low">Price: Low to High</option>
          <option value="price-high">Price: High to Low</option>
          <option value="discount">Highest Discount %</option>
        </select>
      </div>

      <div class="category-tabs" id="categoryTabs">
        <button class="tab-btn active" data-cat="all" onclick="filterCategory('all', this)">⚡ All Gear (70)</button>
        <button class="tab-btn" data-cat="audio" onclick="filterCategory('audio', this)">🎙️ Studio Microphones & Audio (19)</button>
        <button class="tab-btn" data-cat="video" onclick="filterCategory('video', this)">📹 4K Cameras & Studio Lighting (19)</button>
        <button class="tab-btn" data-cat="hardware" onclick="filterCategory('hardware', this)">💻 Workstations & GPUs (15)</button>
        <button class="tab-btn" data-cat="workspace" onclick="filterCategory('workspace', this)">🪑 Standing Desks & Ergonomics (10)</button>
        <button class="tab-btn" data-cat="saas" onclick="filterCategory('saas', this)">🌐 High-Yield SaaS & Cloud (7)</button>
      </div>
    </div>

    <!-- Product Grid -->
    <div class="gear-grid" id="gearGrid">
      {PRODUCT_CARDS_HTML}
    </div>

    <!-- Disclosure & Compliance -->
    <div class="disclosure-box">
      <strong>Amazon Associate & Creator Earnings Disclosure:</strong><br>
      AI Toolkit Pro is a participant in the Amazon Services LLC Associates Program and Amazon.in Associates Central, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.in. Product prices and availability are accurate as of the date/time indicated and are subject to change. Any price and availability information displayed on Amazon.in at the time of purchase will apply to the purchase of this product. Tracking ID: <strong>aitoolkitpro-21</strong>.
    </div>
  </section>

  <!-- Toast Notification -->
  <div class="toast" id="toast">
    <span>✓ Link copied with tag <strong>aitoolkitpro-21</strong>!</span>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>AI Toolkit Pro</h4>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
            Empowering developers, video editors, and 3D animators with production-grade AI source codes, automation agents, and verified studio gear.
          </p>
        </div>
        <div class="footer-col">
          <h4>Store Categories</h4>
          <ul>
            <li><a href="javascript:void(0)" onclick="filterCategory('audio')">Studio Microphones</a></li>
            <li><a href="javascript:void(0)" onclick="filterCategory('video')">4K Cameras & Lighting</a></li>
            <li><a href="javascript:void(0)" onclick="filterCategory('hardware')">GPUs & 3D Workstations</a></li>
            <li><a href="javascript:void(0)" onclick="filterCategory('workspace')">Ergonomic Desks & Chairs</a></li>
            <li><a href="javascript:void(0)" onclick="filterCategory('saas')">Cloud & AI SaaS Platforms</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Our Channels & Media</h4>
          <ul>
            <li><a href="https://www.youtube.com/@WhatHappensNext-3D" target="_blank" rel="noopener">@WhatHappensNext-3D (YouTube)</a></li>
            <li><a href="https://www.youtube.com/@WonderWhysOfficial" target="_blank" rel="noopener">@WonderWhysOfficial (YouTube)</a></li>
            <li><a href="https://www.youtube.com/@aitoolkitpro-o5k" target="_blank" rel="noopener">@aitoolkitpro-o5k (YouTube)</a></li>
            <li><a href="https://shorts-output.vercel.app/" target="_blank" rel="noopener">Shorts Production Hub Live</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Legal & Contact</h4>
          <ul>
            <li><a href="/privacy-policy">Privacy Policy</a></li>
            <li><a href="/terms">Terms of Service</a></li>
            <li><a href="/contact">Support Desk</a></li>
            <li><a href="https://wa.me/916900077102" target="_blank" rel="noopener">WhatsApp Support: +91 69000 77102</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        © 2026 AI Toolkit Pro. Founder: Bishal (Shabbir Ahmed). All Rights Reserved. Amazon Associate Tag: <strong>aitoolkitpro-21</strong>.
      </div>
    </div>
  </footer>

  <!-- Interactive JavaScript Logic -->
  <script>
    function toggleMobileDrawer() {
      const drawer = document.getElementById('mobile-drawer');
      const backdrop = document.getElementById('mobile-drawer-backdrop');
      if (drawer && backdrop) {
        drawer.classList.toggle('open');
        backdrop.classList.toggle('open');
      }
    }

    function copyAffiliateLink(url) {
      navigator.clipboard.writeText(url).then(() => {
        showToast("Affiliate link copied with tag aitoolkitpro-21!");
      }).catch(() => {
        prompt("Copy this link:", url);
      });
    }

    function showToast(msg) {
      const toast = document.getElementById("toast");
      toast.innerHTML = "<span>✓ " + msg + "</span>";
      toast.classList.add("show");
      setTimeout(() => { toast.classList.remove("show"); }, 3000);
    }

    function filterCategory(cat, btn) {
      if (btn) {
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
      } else {
        document.querySelectorAll(".tab-btn").forEach(b => {
          if (b.getAttribute("data-cat") === cat) b.classList.add("active");
          else b.classList.remove("active");
        });
        window.scrollTo({ top: 380, behavior: 'smooth' });
      }
      applyFilters();
    }

    function handleSearch() {
      applyFilters();
    }

    function handleSort() {
      const sortVal = document.getElementById("sortSelect").value;
      const grid = document.getElementById("gearGrid");
      const cards = Array.from(grid.querySelectorAll(".gear-card"));

      cards.sort((a, b) => {
        if (sortVal === "price-low" || sortVal === "price-high") {
          const getNum = (str) => {
            const clean = str.replace(/[^0-9]/g, '');
            return parseInt(clean, 10) || 0;
          };
          const pA = getNum(a.getAttribute("data-price"));
          const pB = getNum(b.getAttribute("data-price"));
          return sortVal === "price-low" ? (pA - pB) : (pB - pA);
        } else if (sortVal === "discount") {
          const getDisc = (card) => {
            const txt = card.querySelector(".discount-floating-pill")?.innerText || "";
            const num = txt.replace(/[^0-9]/g, '');
            return parseInt(num, 10) || 0;
          };
          return getDisc(b) - getDisc(a);
        } else {
          return (parseInt(a.getAttribute("data-index"), 10) || 0) - (parseInt(b.getAttribute("data-index"), 10) || 0);
        }
      });

      cards.forEach(card => grid.appendChild(card));
      applyFilters();
    }

    function applyFilters() {
      const query = document.getElementById("searchInput").value.toLowerCase().trim();
      const activeTab = document.querySelector(".tab-btn.active")?.getAttribute("data-cat") || "all";
      const cards = document.querySelectorAll(".gear-card");

      cards.forEach(card => {
        const cat = card.getAttribute("data-category");
        const title = card.getAttribute("data-title").toLowerCase();
        const brand = card.getAttribute("data-brand").toLowerCase();
        const specs = card.getAttribute("data-specs").toLowerCase();

        const matchesCat = (activeTab === "all" || cat === activeTab);
        const matchesQuery = !query || title.includes(query) || brand.includes(query) || specs.includes(query);

        if (matchesCat && matchesQuery) {
          card.style.display = "flex";
        } else {
          card.style.display = "none";
        }
      });
    }
  </script>
</body>
</html>
"""

def generate_card_html(p, index):
    slug = p["slug"]
    specs_li = "".join([f'<li class="card-spec-item">{s}</li>' for s in p["specs"]])
    specs_flat = " ".join(p["specs"])
    
    is_amazon = p["type"] == "amazon"
    
    # Check if authentic photo exists
    local_photo_path = f"/assets/products/{slug}.jpg"
    full_local = os.path.join("/Users/bishal/ai_toolkit_pro_web/assets/products", f"{slug}.jpg")
    if not os.path.exists(full_local):
        local_photo_path = f"/assets/gear/{slug}.png"

    # Updated URL with live Indian ASIN if in updates
    product_url = p["url"]
    if slug in ASIN_UPDATES:
        new_asin = ASIN_UPDATES[slug]
        product_url = f"https://www.amazon.in/dp/{new_asin}?tag=aitoolkitpro-21"

    # Amazon Badges
    badge_html = ""
    if index in [0, 2, 14, 26, 38]:
        badge_html = '<div class="badge-best-seller">#1 Best Seller</div>'
    elif index in [1, 5, 15, 28, 41]:
        badge_html = '<div class="badge-overall-pick">Overall Pick</div>'
    elif "OFF" in p["discount"] and int(re.search(r'\d+', p["discount"]).group(0) if re.search(r'\d+', p["discount"]) else 0) >= 25:
        badge_html = '<div class="badge-limited-deal">Limited time deal</div>'

    # Social Proof
    bought_counts = ["2K+", "1K+", "800+", "500+", "400+", "300+"]
    social_bought = f"{bought_counts[index % len(bought_counts)]} bought in past month" if is_amazon else "Over 10,000+ active creator users"

    # Rating display
    rating_num = "4.8"
    reviews_count = "12,410"
    if "★" in p["rating"]:
        parts = p["rating"].split("★")
        rating_num = parts[0].strip()
        reviews_count = parts[1].replace("(", "").replace(")", "").replace("Reviews", "").strip()

    stars_str = "★★★★★"

    # Price parsing
    price_clean = p["price"].replace("₹", "").strip()
    discount_val = p["discount"]

    # Delivery line
    delivery_line = """
      <div class="prime-delivery-tag">
        <span class="prime-logo-badge"><span class="prime-check">✔</span>prime</span>
        <span>FREE Delivery by <strong>Tomorrow, 2 PM</strong></span>
      </div>
      <div class="in-stock-line">In stock</div>
    """ if is_amazon else """
      <div class="prime-delivery-tag" style="color: #10b981;">
        <span>⚡ Instant Cloud Activation & Zero Setup Fee</span>
      </div>
      <div class="in-stock-line" style="color: #10b981;">Official Verified Partner Deal</div>
    """

    btn_html = f"""
      <a href="{product_url}" target="_blank" rel="sponsored noopener" class="btn-amazon-primary">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/>
        </svg>
        Buy on Amazon India ↗
      </a>
    """ if is_amazon else f"""
      <a href="{product_url}" target="_blank" rel="sponsored noopener" class="btn-buy-saas">
        Claim Creator Deal ↗
      </a>
    """

    return f"""
      <article class="gear-card" 
               data-index="{index}"
               data-category="{p['category']}" 
               data-title="{p['title']}" 
               data-brand="{p['brand']}" 
               data-specs="{specs_flat}"
               data-price="{p['price']}">
        
        <!-- Clean White Studio Photo Container -->
        <div class="product-photo-card">
          {badge_html}
          <div class="discount-floating-pill">{discount_val}</div>
          <img class="product-real-img" src="{local_photo_path}" alt="{p['title']}" loading="lazy">
        </div>

        <div class="card-body">
          <div class="brand-store-link">{p['brand']}</div>
          <h3 class="card-title">{p['title']}</h3>

          <!-- Star Rating -->
          <div class="amazon-rating-row">
            <span class="amazon-stars">{stars_str}</span>
            <span class="amazon-rating-score">{rating_num}</span>
            <span class="amazon-rating-count">({reviews_count})</span>
          </div>

          <div class="social-proof-line">{social_bought}</div>

          <!-- Amazon Pricing -->
          <div class="amazon-price-row">
            <span class="amazon-discount-rate">-{discount_val.replace(' OFF', '')}</span>
            <div class="amazon-price-main">
              <span class="amazon-currency">₹</span>{price_clean}
            </div>
          </div>
          <div class="amazon-mrp">M.R.P.: <span>{p['mrp']}</span></div>

          {delivery_line}

          <ul class="card-specs-list">
            {specs_li}
          </ul>

          <div class="card-actions">
            {btn_html}
            <button type="button" class="btn-copy-link" title="Copy Affiliate Link" onclick="copyAffiliateLink('{product_url}')">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
              </svg>
            </button>
          </div>
        </div>
      </article>
    """

def main():
    print(f"Building Amazon-style creator-gear.html with {len(GEAR_PRODUCTS)} products...")
    cards_html = "\n".join([generate_card_html(p, idx) for idx, p in enumerate(GEAR_PRODUCTS)])
    
    full_html = HTML_TEMPLATE.replace("{PRODUCT_CARDS_HTML}", cards_html)
    
    output_path = "/Users/bishal/ai_toolkit_pro_web/creator-gear.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Successfully generated Amazon-style {output_path} ({len(full_html)} bytes)")

if __name__ == "__main__":
    main()
