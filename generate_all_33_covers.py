import os
import sys
sys.path.append('/Users/bishal/ai_toolkit_pro_web')
import generate_product_images as gen

PRODUCTS_CONFIG = [
    {
        "id_slug": "ultimate-30-saas-ai-vault",
        "short_title": "The Ultimate 30+ SaaS & AI Mega Vault",
        "tagline": "Lifetime Agency Pass • 30+ Production Web Apps, Micro-SaaS & AI Bots",
        "badge_txt": "LIFETIME MEGA VAULT",
        "accent": (245, 158, 11),
        "url_mock": "https://vault.chementor.in/all-access",
        "menu_items": ["All Apps", "Source ZIPs", "Licenses", "Setup Guides"],
        "stats": [("PORTFOLIO", "30+ SaaS Apps", (245, 158, 11)), ("LICENSE", "Commercial Pass", (12, 150, 156)), ("UPDATES", "Lifetime Access", (34, 197, 94))],
        "ui_kind": "vault"
    },
    {
        "id_slug": "all-ai-agency-bundle",
        "short_title": "Complete AI Agency & Automation Bundle",
        "tagline": "All 4 Production AI Apps: WhatsApp Bot + AI Studio + Shorts + Review",
        "badge_txt": "AGENCY 4-IN-1 PACK",
        "accent": (14, 165, 233),
        "url_mock": "https://agency.ai/suite-v4",
        "menu_items": ["AI Apps", "Model Config", "Webhooks", "Clients"],
        "stats": [("AI APPS", "4 Complete Tools", (14, 165, 233)), ("MODELS", "Claude + GPT-4o", (168, 85, 247)), ("RIGHTS", "100% White-Label", (34, 197, 94))],
        "ui_kind": "code"
    },
    {
        "id_slug": "all-7-saas-bundle",
        "short_title": "Complete 7-in-1 PHP SaaS Bundle",
        "tagline": "All 7 PHP SaaS Systems: Dynamic QR, vCard, WhatsApp Store & Loyalty",
        "badge_txt": "7 FULL SAAS APPS",
        "accent": (16, 185, 129),
        "url_mock": "https://saas-suite.chementor.in",
        "menu_items": ["7 Apps", "Admin Central", "Databases", "Gateways"],
        "stats": [("SAAS SUITES", "7 Full Systems", (16, 185, 129)), ("STACK", "PHP 8.2 + MySQL", (56, 189, 248)), ("DEPLOY", "cPanel 1-Click", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["SAAS PRODUCT", "MODULE", "OWNER PANEL", "CLIENT PORTAL"],
        "table_rows": [
            ("Dynamic QR SaaS", "PHP 8.2", "SUPERADMIN", "LIVE READY"),
            ("WhatsApp Store Maker", "PHP 8.2", "SUPERADMIN", "LIVE READY")
        ]
    },
    {
        "id_slug": "whatsapp-ai-lead-agent",
        "short_title": "WhatsApp AI Lead & Booking Agent",
        "tagline": "Meta Cloud API • 24/7 Automated Bookings & Google Sheets CRM",
        "badge_txt": "TOP SELLER AI",
        "accent": (34, 197, 94),
        "url_mock": "https://api.meta.com/v19.0/whatsapp-agent",
        "menu_items": ["Inbox", "Appointments", "Leads CRM", "Webhook"],
        "stats": [("LATENCY", "0.42s Meta API", (34, 197, 94)), ("SYNC", "Google Sheets", (12, 150, 156)), ("LLM", "Gemini / GPT-4o", (234, 179, 8))],
        "ui_kind": "chat",
        "chat_user": "Hi! Need a dental appointment for tomorrow 4 PM",
        "chat_bot": "Dr. Sharma has a slot available at 4:30 PM. Confirmed!"
    },
    {
        "id_slug": "ai-studio-pro",
        "short_title": "AI Studio Pro: Multi-Model SaaS Web App",
        "tagline": "Self-Hosted ChatGPT & Claude Alternative • 35+ System Personas",
        "badge_txt": "ENTERPRISE AI SAAS",
        "accent": (12, 150, 156),
        "url_mock": "https://ai-studio.app/workspace",
        "menu_items": ["Models", "Personas", "API Keys", "Billing"],
        "stats": [("MODELS", "Claude + GPT + Gemini", (12, 150, 156)), ("PROMPTS", "35+ Personas", (168, 85, 247)), ("SAVINGS", "Zero Subscriptions", (34, 197, 94))],
        "ui_kind": "code"
    },
    {
        "id_slug": "viral-shorts-ai-engine",
        "short_title": "Viral Shorts & Reels AI Video Engine",
        "tagline": "Batch 1080x1920 MP4 Video Generator • Edge-TTS & Dynamic Captions",
        "badge_txt": "PASSIVE TRAFFIC BOT",
        "accent": (168, 85, 247),
        "url_mock": "https://engine.shorts.ai/render",
        "menu_items": ["Hook Generator", "Batch Render", "Voiceovers", "Captions"],
        "stats": [("RESOLUTION", "1080x1920 MP4", (168, 85, 247)), ("HOOKS", "21 Proven Formulas", (234, 179, 8)), ("VOICE", "Edge-TTS Neural", (34, 197, 94))],
        "ui_kind": "table",
        "table_cols": ["VIDEO TITLE", "DURATION", "HOOK FORMULA", "RENDER STATUS"],
        "table_rows": [
            ("5 Secret AI Websites", "48s (1080x1920)", "Curiosity Gap", "100% COMPLETE"),
            ("How Indipreneurs Win", "54s (1080x1920)", "Contrarian Truth", "100% COMPLETE")
        ]
    },
    {
        "id_slug": "ai-review-php",
        "short_title": "AI Google Review & Feedback Filter",
        "tagline": "Boost 5-Star Google Reviews • Route Negative Feedback Privately",
        "badge_txt": "REPUTATION BOOSTER",
        "accent": (234, 179, 8),
        "url_mock": "https://review.chementor.in/biz/star",
        "menu_items": ["Rating Funnel", "Feedback Log", "Google Sync", "QR Stands"],
        "stats": [("RATING", "4.9★ Filter", (234, 179, 8)), ("AI DRAFT", "Instant Reply", (12, 150, 156)), ("STACK", "PHP 8.2 + MySQL", (34, 197, 94))],
        "ui_kind": "table",
        "table_cols": ["CUSTOMER", "SENTIMENT", "ROUTING DESTINATION", "STATUS"],
        "table_rows": [
            ("Vikas Malhotra", "★★★★★ (5 Star)", "Google Maps Public Page", "PUBLISHED"),
            ("Ananya Sen", "★★☆☆☆ (2 Star)", "Private Owner Inbox (Safe)", "RESOLVED")
        ]
    },
    {
        "id_slug": "dynamic-qr-php",
        "short_title": "Dynamic QR Maker & Scan Analytics SaaS",
        "tagline": "Editable Target URLs Without Reprinting • Geo & Device Analytics",
        "badge_txt": "ESSENTIAL SAAS",
        "accent": (56, 189, 248),
        "url_mock": "https://qr.chementor.in/dashboard",
        "menu_items": ["QR Codes", "Link Editor", "Geo Analytics", "API"],
        "stats": [("SCANS", "14,820 Total", (56, 189, 248)), ("TARGET", "Dynamic / Editable", (34, 197, 94)), ("FORMATS", "SVG, PNG, EPS", (234, 179, 8))],
        "ui_kind": "qr",
        "qr_target": "DYNAMIC DESTINATION: https://store.link/promo-2026"
    },
    {
        "id_slug": "ecomm-whatsapp-php",
        "short_title": "Ecomm WhatsApp Store Maker SaaS",
        "tagline": "Convert Any Catalog into a 1-Click WhatsApp Direct Order Machine",
        "badge_txt": "COMMERCE SAAS",
        "accent": (34, 197, 94),
        "url_mock": "https://store.shop/wa-catalog",
        "menu_items": ["Products", "Orders", "Categories", "Payment QR"],
        "stats": [("CART", "1-Click WhatsApp", (34, 197, 94)), ("COMMISSION", "0% Forever", (12, 150, 156)), ("GATEWAY", "Cash / UPI Direct", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["ORDER ID", "ITEMS ORDERED", "TOTAL", "STATUS"],
        "table_rows": [
            ("WA-#4091", "Noise-Cancelling Earbuds", "₹1,899", "DISPATCHED"),
            ("WA-#4092", "Smartwatch Ultra Black", "₹2,499", "PAID via UPI")
        ]
    },
    {
        "id_slug": "vcard-php",
        "short_title": "Digital vCard & NFC Networking SaaS",
        "tagline": "1-Tap Contact Save (.VCF) • NFC Business Card & QR Builder",
        "badge_txt": "NETWORKING SAAS",
        "accent": (99, 102, 241),
        "url_mock": "https://vcard.bio/johndoe",
        "menu_items": ["vCard Editor", "NFC Link", "Social Links", "Analytics"],
        "stats": [("FORMAT", ".VCF Phone Contact", (99, 102, 241)), ("HARDWARE", "NFC + QR Ready", (34, 197, 94)), ("ANALYTICS", "Click Tracking", (234, 179, 8))],
        "ui_kind": "qr",
        "qr_target": "1-TAP SAVE CONTACT: vCard 3.0 Mobile (.VCF)"
    },
    {
        "id_slug": "qr-menu-php",
        "short_title": "Digital Restaurant QR Menu SaaS",
        "tagline": "Contactless Food Menu • Veg / Non-Veg Badges & Dietary Filters",
        "badge_txt": "HOSPITALITY SAAS",
        "accent": (249, 115, 22),
        "url_mock": "https://menu.cafe/tables/scan",
        "menu_items": ["Menu Dishes", "Categories", "Table QRs", "Pricing"],
        "stats": [("PRINTING", "Zero Re-print Costs", (249, 115, 22)), ("FILTERS", "Veg / Non-Veg / Vegan", (34, 197, 94)), ("SPEED", "Instant Mobile Load", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["DISH NAME", "DIETARY", "PRICE", "AVAILABILITY"],
        "table_rows": [
            ("Paneer Butter Masala", "● Veg (Pure)", "₹280", "IN STOCK"),
            ("Tandoori Chicken Tikka", "▲ Non-Veg", "₹360", "IN STOCK")
        ]
    },
    {
        "id_slug": "one-link-qr-php",
        "short_title": "One Link QR & Multi-Link Hub",
        "tagline": "All Your Links & UPI QR on a Single Mobile Micro-Site",
        "badge_txt": "BIO LINK SAAS",
        "accent": (147, 51, 234),
        "url_mock": "https://onelink.qr/creator",
        "menu_items": ["Link Blocks", "UPI QR Block", "Themes", "Clicks"],
        "stats": [("BLOCKS", "Unlimited Links", (147, 51, 234)), ("PAYMENTS", "Integrated UPI QR", (34, 197, 94)), ("MOBILE", "Responsive 100%", (56, 189, 248))],
        "ui_kind": "qr",
        "qr_target": "HUB TARGET: Instagram + YouTube + UPI QR"
    },
    {
        "id_slug": "loyalty-card-php",
        "short_title": "Digital Loyalty Card & Stamp Tracker",
        "tagline": "Replace Paper Cards • 10-Stamp Rewards with Merchant PIN",
        "badge_txt": "CUSTOMER RETENTION",
        "accent": (244, 63, 94),
        "url_mock": "https://loyalty.cafe/stamp-card",
        "menu_items": ["Stamp Cards", "Customers", "PIN Security", "Rewards"],
        "stats": [("STAMPS", "10-Stamp Rewards", (244, 63, 94)), ("FRAUD DEFENSE", "Merchant PIN Lock", (34, 197, 94)), ("REPEAT RATE", "+42% Visits", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["CUSTOMER PHONE", "STAMPS EARNED", "REWARD PROGRESS", "LAST VISIT"],
        "table_rows": [
            ("+91 98201-XXXX", "★★★★★★★☆☆☆ (7/10)", "Free Coffee on 10th", "Today"),
            ("+91 98712-XXXX", "★★★★★★★★★★ (10/10)", "REWARD UNLOCKED", "Yesterday")
        ]
    },
    {
        "id_slug": "gmaps-lead-hunter-ai",
        "short_title": "Google Maps B2B Lead Scraper & AI Pitch",
        "tagline": "Extract Business Phone, Email & Auto-Draft Cold Pitch Proposals",
        "badge_txt": "TOP SELLER B2B",
        "accent": (239, 68, 68),
        "url_mock": "https://hunter.leads.ai/scraper",
        "menu_items": ["Map Search", "Lead Pipeline", "AI Pitcher", "CSV Export"],
        "stats": [("API COST", "₹0 No Cloud API", (239, 68, 68)), ("DATA", "Phone, Site & Ratings", (34, 197, 94)), ("PITCH", "Personalized AI Email", (12, 150, 156))],
        "ui_kind": "table",
        "table_cols": ["BUSINESS NAME", "PHONE", "RATING", "AI PITCH READY"],
        "table_rows": [
            ("Apex Fitness Studio", "+91 98110-XXXX", "4.8★ (120 reviews)", "PITCH GENERATED"),
            ("City Dental Clinic", "+91 98334-XXXX", "4.6★ (88 reviews)", "PITCH GENERATED")
        ]
    },
    {
        "id_slug": "ai-resume-ats-optimizer",
        "short_title": "AI Resume & ATS Score Optimizer",
        "tagline": "Score Resumes Against Job Descriptions • 0-100 Score & Keyword Gap",
        "badge_txt": "JOB SEEKER HOT",
        "accent": (16, 185, 129),
        "url_mock": "https://resume.ai/ats-analyzer",
        "menu_items": ["ATS Score", "Keyword Gap", "Bullet Polish", "PDF Export"],
        "stats": [("ATS SCORE", "96% High Match", (16, 185, 129)), ("KEYWORDS", "14 Missing Identified", (234, 179, 8)), ("FORMAT", "ATS-Friendly PDF", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["SKILL / KEYWORD", "JOB REQUIREMENT", "STATUS IN RESUME", "SUGGESTION"],
        "table_rows": [
            ("Docker & Kubernetes", "Required (Senior)", "MATCH FOUND", "Highlighted in Exp"),
            ("FastAPI Microservices", "Preferred", "MISSING", "Add bullet to Project #2")
        ]
    },
    {
        "id_slug": "ai-voice-meeting-summarizer",
        "short_title": "AI Audio Transcriber & Meeting Summarizer",
        "tagline": "Transcribe Voice Audio & Generate Action Items and Key Takeaways",
        "badge_txt": "PRODUCTIVITY PRO",
        "accent": (14, 165, 233),
        "url_mock": "https://voice.ai/summarizer",
        "menu_items": ["Live Mic", "Audio Upload", "Action Items", "Export"],
        "stats": [("ACCURACY", "99% Whisper AI", (14, 165, 233)), ("AUDIO FORMATS", "MP3, WAV, M4A", (34, 197, 94)), ("EXTRACTION", "Action Items & Timestamps", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["TIMESTAMP", "SPEAKER", "AI ACTION ITEM / DECISION", "OWNER"],
        "table_rows": [
            ("08:14", "Product Manager", "Deploy dark-teal theme to production", "Bishal"),
            ("19:40", "Lead Architect", "Benchmark SQLite query response time", "Backend Team")
        ]
    },
    {
        "id_slug": "ai-pdf-research-notebook",
        "short_title": "AI PDF Research Notebook (NotebookLM Clone)",
        "tagline": "Chat with Textbooks & Research PDFs with Verifiable Page Citations",
        "badge_txt": "HOT EDTECH AI",
        "accent": (6, 182, 212),
        "url_mock": "https://notebook.ai/research-doc",
        "menu_items": ["PDF Library", "Semantic Search", "Citations", "Study Notes"],
        "stats": [("CAPACITY", "500+ Page PDFs", (6, 182, 212)), ("CITATIONS", "Page & Paragraph Pins", (34, 197, 94)), ("FORMAT", "PDF, DOCX, TXT", (234, 179, 8))],
        "ui_kind": "chat",
        "chat_user": "What is the primary conclusion in chapter 4?",
        "chat_bot": "According to Page 84 (Para 2), latency was reduced by 64%."
    },
    {
        "id_slug": "ai-social-carousel-maker",
        "short_title": "AI Social Media Post & Carousel Maker",
        "tagline": "Auto-Generate 10-Slide LinkedIn & Instagram Carousels in Seconds",
        "badge_txt": "CREATOR ENGINE",
        "accent": (217, 70, 239),
        "url_mock": "https://carousel.creator.ai",
        "menu_items": ["Hook Generator", "Slide Designer", "Brand Fonts", "Export"],
        "stats": [("SLIDES", "5-10 Slides Auto", (217, 70, 239)), ("DIMENSIONS", "1080x1350 Pro", (34, 197, 94)), ("EXPORT", "PNG & PDF Ready", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["SLIDE #", "HEADLINE HOOK", "SUBTITLE / COPY", "DESIGN THEME"],
        "table_rows": [
            ("Slide 1", "7 AI Tools That Feel Illegal", "Save 15 hours every week", "Dark Neon Minimal"),
            ("Slide 2", "#1: Self-Hosted Cloud Studio", "Deploy Claude 3.5 on your server", "Split Mockup")
        ]
    },
    {
        "id_slug": "ai-seo-article-writer-schema",
        "short_title": "AI SEO Article & FAQ Schema Generator",
        "tagline": "Write 2,500+ Word Ranking Guides with H2/H3 & JSON-LD FAQ Schema",
        "badge_txt": "RANK #1 GOOGLE",
        "accent": (16, 185, 129),
        "url_mock": "https://writer.seo.ai/article-builder",
        "menu_items": ["Keyword SERP", "H1/H2 Outline", "Article Draft", "JSON-LD"],
        "stats": [("WORD COUNT", "2,500+ In-Depth", (16, 185, 129)), ("SCHEMA", "JSON-LD FAQ Rich", (34, 197, 94)), ("OPTIMIZATION", "Google EEAT Score 96", (234, 179, 8))],
        "ui_kind": "code"
    },
    {
        "id_slug": "clinic-appointment-prescription-saas",
        "short_title": "Clinic Patient Appointment & Digital Rx SaaS",
        "tagline": "Online Token Booking Calendar, Doctor Desk & Printable Rx Generator",
        "badge_txt": "HEALTHCARE SAAS",
        "accent": (13, 148, 136),
        "url_mock": "https://clinic.care/doctor-portal",
        "menu_items": ["Today's Queue", "Appointments", "Digital Rx", "Billing"],
        "stats": [("TOKENS", "Real-Time Queue", (13, 148, 136)), ("PRESCRIPTION", "Printable Digital Rx", (34, 197, 94)), ("ALERTS", "WhatsApp & SMS", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["TOKEN #", "PATIENT NAME", "SYMPTOMS / VISIT", "STATUS"],
        "table_rows": [
            ("Token #08", "Rohan Verma (Age 32)", "Fever & General Consultation", "IN CLINIC (NOW)"),
            ("Token #09", "Meera Sen (Age 28)", "Follow-up Dental Check", "NEXT (11:15 AM)")
        ]
    },
    {
        "id_slug": "restaurant-qr-ordering-kot",
        "short_title": "Restaurant QR Ordering & Kitchen Display (KOT)",
        "tagline": "Dine-In Table QR Ordering • Real-Time Kitchen Order Ticket (KOT)",
        "badge_txt": "RESTAURANT PRO",
        "accent": (245, 158, 11),
        "url_mock": "https://pos.bistro.in/kot-live",
        "menu_items": ["Table Orders", "Live KOT", "Food Menu", "UPI Settle"],
        "stats": [("TABLE QRS", "Dynamic Table QRs", (245, 158, 11)), ("KOT SPEED", "< 2s to Kitchen", (34, 197, 94)), ("PAYMENTS", "Table UPI QR", (12, 150, 156))],
        "ui_kind": "table",
        "table_cols": ["TABLE #", "KOT ITEMS", "ELAPSED", "STATUS"],
        "table_rows": [
            ("Table 4", "Butter Chicken x1, Garlic Naan x3", "04:12 mins", "PREPARING"),
            ("Table 7", "Crispy Corn x1, Virgin Mojito x2", "01:30 mins", "ORDER SENT")
        ]
    },
    {
        "id_slug": "gym-fitness-membership-tracker",
        "short_title": "Gym & Fitness Studio Membership & Fee Tracker",
        "tagline": "Member Attendance Punch, Due Fee WhatsApp Alerts & Trainer Roster",
        "badge_txt": "FITNESS SAAS",
        "accent": (132, 204, 22),
        "url_mock": "https://gym.fit/member-desk",
        "menu_items": ["Members", "Attendance", "Fee Alerts", "Plans"],
        "stats": [("MEMBERS", "Active 340 Members", (132, 204, 22)), ("EXPIRY ALERTS", "WhatsApp Auto-Sent", (34, 197, 94)), ("ATTENDANCE", "QR / Bio Punch", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["MEMBER NAME", "MEMBERSHIP PLAN", "EXPIRATION", "FEE STATUS"],
        "table_rows": [
            ("Karan Singhania", "12-Month Pro Annual", "12 Days Left", "DUE REMINDER SENT"),
            ("Aditya Roy", "6-Month Muscle Gain", "84 Days Left", "PAID IN FULL")
        ]
    },
    {
        "id_slug": "real-estate-property-lead-portal",
        "short_title": "Real Estate Property & WhatsApp Lead Portal",
        "tagline": "Luxury Property Showcase Layout • Filter by City, BHK & Budget",
        "badge_txt": "HIGH TICKET B2B",
        "accent": (217, 119, 6),
        "url_mock": "https://estate.luxury/properties",
        "menu_items": ["Properties", "BHK Filters", "WhatsApp Inquiries", "Brochures"],
        "stats": [("SHOWCASE", "Villas & Apartments", (217, 119, 6)), ("LEADS", "Instant WhatsApp Click", (34, 197, 94)), ("SEARCH", "City, Budget & BHK", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["PROPERTY TITLE", "LOCATION", "PRICE / BUDGET", "BUYER INQUIRIES"],
        "table_rows": [
            ("The Skyline Penthouse 4BHK", "Bandra West, Mumbai", "₹4.85 Crore", "18 WhatsApp Leads"),
            ("Emerald Garden Villa 3BHK", "Whitefield, Bangalore", "₹2.20 Crore", "29 WhatsApp Leads")
        ]
    },
    {
        "id_slug": "salon-spa-booking-system",
        "short_title": "Salon & Luxury Spa Appointment Booking",
        "tagline": "Service Catalog, Stylist Roster, Slot Booking & Client History",
        "badge_txt": "BEAUTY SAAS",
        "accent": (244, 63, 94),
        "url_mock": "https://spa.luxe/bookings",
        "menu_items": ["Services", "Stylists", "Calendar", "Reminders"],
        "stats": [("SERVICES", "Hair, Facial & Spa", (244, 63, 94)), ("CALENDAR", "Live Stylist Slots", (34, 197, 94)), ("NOTIFICATIONS", "WhatsApp Auto-Confirm", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["CLIENT NAME", "TREATMENT SERVICE", "STYLIST", "SLOT TIME"],
        "table_rows": [
            ("Kavita Rao", "Hydra Glow Facial (60m)", "Sana (Senior)", "Today 03:00 PM"),
            ("Sneha Kapoor", "Keratin Hair Spa", "Alex (Master)", "Today 04:30 PM")
        ]
    },
    {
        "id_slug": "whatsapp-bulk-broadcast-tool",
        "short_title": "WhatsApp Bulk Outreach & Broadcast Tool",
        "tagline": "Personalized Outreach Assistant • CSV Contact Upload & Safe Delays",
        "badge_txt": "MARKETING B2B",
        "accent": (34, 197, 94),
        "url_mock": "https://broadcast.wa/campaign",
        "menu_items": ["Campaigns", "CSV Contacts", "Tag Merging", "Safe Delays"],
        "stats": [("DISPATCH", "500+ Contacts Batch", (34, 197, 94)), ("SAFETY", "Random Anti-Ban Delays", (234, 179, 8)), ("TAGS", "{{name}} Dynamic Merge", (12, 150, 156))],
        "ui_kind": "table",
        "table_cols": ["CAMPAIGN NAME", "RECIPIENTS", "SUCCESS RATE", "PACING DELAY"],
        "table_rows": [
            ("Diwali Early Bird Offer", "450 / 450 Sent", "100% Delivered", "8s - 14s Random"),
            ("VIP Membership Renewal", "120 / 120 Sent", "100% Delivered", "10s - 18s Random")
        ]
    },
    {
        "id_slug": "invoice-quotation-generator-upi-qr",
        "short_title": "Invoice & Quotation Maker with Dynamic UPI QR",
        "tagline": "Professional GST Invoices with Scannable Dynamic UPI QR Code on PDF",
        "badge_txt": "ESSENTIAL FINTECH",
        "accent": (6, 182, 212),
        "url_mock": "https://invoice.biz/generator",
        "menu_items": ["New Invoice", "Clients", "Tax Settings", "UPI QR"],
        "stats": [("UPI QR", "Exact Bill Amount Pre-filled", (6, 182, 212)), ("FORMAT", "GST Ready PDF", (34, 197, 94)), ("DISPATCH", "Instant WhatsApp Share", (234, 179, 8))],
        "ui_kind": "qr",
        "qr_target": "UPI PAYMENT QR: Scan to pay exact bill ₹14,999"
    },
    {
        "id_slug": "bio-link-digital-vcard-builder",
        "short_title": "Bio Link & Digital Business Card Builder",
        "tagline": "Self-Hosted Linktree Alternative • Custom Themes, Social Icons & NFC",
        "badge_txt": "CREATOR SAAS",
        "accent": (139, 92, 246),
        "url_mock": "https://biolink.me/profile",
        "menu_items": ["Bio Buttons", "Themes", "Social Links", "Analytics"],
        "stats": [("PAGES", "Unlimited Bio Landing Pages", (139, 92, 246)), ("FEES", "Zero Monthly Charges", (34, 197, 94)), ("SHARING", "NFC + QR 1-Tap", (56, 189, 248))],
        "ui_kind": "qr",
        "qr_target": "BIO LINK: Portfolio + Shop + Social Links"
    },
    {
        "id_slug": "branded-url-shortener-analytics",
        "short_title": "Branded URL Shortener & Link Tracking Engine",
        "tagline": "Custom Domain Slugs, Dynamic QR Codes, Geo Tracking & Referrer Charts",
        "badge_txt": "MARKETING B2B",
        "accent": (59, 130, 246),
        "url_mock": "https://short.link/analytics",
        "menu_items": ["Links", "Custom Domains", "Geo Map", "Referrers"],
        "stats": [("CLICKS", "48,290 Tracked", (59, 130, 246)), ("DOMAINS", "Custom Branded Slugs", (34, 197, 94)), ("ANALYTICS", "Country, Device & OS", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["SHORT URL", "ORIGINAL DESTINATION", "CLICKS", "TOP COUNTRY"],
        "table_rows": [
            ("cds.to/ai-tools", "https://chementor.in/ai-catalog", "24,800 Clicks", "India (68%)"),
            ("cds.to/spring-sale", "https://chementor.in/deal", "18,400 Clicks", "USA (22%)")
        ]
    },
    {
        "id_slug": "client-design-feedback-proofing-tool",
        "short_title": "Client Design & Website Proofing Tool",
        "tagline": "Pinpoint Visual Feedback on Images & Live Web Pages • Version Slider",
        "badge_txt": "AGENCY ESSENTIAL",
        "accent": (245, 158, 11),
        "url_mock": "https://proof.design/mockup-v2",
        "menu_items": ["Mockups", "Version Slider", "Pin Comments", "Approvals"],
        "stats": [("COMMENTING", "Pinpoint Pixel Pins", (245, 158, 11)), ("VERSIONS", "Before / After Slider", (34, 197, 94)), ("SIGN-OFF", "1-Click Client Approval", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["PIN #", "COORDINATES", "CLIENT FEEDBACK COMMENT", "STATUS"],
        "table_rows": [
            ("Pin #01", "X: 420px, Y: 110px", "Make hero headline cyan to match palette", "RESOLVED"),
            ("Pin #02", "X: 980px, Y: 340px", "Increase button padding for mobile tap", "RESOLVED")
        ]
    },
    {
        "id_slug": "license-key-manager-api",
        "short_title": "Software License Key Manager & REST API",
        "tagline": "Bulk Key Generation, Domain Lock, Hardware UUID & Validation API",
        "badge_txt": "DEVELOPER SAAS",
        "accent": (16, 185, 129),
        "url_mock": "https://license.dev/api/v1",
        "menu_items": ["Keys", "Activations", "Domain Locks", "REST Endpoints"],
        "stats": [("SECURITY", "Domain & Machine UUID Lock", (16, 185, 129)), ("VALIDATION", "Sub-10ms REST API", (34, 197, 94)), ("GENERATION", "Bulk 10,000 Keys Batch", (234, 179, 8))],
        "ui_kind": "table",
        "table_cols": ["LICENSE KEY", "CLIENT DOMAIN", "ACTIVATED", "STATUS"],
        "table_rows": [
            ("LIC-PRO-8921-AF", "client-saas.com", "2026-10-31", "ACTIVE (VERIFIED)"),
            ("LIC-PRO-7832-BC", "agency-portal.io", "2026-10-30", "ACTIVE (VERIFIED)")
        ]
    },
    {
        "id_slug": "online-quiz-mock-exam-portal",
        "short_title": "Online Quiz & Mock Test Exam Portal (CBSE / JEE)",
        "tagline": "Timed Test Simulator • Negative Marking, Section Splitting & Rank Cards",
        "badge_txt": "EDTECH PRO",
        "accent": (79, 70, 229),
        "url_mock": "https://exam.test/jee-mock",
        "menu_items": ["Live Exam", "Questions", "Question Palette", "Scorecard"],
        "stats": [("TIMER", "Real-Time Countdown", (79, 70, 229)), ("MARKING", "Negative Marking Supported", (234, 179, 8)), ("SECTIONS", "Physics / Chem / Math", (34, 197, 94))],
        "ui_kind": "table",
        "table_cols": ["QUESTION #", "SECTION", "STATUS IN TEST", "TIMER"],
        "table_rows": [
            ("Question 14", "Section B (Physics)", "ANSWERED & SAVED", "44:10 mins left"),
            ("Question 15", "Section B (Chemistry)", "MARKED FOR REVIEW", "44:02 mins left")
        ]
    },
    {
        "id_slug": "batch-certificate-id-card-generator",
        "short_title": "Batch Digital Certificate & Event ID Card Maker",
        "tagline": "Generate 500+ PDF Certificates & ID Cards in Seconds from Excel/CSV",
        "badge_txt": "EVENT SAAS",
        "accent": (217, 119, 6),
        "url_mock": "https://cert.event/generator",
        "menu_items": ["Templates", "Excel Upload", "Variable Tags", "Batch Export"],
        "stats": [("BATCH SPEED", "500+ PDFs in Seconds", (217, 119, 6)), ("IMPORT", "Excel & CSV Support", (34, 197, 94)), ("OUTPUT", "High-Res Print Ready", (56, 189, 248))],
        "ui_kind": "table",
        "table_cols": ["RECIPIENT NAME", "EVENT / COURSE TITLE", "ISSUE DATE", "EXPORT STATUS"],
        "table_rows": [
            ("Dr. Rajesh Sengupta", "Mastering Agentic AI 2026", "31 Oct 2026", "PDF GENERATED"),
            ("Ananya Mukherjee", "Full-Stack SaaS Engineering", "31 Oct 2026", "PDF GENERATED")
        ]
    },
    {
        "id_slug": "customer-support-ticket-helpdesk",
        "short_title": "Self-Hosted Customer Support Ticket & Helpdesk",
        "tagline": "Customer Support Portal, Ticket Queues, Priority Badges & SLA Timers",
        "badge_txt": "CUSTOMER SUPPORT",
        "accent": (14, 165, 233),
        "url_mock": "https://support.desk/inbox",
        "menu_items": ["Open Tickets", "SLA Priority", "Assigned Agents", "Macros"],
        "stats": [("QUEUES", "Multi-Department Queues", (14, 165, 233)), ("SLA TIMERS", "Priority Countdown", (234, 179, 8)), ("ATTACHMENTS", "Screenshots & Logs", (34, 197, 94))],
        "ui_kind": "table",
        "table_cols": ["TICKET #", "SUBJECT / QUERY", "PRIORITY", "SLA STATUS"],
        "table_rows": [
            ("#1042", "Webhook payment verification callback", "URGENT", "12 mins left"),
            ("#1043", "Setup assistance for cPanel domain", "NORMAL", "2 hrs left")
        ]
    }
]

print(f"Generating graphics for {len(PRODUCTS_CONFIG)} products...")
for idx, p in enumerate(PRODUCTS_CONFIG):
    path = gen.create_product_graphic(p)
    print(f"[{idx+1}/{len(PRODUCTS_CONFIG)}] Generated: {p['id_slug']}.png")

print("All 33 product graphics generated successfully!")
