import os
import sys
sys.path.append('/Users/bishal/ai_toolkit_pro_web')
import generate_product_images as gen

PRODUCTS_CONFIG = [
    {
        "id_slug": "videoflix-vod-streaming-platform",
        "short_title": "Videoflix On-Demand Video Streaming Platform",
        "tagline": "Netflix & Prime Video Clone • Multi-Device Player, Paywall & Series",
        "badge_txt": "VOD STREAMING",
        "accent": (239, 68, 68), # Crimson Red
        "url_mock": "https://stream.videoflix.app/watch/sci-fi-4k",
        "menu_items": ["Browse Movies", "Original Series", "My List", "Subscription Plans"],
        "stats": [
            ("PLAYER", "4K HLS / MP4", (239, 68, 68)),
            ("GATEWAY", "Razorpay + Stripe", (56, 189, 248)),
            ("PAYWALL", "Monthly & VIP Passes", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["FEATURED TITLE", "GENRE / TAGS", "STREAM QUALITY", "ACCESS TIER"],
        "table_rows": [
            ("Cyber City 2099 (Season 1)", "Sci-Fi / Action / Thriller", "4K Ultra HD (Dolby 5.1)", "PREMIUM VIP"),
            ("Mastering Agentic AI Studio", "Tech Documentary", "1080p Full HD", "SUBSCRIBER")
        ]
    },
    {
        "id_slug": "wowonder-social-network-platform",
        "short_title": "WoWonder Full-Scale Social Network Platform",
        "tagline": "Facebook & Twitter Clone • Newsfeed, Stories, Groups & Audio/Video Call",
        "badge_txt": "SOCIAL NETWORK",
        "accent": (59, 130, 246), # Facebook Blue
        "url_mock": "https://network.wowonder.in/feed",
        "menu_items": ["Newsfeed", "Stories", "Communities", "Video Calling"],
        "stats": [
            ("NEWSFEED", "Real-Time Posts & Reacts", (59, 130, 246)),
            ("MESSENGER", "Audio & Video Calls", (34, 197, 94)),
            ("PRO TIERS", "Paid Memberships", (234, 179, 8))
        ],
        "ui_kind": "table",
        "table_cols": ["USER ACTIVITY", "POST TYPE", "ENGAGEMENT", "REACTIONS"],
        "table_rows": [
            ("Arjun Mehta shared a video", "Tech Reel & Discussion", "1.4k Shares • 248 Comments", "❤️ 840 • 👍 512"),
            ("Designers Guild posted a job", "Community Job Listing", "42 Applications Sent", "💡 320 • 🚀 180")
        ]
    },
    {
        "id_slug": "taxibooking-uber-clone-system",
        "short_title": "TaxiBooking Pro: On-Demand Cab Booking System",
        "tagline": "Uber Clone • Live Google Maps Route Tracking, Driver Dispatch & Fares",
        "badge_txt": "MOBILITY TECH",
        "accent": (234, 179, 8), # Gold / Taxi Yellow
        "url_mock": "https://ride.taxibooking.io/dispatch",
        "menu_items": ["Live Map", "Fleet Dispatch", "Passenger Bookings", "Driver Payouts"],
        "stats": [
            ("DISPATCH", "Live GPS Tracking", (234, 179, 8)),
            ("PRICING", "Dynamic Surge & Distance", (34, 197, 94)),
            ("PLATFORM", "Driver + Rider Portals", (56, 189, 248))
        ],
        "ui_kind": "table",
        "table_cols": ["TRIP ID", "PICKUP & DESTINATION", "VEHICLE CLASS", "FARE / STATUS"],
        "table_rows": [
            ("TRIP #8492", "Airport T3 ➔ City Center", "Prime Sedan (AC)", "₹850 COMPLETED"),
            ("TRIP #8493", "Tech Park ➔ Metro Station", "Mini Hatchback", "₹320 EN ROUTE")
        ]
    },
    {
        "id_slug": "walletpro-digital-wallet-p2p",
        "short_title": "WalletPro Multi-Currency Digital Wallet & P2P",
        "tagline": "Fintech Platform • P2P Transfers, Merchant QR Payments & Exchange Rates",
        "badge_txt": "FINTECH SAAS",
        "accent": (16, 185, 129), # Emerald Fintech
        "url_mock": "https://wallet.fintech.pro/dashboard",
        "menu_items": ["Wallets", "P2P Transfer", "Merchant API", "Currency Exchange"],
        "stats": [
            ("TRANSFERS", "Instant P2P Ledger", (16, 185, 129)),
            ("PAYMENTS", "QR Scan & Pay API", (56, 189, 248)),
            ("EXCHANGE", "Multi-Currency Rates", (234, 179, 8))
        ],
        "ui_kind": "table",
        "table_cols": ["TRANSACTION", "PAYMENT TYPE", "EXCHANGE CONVERSION", "STATUS"],
        "table_rows": [
            ("Payment to Merchant #4021", "QR Scan & Pay (INR)", "₹4,200 (Fee: ₹0)", "SETTLED"),
            ("P2P Transfer to S. Ahmed", "Instant Wallet Transfer", "$150.00 ➔ ₹12,500", "COMPLETED")
        ]
    },
    {
        "id_slug": "tutorpro-online-academy-lms",
        "short_title": "TutorPro Gold: Multi-Instructor Academy LMS",
        "tagline": "Udemy Clone • Video Course Player, Quizzes & Automated Certificates",
        "badge_txt": "EDTECH LMS",
        "accent": (99, 102, 241), # Indigo
        "url_mock": "https://academy.tutorpro.net/course/ai-mastery",
        "menu_items": ["Course Catalog", "Instructors", "Quizzes & Tests", "Certificates"],
        "stats": [
            ("COURSES", "Video Player & Files", (99, 102, 241)),
            ("COMMISSION", "Instructor Splits", (34, 197, 94)),
            ("CERTIFICATES", "Automated PDF Awards", (234, 179, 8))
        ],
        "ui_kind": "table",
        "table_cols": ["COURSE TITLE", "INSTRUCTOR", "ENROLLED STUDENTS", "REVENUE"],
        "table_rows": [
            ("Mastering Agentic AI & Micro-SaaS", "Prof. K. Sen", "1,840 Students", "₹3,68,000"),
            ("Full-Stack PHP 8.2 Enterprise Apps", "Shabbir Ahmed", "940 Students", "₹1,88,000")
        ]
    },
    {
        "id_slug": "unisite-classified-ads-marketplace",
        "short_title": "UniSite Board: Classified Ads & Marketplace",
        "tagline": "OLX Clone • City Filters, User Messenger, VIP Featured Ads & Banners",
        "badge_txt": "MARKETPLACE",
        "accent": (249, 115, 22), # Orange Marketplace
        "url_mock": "https://classifieds.unisite.in/ads/electronics",
        "menu_items": ["Browse Ads", "Post Free Ad", "VIP Promotions", "Buyer Chat"],
        "stats": [
            ("CATEGORIES", "Auto, Homes, Jobs, Tech", (249, 115, 22)),
            ("VIP ADS", "Paid Top Listing Bumps", (34, 197, 94)),
            ("MESSAGING", "Built-In Buyer Chat", (56, 189, 248))
        ],
        "ui_kind": "table",
        "table_cols": ["AD LISTING TITLE", "LOCATION / CITY", "ASKING PRICE", "PROMOTION"],
        "table_rows": [
            ("Apple MacBook Air M3 (16GB/512GB)", "Guwahati, Assam", "₹82,000", "FEATURED VIP"),
            ("2 BHK Luxury Furnished Apartment", "Salt Lake, Kolkata", "₹45,00,000", "TOP BUMPED")
        ]
    },
    {
        "id_slug": "ultimate-loan-microfinance-manager",
        "short_title": "Ultimate Loan & Microfinance Ledger ERP",
        "tagline": "NBFC & Lenders • EMI Amortization, Grace Periods & Borrower Ledgers",
        "badge_txt": "FINANCE ERP",
        "accent": (20, 184, 166), # Teal Finance
        "url_mock": "https://loans.ledger.app/repayments",
        "menu_items": ["Borrower KYC", "Loan Plans", "EMI Schedules", "Collections"],
        "stats": [
            ("AMORTIZATION", "Flat & Reducing Rate", (20, 184, 166)),
            ("PENALTIES", "Auto Overdue Fees", (239, 68, 68)),
            ("RECORDS", "Borrower Ledger Audit", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["BORROWER NAME", "LOAN AMOUNT", "NEXT EMI DUE", "LEDGER STATUS"],
        "table_rows": [
            ("Rohit Varma (LN-1092)", "₹1,50,000 (12M)", "15 Nov 2026 (₹13,850)", "ACTIVE ON TIME"),
            ("Neelam Borah (LN-1095)", "₹75,000 (6M)", "18 Nov 2026 (₹13,200)", "ACTIVE ON TIME")
        ]
    },
    {
        "id_slug": "virtual-tour-360-panoramic-maker",
        "short_title": "360° Virtual Tour & Panoramic VR Creator",
        "tagline": "Real Estate & Hotels • Hotspots, Floorplans, Gyroscope & VR Embeds",
        "badge_txt": "3D VR SAAS",
        "accent": (6, 182, 212), # Cyan VR
        "url_mock": "https://vr.virtualtour360.live/tour/grand-resort",
        "menu_items": ["Tour Editor", "Panorama Hotspots", "Floorplan Map", "Web Embed"],
        "stats": [
            ("PANORAMA", "Equirectangular 8K", (6, 182, 212)),
            ("HOTSPOTS", "Info, Audio, Video & Links", (234, 179, 8)),
            ("SUPPORT", "Mobile Gyroscope & VR", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["TOUR SCENE / ROOM", "ATTACHED HOTSPOTS", "RESOLUTION", "EMBED STATUS"],
        "table_rows": [
            ("Executive Suite Living Room", "4 Interactive Hotspots", "8192 x 4096 (8K)", "LIVE EMBEDDED"),
            ("Infinity Pool & Ocean Deck", "3 Video Hotspots + Audio", "8192 x 4096 (8K)", "LIVE EMBEDDED")
        ]
    },
    {
        "id_slug": "ultimate-bulk-sms-gateway-reseller",
        "short_title": "Ultimate Bulk SMS Gateway & Reseller Portal",
        "tagline": "Multi-Gateway SMS SaaS • Sender IDs, OTP API, DND & Scheduled Blasts",
        "badge_txt": "TELECOM B2B",
        "accent": (147, 51, 234), # Purple Telecom
        "url_mock": "https://sms.gateway.net/broadcast/new",
        "menu_items": ["Campaign Dispatch", "Sender IDs", "User Balances", "Gateway API"],
        "stats": [
            ("THROUGHPUT", "500 SMS / Second", (147, 51, 234)),
            ("GATEWAYS", "Twilio, Plivo, HTTP", (56, 189, 248)),
            ("RESELLER", "User Balance & Topups", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["CAMPAIGN TITLE", "TOTAL RECIPIENTS", "DELIVERY RATE", "BALANCE COST"],
        "table_rows": [
            ("Diwali Mega Festive Sale Blast", "45,000 Contacts", "99.2% Delivered (OTP)", "45,000 Credits"),
            ("Appointment Reminder Queue", "1,200 Contacts", "100.0% Delivered", "1,200 Credits")
        ]
    },
    {
        "id_slug": "turbowebsite-seo-audit-reviewer",
        "short_title": "TurboWebsite SEO Audit & Domain Analyzer",
        "tagline": "Automated Technical SEO Reviewer • 50+ Page Branded PDF Reports",
        "badge_txt": "SEO ANALYZER",
        "accent": (16, 185, 129), # Emerald SEO
        "url_mock": "https://audit.turboseo.pro/review/domain",
        "menu_items": ["Domain Audit", "PDF Generator", "Competitor Compare", "Lead Form"],
        "stats": [
            ("AUDIT METRICS", "50+ Technical Checks", (16, 185, 129)),
            ("PDF REPORTS", "White-Label Branded", (234, 179, 8)),
            ("LEAD CAPTURE", "Client Widget Included", (56, 189, 248))
        ],
        "ui_kind": "table",
        "table_cols": ["AUDIT DOMAIN", "SEO HEALTH SCORE", "CRITICAL ISSUES", "PDF REPORT"],
        "table_rows": [
            ("https://techstartup.io", "Score: 88/100 (GOOD)", "2 Slow Assets • No Schema", "READY DOWNLOAD"),
            ("https://dentalclinic.co.in", "Score: 62/100 (NEEDS WORK)", "Missing Meta • Slow LCP", "READY DOWNLOAD")
        ]
    }
]

print(f"Generating covers for {len(PRODUCTS_CONFIG)} top blockbuster products...")
for idx, p in enumerate(PRODUCTS_CONFIG):
    path = gen.create_product_graphic(p)
    print(f"[{idx+1}/{len(PRODUCTS_CONFIG)}] Generated: {path}")

print("Done! All blockbuster product covers generated.")
