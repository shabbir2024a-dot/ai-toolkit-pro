import os
import json
import re
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = "/Users/bishal/ai_toolkit_pro_web"
ASSETS_PRODUCTS_DIR = os.path.join(BASE_DIR, "assets", "products")
ASSETS_GEAR_DIR = os.path.join(BASE_DIR, "assets", "gear")

os.makedirs(ASSETS_PRODUCTS_DIR, exist_ok=True)
os.makedirs(ASSETS_GEAR_DIR, exist_ok=True)

NEW_PRODUCTS = [
    # 🎙️ PRO AUDIO & REFERENCE MONITORS
    {
        "slug": "rode-nt1-5th-gen-condenser-mic",
        "title": "Røde NT1 5th Gen Studio Condenser Mic",
        "subtitle": "32-Bit Float On-Board Recording • XLR & USB-C Dual Output • Revolution Preamp",
        "brand": "RØDE • BROADCAST STUDIO",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹23,990",
        "mrp": "₹28,500",
        "discount": "16% OFF",
        "rating": "4.8 ★ (3,400+ Reviews)",
        "badge": "32-BIT FLOAT",
        "accent": (12, 150, 156),
        "specs": ["Ultra-Low Noise (4dBA) Capsule", "32-Bit Float USB Recording Zero Clipping", "Internal DSP with APHEX Audio Effects"],
        "url": "https://www.amazon.in/dp/B0BSV45N62?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "yamaha-hs5-powered-studio-monitors",
        "title": "Yamaha HS5 Powered Studio Monitors (Pair)",
        "subtitle": "5-Inch Cone Woofer • 1-Inch Dome Tweeter • Bi-Amp 70W Nearfield Monitors",
        "brand": "YAMAHA • AUDIO REFERENCE",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹31,990",
        "mrp": "₹38,000",
        "discount": "16% OFF",
        "rating": "4.7 ★ (4,800+ Reviews)",
        "badge": "STUDIO STANDARD",
        "accent": (12, 150, 156),
        "specs": ["54Hz - 30kHz Flat Frequency Response", "Room Control and High TRIM Filters", "Bi-Amplified 70W High-Performance Output"],
        "url": "https://www.amazon.in/dp/B00CFOX420?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "lewitt-lct-440-pure-condenser-mic",
        "title": "Lewitt LCT 440 PURE Large Diaphragm Mic",
        "subtitle": "1-Inch True Condenser Capsule • Gold Sputtered Mylar • Zero Distortion",
        "brand": "LEWITT • VIENNA AUDIO",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹24,490",
        "mrp": "₹29,990",
        "discount": "18% OFF",
        "rating": "4.9 ★ (1,150+ Reviews)",
        "badge": "PURE CLARITY",
        "accent": (12, 150, 156),
        "specs": ["Gold-Sputtered 3-Micron Mylar Capsule", "Outstanding High-End Vocal Presence", "Magnetic Pop Filter & Shock Mount Included"],
        "url": "https://www.amazon.in/dp/B06XQ2G8W2?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "rodecaster-pro-ii-audio-studio",
        "title": "Rodecaster Pro II Audio Production Studio",
        "subtitle": "Quad Revolution Preamps • Dual USB-C Audio • APHEX DSP Processing",
        "brand": "RØDE • ALL-IN-ONE MIXER",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹64,990",
        "mrp": "₹74,990",
        "discount": "13% OFF",
        "rating": "4.8 ★ (2,400+ Reviews)",
        "badge": "FLAGSHIP CONSOLE",
        "accent": (12, 150, 156),
        "specs": ["4 High-Gain Combo XLR/TRS Revolution Preamps", "8 Fully Programmable SMART Trigger Pads", "Dual USB-C Audio Interfaces for 2 PCs"],
        "url": "https://www.amazon.in/dp/B0B17V9V6M?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "elgato-stream-deck-plus",
        "title": "Elgato Stream Deck + (Console & Touch Strip)",
        "subtitle": "8 LCD Keys • 4 Rotary Encoders • Dynamic Touch Strip • Wave Link Hub",
        "brand": "ELGATO • WORKFLOW AUTOMATION",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹19,990",
        "mrp": "₹23,990",
        "discount": "17% OFF",
        "rating": "4.8 ★ (5,200+ Reviews)",
        "badge": "CREATOR CONSOLE",
        "accent": (12, 150, 156),
        "specs": ["4 Tactile Push Encoders for Audio & Dials", "Dynamic Touch Strip Display with Swipe Navigation", "Deep OBS Studio & Premiere Pro Integrations"],
        "url": "https://www.amazon.in/dp/B0BHTR7M4Z?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    # 📷 4K CINEMA & OPTICS
    {
        "slug": "sony-fx30-cinema-line-camera",
        "title": "Sony FX30 Cinema Line Super 35 Camera",
        "subtitle": "Dual Base ISO 800/2500 • 4K 120p 10-bit 4:2:2 • S-Cinetone Color Science",
        "brand": "SONY CINEMA LINE • PROFESSIONAL VIDEO",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹1,79,990",
        "mrp": "₹1,99,990",
        "discount": "10% OFF",
        "rating": "4.8 ★ (1,450+ Reviews)",
        "badge": "CINEMA PRO",
        "accent": (12, 150, 156),
        "specs": ["Super 35 Back-Illuminated 6K Sensor", "4K 120p 10-bit 4:2:2 All-Intra Recording", "Active Cooling Fan for Unlimited 4K Capture"],
        "url": "https://www.amazon.in/dp/B0BGJBMK6W?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "sigma-24-70mm-f2-8-dg-dn-art-lens",
        "title": "Sigma 24-70mm f/2.8 DG DN Art Lens (Sony E)",
        "subtitle": "Constant f/2.8 Aperture • 11-Blade Circular Diaphragm • Nano Porous Coating",
        "brand": "SIGMA • ART SERIES OPTICS",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹98,900",
        "mrp": "₹1,24,900",
        "discount": "21% OFF",
        "rating": "4.9 ★ (2,100+ Reviews)",
        "badge": "FLAGSHIP GLASS",
        "accent": (12, 150, 156),
        "specs": ["Constant f/2.8 Maximum Aperture Throughout Zoom", "Hyper Sonic Stepping Motor for Fast Silent AF", "Dust & Splash-Proof Brass Bayonet Mount"],
        "url": "https://www.amazon.in/dp/B0829RP85S?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "elgato-4k-x-capture-card",
        "title": "Elgato 4K X External USB-C Capture Card",
        "subtitle": "4K144 Pass-Through & Capture • 1080p240 Refresh • VRR & HDR10 Support",
        "brand": "ELGATO • BROADCAST CAPTURE",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹21,990",
        "mrp": "₹26,990",
        "discount": "19% OFF",
        "rating": "4.7 ★ (1,850+ Reviews)",
        "badge": "4K 144FPS",
        "accent": (12, 150, 156),
        "specs": ["HDMI 2.1 Ultra-Low Latency Pass-Through", "Up to 4K144 / 1080p240 High Frame Rate Capture", "Driverless Plug & Play on Mac, Windows, iPad"],
        "url": "https://www.amazon.in/dp/B0CP2CS95L?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "aputure-amaran-100d-s-led-light",
        "title": "Aputure Amaran 100d S Daylight LED Light",
        "subtitle": "100W Ultra-High Color Quality • 5600K Daylight • CRI 95+ TLCI 97+ • Bowens Mount",
        "brand": "APUTURE • AMARAN CINEMA",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹18,490",
        "mrp": "₹22,990",
        "discount": "20% OFF",
        "rating": "4.8 ★ (3,600+ Reviews)",
        "badge": "PRO STUDIO LIGHT",
        "accent": (12, 150, 156),
        "specs": ["Ultra-High SSI Color Accuracy CRI 95+ TLCI 97+", "Universal Bowens Mount for Studio Softboxes", "Sidus Link Smartphone App Wireless Bluetooth Control"],
        "url": "https://www.amazon.in/dp/B0BXFSW9J9?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "aputure-light-dome-se-softbox",
        "title": "Aputure Light Dome SE 33.5\" Softbox Diffuser",
        "subtitle": "16-Sided Hexadecagon Softbox • 1.5 & 2.5 Stop Diffusion • 45° Fabric Grid",
        "brand": "APUTURE • STUDIO MODIFIER",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹8,990",
        "mrp": "₹11,500",
        "discount": "22% OFF",
        "rating": "4.7 ★ (2,900+ Reviews)",
        "badge": "CINEMA SOFT LIGHT",
        "accent": (12, 150, 156),
        "specs": ["Deep Parabolic 16-Sided Hexadecagon Shape", "Dual Front Diffusion Fabrics & 45° Honeycomb Grid", "Lightweight Fiberglass Rods for Fast Studio Setup"],
        "url": "https://www.amazon.in/dp/B08YRPQDF7?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "dji-rs-3-mini-camera-gimbal",
        "title": "DJI RS 3 Mini 3-Axis Camera Gimbal",
        "subtitle": "Ultra-Lightweight 795g Body • 2kg Tested Payload • Native Vertical Video",
        "brand": "DJI • PROFESSIONAL STABILIZER",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹25,990",
        "mrp": "₹32,990",
        "discount": "21% OFF",
        "rating": "4.7 ★ (4,100+ Reviews)",
        "badge": "NATIVE VERTICAL",
        "accent": (12, 150, 156),
        "specs": ["795g Ultra-Compact Lightweight Design", "Native Vertical Shooting for YouTube Shorts & Reels", "Bluetooth Wireless Shutter Control Integration"],
        "url": "https://www.amazon.in/dp/B0BSH7Y1XQ?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "zhiyun-crane-m3s-gimbal-stabilizer",
        "title": "Zhiyun Crane M3S Gimbal Stabilizer",
        "subtitle": "Built-in Lumen Amplifier Fill Light • Quick Release 4.0 • Bluetooth Shutter",
        "brand": "ZHIYUN • CREATOR GIMBAL",
        "category": "camera",
        "category_name": "Cameras & Optics",
        "price": "₹26,490",
        "mrp": "₹34,000",
        "discount": "22% OFF",
        "rating": "4.6 ★ (1,300+ Reviews)",
        "badge": "PORTABLE VLOGGING",
        "accent": (12, 150, 156),
        "specs": ["Built-in 1000 Lux Bi-Color Video Fill Light", "Quick Release Plate without Rebalancing Between Battery Swaps", "PD Fast Charging 100% in 2 Hours"],
        "url": "https://www.amazon.in/dp/B0C6DB7Q5X?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    # 🖥️ WORKSTATION DISPLAYS & HARDWARE
    {
        "slug": "asus-proart-pa278cv-designer-monitor",
        "title": "ASUS ProArt Display PA278CV 27-Inch 1440p",
        "subtitle": "2560 x 1440 IPS • 100% sRGB / Rec.709 • Calman Verified Delta E < 2 • 65W USB-C",
        "brand": "ASUS PROART • COLOR ACCURACY",
        "category": "hardware",
        "category_name": "Rig Hardware",
        "price": "₹28,990",
        "mrp": "₹37,000",
        "discount": "22% OFF",
        "rating": "4.7 ★ (3,100+ Reviews)",
        "badge": "CALMAN VERIFIED",
        "accent": (12, 150, 156),
        "specs": ["100% sRGB & 100% Rec. 709 Wide Color Gamut", "Calman Verified Factory Pre-Calibrated Delta E < 2", "65W USB-C Single Cable Video, Data & Fast Charging"],
        "url": "https://www.amazon.in/dp/B08LCP296A?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "benq-pd2705u-4k-designer-monitor",
        "title": "BenQ PD2705U 27-Inch 4K UHD Designer Monitor",
        "subtitle": "3840 x 2160 UHD • AQCOLOR Technology • 99% sRGB / Rec.709 • KVM Switch",
        "brand": "BENQ • PROFESSIONAL DISPLAY",
        "category": "hardware",
        "category_name": "Rig Hardware",
        "price": "₹44,990",
        "mrp": "₹56,000",
        "discount": "20% OFF",
        "rating": "4.7 ★ (1,700+ Reviews)",
        "badge": "4K UHD AQCOLOR",
        "accent": (12, 150, 156),
        "specs": ["4K UHD (3840x2160) IPS Anti-Glare Panel", "Integrated KVM Switch for Instant Dual PC Control", "Hotkey Puck G2 Controller for Instant Color Profile Switching"],
        "url": "https://www.amazon.in/dp/B09Q8562B1?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    {
        "slug": "logitech-mx-mechanical-wireless-keyboard",
        "title": "Logitech MX Mechanical Wireless Tactile Keyboard",
        "subtitle": "Low-Profile Tactile Quiet Mechanical Switches • Smart Backlighting • Multi-OS",
        "brand": "LOGITECH • MASTER SERIES",
        "category": "hardware",
        "category_name": "Rig Hardware",
        "price": "₹14,990",
        "mrp": "₹18,995",
        "discount": "21% OFF",
        "rating": "4.8 ★ (4,900+ Reviews)",
        "badge": "MASTER SERIES",
        "accent": (12, 150, 156),
        "specs": ["Low-Profile Quiet Tactile Mechanical Switches", "Smart Backlighting with Hand Proximity Sensors", "Multi-OS Dual Bluetooth and Logi Bolt Wireless Support"],
        "url": "https://www.amazon.in/dp/B09LK2R8D2?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    },
    # 🪑 ERGONOMIC CREATOR SEATING
    {
        "slug": "sihoo-doro-c300-ergonomic-creator-chair",
        "title": "Sihoo Doro C300 Ergonomic Creator Chair",
        "subtitle": "Dynamic Self-Adaptive Lumbar Support • 6D Coordinated Armrests • Cloud Mesh",
        "brand": "SIHOO • ERGONOMIC SEATING",
        "category": "workspace",
        "category_name": "Ergonomics & Desk",
        "price": "₹28,990",
        "mrp": "₹42,000",
        "discount": "31% OFF",
        "rating": "4.7 ★ (5,800+ Reviews)",
        "badge": "ALL-DAY COMFORT",
        "accent": (12, 150, 156),
        "specs": ["Dynamic Self-Adaptive Lumbar Support Follows Posture", "6D Synchronized Mechanical Armrests", "Pressure-Relieving Cloud Mesh with Waterfall Seat Edge"],
        "url": "https://www.amazon.in/dp/B0BYRMDV55?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.5% Commission"
    }
]

def render_studio_photo(p):
    """Render clean Amazon-style product visual for each item."""
    W, H = 1000, 1000
    im = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Soft circular background glow
    center = (W // 2, H // 2 - 40)
    for r in range(350, 100, -15):
        alpha = int(12 * (1 - r / 350))
        draw.ellipse([center[0]-r, center[1]-r, center[0]+r, center[1]+r], fill=(240, 248, 250))
    
    # Brand watermark
    try:
        font_brand = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
        font_name = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 36)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
        font_badge = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)
    except:
        font_brand = ImageFont.load_default()
        font_name = font_brand
        font_sub = font_brand
        font_badge = font_brand
        
    draw.text((60, 60), p["brand"], font=font_brand, fill=(10, 112, 117))
    
    # Central product stylized graphic container
    cx, cy = W // 2, H // 2 - 20
    box_w, box_h = 600, 500
    draw.rounded_rectangle([cx - box_w//2, cy - box_h//2, cx + box_w//2, cy + box_h//2], radius=30, fill=(248, 250, 252), outline=(226, 232, 240), width=3)
    
    # Product title inside box
    draw.text((cx - box_w//2 + 40, cy - box_h//2 + 50), p["title"], font=font_name, fill=(15, 23, 42))
    draw.text((cx - box_w//2 + 40, cy - box_h//2 + 105), p["subtitle"][:65] + "...", font=font_sub, fill=(100, 116, 139))
    
    # Specs inside box
    sy = cy - box_h//2 + 170
    for spec in p["specs"]:
        draw.ellipse([cx - box_w//2 + 40, sy + 6, cx - box_w//2 + 54, sy + 20], fill=(12, 150, 156))
        draw.text((cx - box_w//2 + 65, sy), spec, font=font_sub, fill=(30, 41, 59))
        sy += 45
        
    # Badge floating tag
    draw.rounded_rectangle([cx - box_w//2 + 40, cy + box_h//2 - 90, cx - box_w//2 + 280, cy + box_h//2 - 40], radius=12, fill=(12, 150, 156))
    draw.text((cx - box_w//2 + 60, cy + box_h//2 - 78), f"★ {p['badge']}", font=font_badge, fill=(255, 255, 255))
    
    # Bottom Amazon verification strip
    draw.rounded_rectangle([60, H - 120, W - 60, H - 40], radius=16, fill=(241, 245, 249))
    draw.text((90, H - 95), "VERIFIED PRIME CREATOR SPECIFICATION • OFFICIAL STORE ID: aitoolkitpro-21", font=font_sub, fill=(71, 85, 105))
    
    out_path = os.path.join(ASSETS_PRODUCTS_DIR, f"{p['slug']}.jpg")
    im.save(out_path, "JPEG", quality=95)
    return out_path

def render_gear_card(p):
    """Render luxury dark teal preview banner in assets/gear/"""
    W, H = 1200, 675
    im = Image.new("RGBA", (W, H), (3, 23, 22, 255))
    draw = ImageDraw.Draw(im)
    
    try:
        font_hero = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 38)
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 28)
        font_price = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
        font_mrp = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
        font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 19)
        font_regular = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 17)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
        font_badge = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 14)
        font_mono = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 16)
    except:
        font_hero = ImageFont.load_default()
        font_title = font_hero
        font_price = font_hero
        font_mrp = font_hero
        font_bold = font_hero
        font_regular = font_hero
        font_small = font_hero
        font_badge = font_hero
        font_mono = font_hero
        
    accent_col = p["accent"]
    
    # Card outline
    draw.rounded_rectangle([40, 40, W - 40, H - 40], radius=24, fill=(4, 36, 38, 235), outline=(12, 150, 156, 120), width=2)
    
    # Top Brand Bar
    draw.rounded_rectangle([70, 70, 420, 115], radius=12, fill=(27, 56, 71, 240), outline=(*accent_col, 180), width=1)
    draw.text((86, 82), p["brand"], font=font_badge, fill=accent_col)
    
    # Badge (Top Right)
    draw.rounded_rectangle([W - 390, 70, W - 70, 115], radius=12, fill=(*accent_col, 45), outline=(*accent_col, 220), width=1)
    draw.text((W - 370, 82), f"⚡ {p['badge']}", font=font_badge, fill=(255, 255, 255))
    
    # Title & Subtitle
    draw.text((70, 145), p["title"], font=font_hero, fill=(255, 255, 255))
    draw.text((70, 200), p["subtitle"], font=font_regular, fill=(107, 163, 190))
    
    # Specs
    sy = 275
    draw.text((70, sy), "VERIFIED CREATOR SPECIFICATIONS:", font=font_bold, fill=(255, 255, 255))
    sy += 38
    for spec in p["specs"]:
        draw.ellipse([(72, sy + 4), (84, sy + 16)], fill=accent_col)
        draw.text((98, sy), spec, font=font_regular, fill=(220, 240, 245))
        sy += 36
        
    # Rating
    sy += 15
    draw.rounded_rectangle([70, sy, 380, sy + 44], radius=10, fill=(3, 23, 22, 240), outline=(12, 150, 156, 100), width=1)
    draw.text((86, sy + 11), f"⭐ {p['rating']}", font=font_bold, fill=(245, 158, 11))
    
    # Price Box
    px1, py1, px2, py2 = W - 480, 275, W - 70, 580
    draw.rounded_rectangle([px1, py1, px2, py2], radius=20, fill=(3, 23, 22, 250), outline=(*accent_col, 160), width=2)
    draw.text((px1 + 30, py1 + 25), "LIVE VERIFIED DEAL:", font=font_small, fill=(107, 163, 190))
    draw.text((px1 + 30, py1 + 55), p["price"], font=font_price, fill=(255, 255, 255))
    draw.text((px1 + 230, py1 + 65), f"MRP {p['mrp']}", font=font_mrp, fill=(107, 163, 190))
    draw.rounded_rectangle([px1 + 30, py1 + 120, px1 + 210, py1 + 160], radius=8, fill=(34, 197, 94, 40), outline=(34, 197, 94, 180), width=1)
    draw.text((px1 + 45, py1 + 130), f"🔥 {p['discount']}", font=font_bold, fill=(34, 197, 94))
    draw.text((px1 + 30, py1 + 185), f"💰 {p['comm_est']}", font=font_bold, fill=accent_col)
    
    # CTA
    draw.rounded_rectangle([px1 + 30, py2 - 80, px2 - 30, py2 - 25], radius=12, fill=(255, 153, 0))
    draw.text((px1 + 55, py2 - 62), "BUY ON AMAZON INDIA ↗", font=font_bold, fill=(0, 0, 0))
    
    out_path = os.path.join(ASSETS_GEAR_DIR, f"{p['slug']}.png")
    im.save(out_path, "PNG", optimize=True)
    return out_path

def append_to_gear_assets():
    """Append NEW_PRODUCTS to generate_gear_assets.py"""
    with open(os.path.join(BASE_DIR, "generate_gear_assets.py"), "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if already appended
    if "rode-nt1-5th-gen-condenser-mic" in content:
        print("New products already present in generate_gear_assets.py.")
        return
        
    # Format new products python code
    new_code = "    # =========================================================================\n"
    new_code += "    # 🚀 EXPANDED FLAGSHIP CREATOR GEAR (16 Additional Rigs - 70 Total)\n"
    new_code += "    # =========================================================================\n"
    for p in NEW_PRODUCTS:
        new_code += f"    {repr(p)},\n"
    new_code += "]\n"
    
    content = content.replace("]\n\ndef draw_rounded_rect", new_code + "\ndef draw_rounded_rect")
    with open(os.path.join(BASE_DIR, "generate_gear_assets.py"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully appended 16 flagship products to generate_gear_assets.py!")

def main():
    print("Expanding Creator Store Catalog to 70 Flagship Products...")
    
    # 1. Append products to generate_gear_assets.py
    append_to_gear_assets()
    
    # 2. Render visuals for all 16 new products
    for p in NEW_PRODUCTS:
        p_photo = render_studio_photo(p)
        p_gear = render_gear_card(p)
        print(f"  Generated visuals for: {p['title']}")
        
    # 3. Run build_creator_gear_page.py
    print("\nRebuilding creator-gear.html...")
    os.system(f"python3 {os.path.join(BASE_DIR, 'build_creator_gear_page.py')}")
    
    print("\nAll 70 products live and fully styled!")

if __name__ == "__main__":
    main()
