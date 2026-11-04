import os
from PIL import Image, ImageDraw, ImageFont

PIN_PATH = "/Users/bishal/ai_toolkit_pro_web/assets/pinterest_impulse_gear_pin.jpg"
PRODUCTS_DIR = "/Users/bishal/ai_toolkit_pro_web/assets/products"

W, H = 1000, 1500
img = Image.new("RGB", (W, H), (3, 23, 22))
draw = ImageDraw.Draw(img)

# Background ambient glows
draw.ellipse([(W//2 - 400, -80), (W//2 + 400, 480)], fill=(12, 150, 156))
draw.ellipse([(W//2 - 450, H - 420), (W//2 + 450, H + 180)], fill=(10, 112, 117))

# Darken overlay
overlay = Image.new("RGBA", (W, H), (3, 23, 22, 215))
img = Image.alpha_composite(img.convert("RGBA"), overlay)
draw = ImageDraw.Draw(img)

# Font setup
font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
font_regular = "/System/Library/Fonts/Supplemental/Arial.ttf"

try:
    f_header = ImageFont.truetype(font_bold, 50)
    f_header_sub = ImageFont.truetype(font_bold, 44)
    f_sub = ImageFont.truetype(font_regular, 24)
    f_card_title = ImageFont.truetype(font_bold, 27)
    f_card_sub = ImageFont.truetype(font_regular, 21)
    f_pill = ImageFont.truetype(font_bold, 22)
    f_badge = ImageFont.truetype(font_bold, 21)
    f_cta_title = ImageFont.truetype(font_bold, 30)
    f_cta_btn = ImageFont.truetype(font_bold, 26)
except Exception:
    f_header = ImageFont.load_default()
    f_header_sub = f_header
    f_sub = f_header
    f_card_title = f_header
    f_card_sub = f_header
    f_pill = f_header
    f_badge = f_header
    f_cta_title = f_header
    f_cta_btn = f_header

# 1. Top Brand Tag
pill_w, pill_h = 360, 46
pill_x1 = (W - pill_w) // 2
draw.rounded_rectangle([pill_x1, 45, pill_x1 + pill_w, 45 + pill_h], radius=23, fill=(4, 36, 38, 240), outline=(12, 150, 156, 220), width=2)
draw.text((W // 2, 68), "CREATOR DESK SETUP GUIDE • 2026", font=f_pill, fill=(0, 168, 225), anchor="mm")

# 2. Main High-Impact Headline
draw.text((W // 2, 135), "4 MUST-HAVE DESK UPGRADES", font=f_header, fill=(255, 255, 255), anchor="mm")
draw.text((W // 2, 190), "UNDER ₹3,000 / BUDGET ESSENTIALS", font=f_header_sub, fill=(255, 153, 0), anchor="mm")
draw.text((W // 2, 238), "Top-Rated Creator Rigs • Amazon India Verified Deals • 1-Day Prime", font=f_sub, fill=(148, 163, 184), anchor="mm")

# 3. 2x2 Product Grid Cards
cards = [
    {
        "title": "Portronics Clamp X",
        "sub": "Multi-Angle Laptop Riser",
        "price_badge": "₹899 (55% OFF)",
        "badge_color": (204, 12, 57), # Amazon deal red
        "file": "portronics-clamp-x-laptop-stand.jpg",
        "box": (55, 280, 475, 680)
    },
    {
        "title": "Ulanzi VL49 RGB",
        "sub": "Portable Studio Pocket LED",
        "price_badge": "₹1,999 (#1 Best Seller)",
        "badge_color": (230, 122, 0), # Amazon orange
        "file": "ulanzi-vl49-rgb-pocket-led-light.jpg",
        "box": (525, 280, 945, 680)
    },
    {
        "title": "Rife Heavy Duty Gas Arm",
        "sub": "Dual Monitor Desk Mount",
        "price_badge": "₹3,999 (50% OFF)",
        "badge_color": (204, 12, 57),
        "file": "rife-dual-monitor-arm-gas-spring.jpg",
        "box": (55, 715, 475, 1115)
    },
    {
        "title": "Fifine AmpliGame AM8",
        "sub": "XLR & USB Dynamic Mic",
        "price_badge": "₹5,390 (Top Rated)",
        "badge_color": (12, 150, 156), # Teal accent
        "file": "fifine-am8-rgb-dynamic-mic.jpg",
        "box": (525, 715, 945, 1115)
    }
]

for card in cards:
    x1, y1, x2, y2 = card["box"]
    
    # White card container with subtle shadow
    draw.rounded_rectangle([x1, y1, x2, y2], radius=20, fill=(255, 255, 255))
    
    # Product Image
    img_path = os.path.join(PRODUCTS_DIR, card["file"])
    if os.path.exists(img_path):
        try:
            p_img = Image.open(img_path).convert("RGBA")
            target_w = x2 - x1 - 50
            target_h = y2 - y1 - 130
            p_img.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)
            offset_x = x1 + (x2 - x1 - p_img.width) // 2
            offset_y = y1 + 25 + (target_h - p_img.height) // 2
            img.paste(p_img, (offset_x, offset_y), p_img)
        except Exception as e:
            print(f"Error loading {card['file']}: {e}")
            
    # Floating Price Deal Badge (Top Left of card)
    badge_text = card["price_badge"]
    badge_bg = card["badge_color"]
    draw.rounded_rectangle([x1 + 14, y1 + 14, x1 + 230, y1 + 52], radius=8, fill=badge_bg)
    draw.text((x1 + 122, y1 + 33), badge_text, font=f_badge, fill=(255, 255, 255), anchor="mm")
    
    # Bottom Label Bar
    draw.rounded_rectangle([x1, y2 - 82, x2, y2], radius=0, fill=(4, 36, 38, 255))
    draw.text((x1 + (x2 - x1) // 2, y2 - 53), card["title"], font=f_card_title, fill=(255, 255, 255), anchor="mm")
    draw.text((x1 + (x2 - x1) // 2, y2 - 24), card["sub"], font=f_card_sub, fill=(148, 163, 184), anchor="mm")

# 4. Bottom High-Converting Call To Action Box
cta_y1 = 1150
cta_y2 = 1445
draw.rounded_rectangle([55, cta_y1, W - 55, cta_y2], radius=24, fill=(4, 36, 38, 245), outline=(255, 153, 0, 180), width=2)

draw.text((W // 2, cta_y1 + 45), "Upgrade Your Setup on Amazon India Today", font=f_cta_title, fill=(255, 255, 255), anchor="mm")
draw.text((W // 2, cta_y1 + 90), "Direct Prime Links • Price Drops • Full Tech Rigs", font=f_sub, fill=(148, 163, 184), anchor="mm")

# Yellow Amazon Style Button
btn_w = 640
btn_h = 70
btn_x1 = (W - btn_w) // 2
btn_y1 = cta_y1 + 130
draw.rounded_rectangle([btn_x1, btn_y1, btn_x1 + btn_w, btn_y1 + btn_h], radius=22, fill=(255, 216, 20))
draw.text((W // 2, btn_y1 + btn_h // 2), "Shop Official Creator Gear Deals ➔", font=f_cta_btn, fill=(15, 17, 17), anchor="mm")

# Destination Link text
draw.text((W // 2, cta_y1 + 240), "ai-toolkit-pro-eta.vercel.app/creator-gear", font=f_sub, fill=(0, 168, 225), anchor="mm")

# Save pin
img.convert("RGB").save(PIN_PATH, "JPEG", quality=95)
print(f"Generated Impulse Gear Pin at {PIN_PATH} ({os.path.getsize(PIN_PATH)} bytes)")
