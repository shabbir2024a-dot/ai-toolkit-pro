import os
from PIL import Image, ImageDraw, ImageFont

PIN_PATH = "/Users/bishal/ai_toolkit_pro_web/assets/pinterest_creator_gear_pin.jpg"
PRODUCTS_DIR = "/Users/bishal/ai_toolkit_pro_web/assets/products"

W, H = 1000, 1500
img = Image.new("RGB", (W, H), (3, 23, 22))
draw = ImageDraw.Draw(img)

# Glows & Grids
draw.ellipse([(W//2 - 400, -100), (W//2 + 400, 500)], fill=(12, 150, 156))
draw.ellipse([(W//2 - 450, H - 400), (W//2 + 450, H + 200)], fill=(10, 112, 117))

# Semi-transparent overlay to soften glows
overlay = Image.new("RGBA", (W, H), (3, 23, 22, 210))
img = Image.alpha_composite(img.convert("RGBA"), overlay)
draw = ImageDraw.Draw(img)

try:
    f_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 52)
    f_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 32)
    f_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
    f_pill = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 24)
    f_cta = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 28)
except Exception:
    f_title = ImageFont.load_default()
    f_sub = f_title
    f_body = f_title
    f_pill = f_title
    f_cta = f_title

# Top Brand Pill
draw.rounded_rectangle([W//2 - 200, 50, W//2 + 200, 105], radius=28, fill=(4, 36, 38, 240), outline=(12, 150, 156, 180), width=2)
draw.text((W//2, 78), "AI TOOLKIT PRO • 2026 GUIDE", font=f_pill, fill=(0, 168, 225), anchor="mm")

# Headline
draw.text((W//2, 160), "70+ BEST YOUTUBE &", font=f_title, fill=(255, 255, 255), anchor="mm")
draw.text((W//2, 225), "CREATOR STUDIO RIGS", font=f_title, fill=(255, 153, 0), anchor="mm")
draw.text((W//2, 280), "Tested Hardware • Prime 1-Day Delivery • Full Setup Specs", font=f_body, fill=(107, 163, 190), anchor="mm")

# 2x2 Visual Product Grid
cards = [
    ("Shure SM7B Vocal Mic", "shure-sm7b-dynamic-vocal-mic.jpg", "#1 Best Seller", (60, 330, 470, 710)),
    ("Sony FX30 Cinema 4K", "sony-fx30-cinema-line-camera.jpg", "Cinema Line 4K", (530, 330, 940, 710)),
    ("Røde NT1 5th Gen", "rode-nt1-5th-gen-condenser-mic.jpg", "32-Bit Float Mic", (60, 740, 470, 1120)),
    ("Zotac RTX 4070 12GB", "zotac-rtx-5060-4070-graphics-card.jpg", "Blender & Unreal Rig", (530, 740, 940, 1120))
]

for name, fname, badge, (x1, y1, x2, y2) in cards:
    # Card Background (White container)
    draw.rounded_rectangle([x1, y1, x2, y2], radius=18, fill=(255, 255, 255))
    
    # Image
    p_path = os.path.join(PRODUCTS_DIR, fname)
    if os.path.exists(p_path):
        try:
            p_img = Image.open(p_path).convert("RGBA")
            p_img.thumbnail((x2 - x1 - 40, y2 - y1 - 120), Image.Resampling.LANCZOS)
            img.paste(p_img, (x1 + (x2 - x1 - p_img.width)//2, y1 + 20), p_img)
        except Exception as e:
            pass
            
    # Badge
    draw.rounded_rectangle([x1 + 15, y1 + 15, x1 + 195, y1 + 55], radius=6, fill=(230, 122, 0))
    draw.text((x1 + 105, y1 + 35), badge, font=f_pill, fill=(255, 255, 255), anchor="mm")
    
    # Bottom Label Bar inside card
    draw.rounded_rectangle([x1, y2 - 70, x2, y2], radius=0, fill=(4, 36, 38, 255))
    draw.text((x1 + (x2 - x1)//2, y2 - 35), name, font=f_sub, fill=(255, 255, 255), anchor="mm")

# Bottom Call To Action Block
draw.rounded_rectangle([60, 1160, W - 60, 1420], radius=22, fill=(4, 36, 38, 240), outline=(255, 153, 0, 160), width=2)
draw.text((W//2, 1215), "Compare All 70+ Studio Rigs in One Place", font=f_sub, fill=(255, 255, 255), anchor="mm")
draw.text((W//2, 1265), "Microphones • Mirrorless Cameras • Sit-Stand Desks • Workstations", font=f_body, fill=(107, 163, 190), anchor="mm")

# Yellow Amazon Style Button
draw.rounded_rectangle([W//2 - 260, 1315, W//2 + 260, 1385], radius=20, fill=(255, 216, 20))
draw.text((W//2, 1350), "ai-toolkit-pro-eta.vercel.app ➔", font=f_cta, fill=(15, 17, 17), anchor="mm")

img.convert("RGB").save(PIN_PATH, "JPEG", quality=95)
print(f"Pinterest Pin generated at {PIN_PATH} ({os.path.getsize(PIN_PATH)} bytes)")
