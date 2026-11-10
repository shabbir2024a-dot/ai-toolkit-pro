import os
import sys
sys.path.append('/Users/bishal/ai_toolkit_pro_web')
import generate_product_images as gen

PRODUCTS_CONFIG = [
    {
        "id_slug": "mega-vault-900-web-softwares",
        "short_title": "900+ Enterprise Web Softwares & SaaS Vault",
        "tagline": "Master VIP Pass • 900+ PHP SaaS, POS, CRMs, ERPs, Portals & Scripts",
        "badge_txt": "900+ MASTER VAULT",
        "accent": (245, 158, 11), # Amber Gold
        "url_mock": "https://vault.cds.chementor.in/900-softwares",
        "menu_items": ["900+ Softwares", "Full Archives", "SaaS Engines", "Reseller Rights"],
        "stats": [
            ("REPOSITORY", "900+ Web Apps", (245, 158, 11)),
            ("CATEGORIES", "POS, CRM, ERP, SaaS", (12, 150, 156)),
            ("ACCESS", "Lifetime Drive Pass", (34, 197, 94))
        ],
        "ui_kind": "vault"
    },
    {
        "id_slug": "ultimate-pos-billing-saas",
        "short_title": "Ultimate POS & Inventory Management SaaS",
        "tagline": "Multi-Location POS, Stock Control, Barcode Generator & GST Billing",
        "badge_txt": "ENTERPRISE POS",
        "accent": (16, 185, 129), # Emerald
        "url_mock": "https://pos.suite/pos-counter",
        "menu_items": ["POS Terminal", "Products", "Stock Alerts", "Tax Invoices"],
        "stats": [
            ("LOCATIONS", "Multi-Warehouse", (16, 185, 129)),
            ("PRINTING", "Thermal POS & Barcodes", (56, 189, 248)),
            ("BILLING", "GST / VAT Ready", (234, 179, 8))
        ],
        "ui_kind": "table",
        "table_cols": ["PRODUCT / SKU", "STOCK LEVEL", "UNIT PRICE", "POS STATUS"],
        "table_rows": [
            ("Wireless Barcode Scanner", "142 Units in Stock", "₹1,850", "IN STOCK"),
            ("Thermal Receipt Paper (80mm)", "520 Rolls", "₹45", "IN STOCK")
        ]
    },
    {
        "id_slug": "ultimate-project-crm-manager",
        "short_title": "Ultimate Project Manager & Client CRM PRO",
        "tagline": "Kanban Milestones, Client Invoices, Timesheets & Staff Helpdesk",
        "badge_txt": "AGENCY CRM",
        "accent": (59, 130, 246), # Royal Blue
        "url_mock": "https://crm.agency/projects/board",
        "menu_items": ["Kanban Board", "Clients", "Invoices", "Timesheets"],
        "stats": [
            ("PROJECTS", "Kanban & Sprints", (59, 130, 246)),
            ("PORTAL", "Client Access & Pay", (12, 150, 156)),
            ("TICKETS", "SLA Support Desk", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["PROJECT NAME", "CLIENT", "MILESTONE", "INVOICE"],
        "table_rows": [
            ("Fintech Mobile App Redesign", "Vertex Corp", "UI Phase 2 Completed", "₹45,000 PAID"),
            ("Healthcare EHR SaaS Portal", "Apollo Med", "Database Schema & API", "₹80,000 ACTIVE")
        ]
    },
    {
        "id_slug": "stackposts-social-marketing-suite",
        "short_title": "Stackposts Multi-Platform Social Media Suite",
        "tagline": "Auto-Publish & Schedule Across Instagram, FB, Twitter, LinkedIn & Pinterest",
        "badge_txt": "SOCIAL SUITE",
        "accent": (168, 85, 247), # Purple
        "url_mock": "https://social.stack/publisher",
        "menu_items": ["Publish Scheduler", "Accounts", "Content Calendar", "Analytics"],
        "stats": [
            ("NETWORKS", "7+ Social Platforms", (168, 85, 247)),
            ("AUTOMATION", "Reels & Carousels", (234, 179, 8)),
            ("CALENDAR", "Drag & Drop Queue", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["CAMPAIGN POST", "TARGET NETWORK", "SCHEDULE TIME", "STATUS"],
        "table_rows": [
            ("AI Marketing Trends 2026", "Instagram + LinkedIn", "Today 06:30 PM", "QUEUED"),
            ("Product Launch Promo Reel", "Facebook + YouTube", "Tomorrow 10:00 AM", "READY")
        ]
    },
    {
        "id_slug": "ucloud-cloud-storage-saas",
        "short_title": "uCloud Self-Hosted Cloud Storage & File SaaS",
        "tagline": "Google Drive Alternative • Password-Protected Shares & Chunked Uploads",
        "badge_txt": "CLOUD STORAGE",
        "accent": (14, 165, 233), # Sky Blue
        "url_mock": "https://cloud.ucloud.app/drive/my-files",
        "menu_items": ["My Files", "Shared Links", "Storage Quota", "User Groups"],
        "stats": [
            ("STORAGE", "Chunked File Upload", (14, 165, 233)),
            ("SECURITY", "Password Shares & Expiry", (12, 150, 156)),
            ("PREVIEW", "PDF, Video & Audio Player", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["FILE / FOLDER NAME", "SIZE", "SECURITY", "DOWNLOADS"],
        "table_rows": [
            ("Client_Brand_Identity_Pack.zip", "248.5 MB", "Password Protected", "84 Downloads"),
            ("Product_Explainer_4K.mp4", "1.2 GB", "Expiring Link (48h)", "120 Views")
        ]
    },
    {
        "id_slug": "ultimate-school-college-erp",
        "short_title": "Ultimate School & College Academic ERP",
        "tagline": "Student Admissions, Fee Receipts, Examination Grade Sheets & Staff Payroll",
        "badge_txt": "EDTECH ERP",
        "accent": (234, 88, 12), # Orange
        "url_mock": "https://erp.campus.edu/portal",
        "menu_items": ["Admissions", "Fee Collection", "Exam Results", "Staff Payroll"],
        "stats": [
            ("STUDENTS", "Admission & ID Cards", (234, 88, 12)),
            ("FEES", "Automated Due Invoices", (34, 197, 94)),
            ("EXAMS", "Report Cards & Ranks", (56, 189, 248))
        ],
        "ui_kind": "table",
        "table_cols": ["STUDENT NAME", "CLASS / SECTION", "FEE STATUS", "ATTENDANCE"],
        "table_rows": [
            ("Devansh Kashyap (Roll 104)", "Grade 10 - Section A", "Term 2 Paid (₹14,500)", "96.4% Present"),
            ("Aanya Baruah (Roll 108)", "Grade 10 - Section A", "Term 2 Paid (₹14,500)", "98.1% Present")
        ]
    },
    {
        "id_slug": "xerochat-multichannel-marketing-bot",
        "short_title": "XeroChat Multi-Channel Marketing Chatbot",
        "tagline": "Visual Flow Builder, Auto Comment Replies & Messenger Broadcast Bot",
        "badge_txt": "CHATBOT PRO",
        "accent": (34, 197, 94), # Emerald Green
        "url_mock": "https://bot.xerochat.io/flow-builder",
        "menu_items": ["Visual Flows", "Auto Comment", "Broadcaster", "Messenger Store"],
        "stats": [
            ("CHANNELS", "Facebook + Instagram", (34, 197, 94)),
            ("BUILDER", "Drag & Drop Flows", (168, 85, 247)),
            ("COMMERCE", "In-Chat Checkout", (234, 179, 8))
        ],
        "ui_kind": "chat",
        "chat_user": "Price for the marketing package?",
        "chat_bot": "Special offer ₹199 today! Tap below to claim with instant access."
    },
    {
        "id_slug": "veno-file-manager-pro",
        "short_title": "Veno White-Label Multi-User File Manager",
        "tagline": "Flat-File PHP Storage • Multi-User Roles & Folder-Level Security",
        "badge_txt": "FILE MANAGER",
        "accent": (20, 184, 166), # Teal
        "url_mock": "https://files.veno.net/drive",
        "menu_items": ["File Directory", "User Roles", "Branding", "Uploads"],
        "stats": [
            ("DATABASE", "Zero DB (Flat-File)", (20, 184, 166)),
            ("ROLES", "Granular Folder Roles", (12, 150, 156)),
            ("BRANDING", "100% White-Label", (34, 197, 94))
        ],
        "ui_kind": "table",
        "table_cols": ["FOLDER / CLIENT DIR", "USER ACCESS", "PERMISSIONS", "TOTAL FILES"],
        "table_rows": [
            ("/Client-Vault/TechCorp/", "techcorp_admin", "Read & Write & Upload", "45 Files"),
            ("/Assets/Design-Templates/", "agency_staff", "Read Only Preview", "112 Files")
        ]
    }
]

print(f"Generating covers for {len(PRODUCTS_CONFIG)} new products...")
for idx, p in enumerate(PRODUCTS_CONFIG):
    path = gen.create_product_graphic(p)
    print(f"[{idx+1}/{len(PRODUCTS_CONFIG)}] Generated: {path}")

print("Done! All 8 product covers generated.")
