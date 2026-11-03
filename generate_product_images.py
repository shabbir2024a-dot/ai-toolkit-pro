import os
import math
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/Users/bishal/ai_toolkit_pro_web/assets/products"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fonts
try:
    font_hero = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 36)
    font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
    font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)
    font_regular = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 17)
    font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
    font_badge = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 13)
    font_mono = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 15)
    font_mono_sm = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 12)
except Exception:
    font_hero = ImageFont.load_default()
    font_title = font_hero
    font_bold = font_hero
    font_regular = font_hero
    font_small = font_hero
    font_badge = font_hero
    font_mono = font_hero
    font_mono_sm = font_hero

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_radial_glow(draw, center, radius, color, max_alpha=50):
    cx, cy = center
    steps = 15
    for i in range(steps, 0, -1):
        r = int(radius * (i / steps))
        alpha = int(max_alpha * (1 - (i / steps)))
        fill = (*color[:3], alpha)
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=fill)

def create_product_graphic(p):
    w, h = 1200, 675
    # Create RGBA canvas for glow layering
    im = Image.new('RGBA', (w, h), (3, 23, 22, 255)) # #031716 base
    draw = ImageDraw.Draw(im)

    # 1. Subtle Background Vertical Gradient
    bg_top = (3, 23, 22)
    bg_bot = (2, 38, 39)
    for y in range(0, h, 2):
        ratio = y / h
        r = int(bg_top[0] + (bg_bot[0] - bg_top[0]) * ratio)
        g = int(bg_top[1] + (bg_bot[1] - bg_top[1]) * ratio)
        b = int(bg_top[2] + (bg_bot[2] - bg_top[2]) * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255), width=2)

    # 2. Tech grid dots
    for x in range(30, w, 45):
        for y in range(30, h, 45):
            draw.point((x, y), fill=(107, 163, 190, 35))

    accent_color = p.get('accent', (12, 150, 156)) # default cyan

    # 3. Ambient Glow behind center window
    glow_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_overlay)
    draw_radial_glow(glow_draw, (w // 2, h // 2), 360, accent_color, max_alpha=40)
    im = Image.alpha_composite(im, glow_overlay)
    draw = ImageDraw.Draw(im)

    # 4. macOS Window Container
    win_x1, win_y1 = 120, 60
    win_x2, win_y2 = 1080, 560
    
    # Outer glowing border
    draw.rounded_rectangle(
        [(win_x1 - 2, win_y1 - 2), (win_x2 + 2, win_y2 + 2)],
        radius=20,
        outline=(*accent_color, 120),
        width=2
    )

    # Window Surface
    draw.rounded_rectangle(
        [(win_x1, win_y1), (win_x2, win_y2)],
        radius=18,
        fill=(4, 36, 38, 245),
        outline=(10, 112, 117, 200),
        width=1
    )

    # Window Title Bar
    titlebar_h = 48
    draw.rounded_rectangle(
        [(win_x1, win_y1), (win_x2, win_y1 + titlebar_h)],
        radius=18,
        fill=(2, 22, 23, 255)
    )
    draw.rectangle([(win_x1, win_y1 + 30), (win_x2, win_y1 + titlebar_h)], fill=(2, 22, 23, 255))
    draw.line([(win_x1, win_y1 + titlebar_h), (win_x2, win_y1 + titlebar_h)], fill=(10, 112, 117, 180), width=1)

    # Traffic light dots
    draw.ellipse([(win_x1 + 20, win_y1 + 17), (win_x1 + 34, win_y1 + 31)], fill=(239, 68, 68))
    draw.ellipse([(win_x1 + 42, win_y1 + 17), (win_x1 + 56, win_y1 + 31)], fill=(234, 179, 8))
    draw.ellipse([(win_x1 + 64, win_y1 + 17), (win_x1 + 78, win_y1 + 31)], fill=(34, 197, 94))

    # Window Title / URL
    app_url = p.get('url_mock', f"https://demo.cds.in/{p['id_slug']}")
    draw.text((win_x1 + 100, win_y1 + 14), app_url, fill=(107, 163, 190), font=font_mono)

    # Top right pill: Category & Tech
    badge_txt = p.get('badge_txt', 'WHITE-LABEL PRO')
    bw = len(badge_txt) * 8 + 24
    draw.rounded_rectangle([(win_x2 - bw - 20, win_y1 + 11), (win_x2 - 20, win_y1 + 37)], radius=8, fill=(*accent_color, 40), outline=(*accent_color, 180), width=1)
    draw.text((win_x2 - bw - 8, win_y1 + 16), badge_txt, fill=(*accent_color, 255), font=font_badge)

    # Left Mini Sidebar inside Window
    sb_w = 170
    sb_y1 = win_y1 + titlebar_h
    draw.rectangle([(win_x1, sb_y1), (win_x1 + sb_w, win_y2)], fill=(3, 26, 27, 200))
    draw.line([(win_x1 + sb_w, sb_y1), (win_x1 + sb_w, win_y2)], fill=(10, 112, 117, 120), width=1)

    # Sidebar Menu Items
    menu_items = p.get('menu_items', ['Overview', 'Analytics', 'Settings', 'API Keys'])
    sy = sb_y1 + 24
    for idx, m in enumerate(menu_items):
        is_active = (idx == 0)
        if is_active:
            draw.rounded_rectangle([(win_x1 + 12, sy - 4), (win_x1 + sb_w - 12, sy + 28)], radius=6, fill=(*accent_color, 50))
            draw.text((win_x1 + 26, sy + 2), f"▸ {m}", fill=(255, 255, 255), font=font_bold)
        else:
            draw.text((win_x1 + 26, sy + 2), f"  {m}", fill=(107, 163, 190), font=font_regular)
        sy += 40

    # System Stats in Sidebar Bottom
    draw.line([(win_x1 + 12, win_y2 - 70), (win_x1 + sb_w - 12, win_y2 - 70)], fill=(10, 112, 117, 100), width=1)
    draw.text((win_x1 + 18, win_y2 - 58), "STACK: PHP/PY", fill=(107, 163, 190), font=font_mono_sm)
    draw.text((win_x1 + 18, win_y2 - 38), "STATUS: ONLINE", fill=(34, 197, 94), font=font_mono_sm)

    # Main Workspace Area
    main_x1 = win_x1 + sb_w + 24
    main_y1 = sb_y1 + 20
    main_x2 = win_x2 - 24
    main_w = main_x2 - main_x1

    # Product Title in Main Area
    display_title = p.get('short_title', p.get('title', 'Software Product'))
    draw.text((main_x1, main_y1), display_title, fill=(255, 255, 255), font=font_title)
    
    # Tagline / Subtitle
    sub_txt = p.get('tagline', 'Production ready digital source code & white-label web application')
    if len(sub_txt) > 65:
        sub_txt = sub_txt[:62] + '...'
    draw.text((main_x1, main_y1 + 38), sub_txt, fill=(107, 163, 190), font=font_regular)

    # 3 Stat / Metric Cards
    stat_y1 = main_y1 + 72
    stat_h = 75
    stat_w = (main_w - 24) // 3
    stats = p.get('stats', [
        ("LICENSE", "White-Label", accent_color),
        ("DATABASE", "MySQL / SQLite", (34, 197, 94)),
        ("DELIVERY", "Instant ZIP", (234, 179, 8))
    ])

    for i, (label, val, col) in enumerate(stats):
        sx1 = main_x1 + i * (stat_w + 12)
        sx2 = sx1 + stat_w
        draw.rounded_rectangle([(sx1, stat_y1), (sx2, stat_y1 + stat_h)], radius=10, fill=(2, 20, 21, 220), outline=(10, 112, 117, 150), width=1)
        draw.text((sx1 + 14, stat_y1 + 12), label, fill=(107, 163, 190), font=font_badge)
        draw.text((sx1 + 14, stat_y1 + 34), val, fill=(*col, 255), font=font_bold)

    # Main Center Preview Box (Simulated UI specific to product)
    prev_y1 = stat_y1 + stat_h + 16
    prev_y2 = win_y2 - 20
    draw.rounded_rectangle(
        [(main_x1, prev_y1), (main_x2, prev_y2)],
        radius=12,
        fill=(2, 16, 17, 240),
        outline=(*accent_color, 140),
        width=1
    )

    # Render specific UI elements based on product type
    render_custom_ui(draw, p, main_x1, prev_y1, main_x2, prev_y2, accent_color)

    # Bottom Banner Outside Window: Value Prop Pills
    pills = [
        ("✓ 100% UNENCRYPTED SOURCE CODE", (12, 150, 156)),
        ("✓ ZERO MONTHLY ROYALTIES", (34, 197, 94)),
        ("✓ RE-SELL AS YOUR OWN SAAS", (245, 158, 11))
    ]
    pill_y = h - 65
    px = win_x1 + 10
    for text, pcol in pills:
        pw = len(text) * 8 + 32
        draw.rounded_rectangle([(px, pill_y), (px + pw, pill_y + 36)], radius=8, fill=(2, 18, 19, 230), outline=(*pcol, 160), width=1)
        draw.text((px + 14, pill_y + 9), text, fill=(*pcol, 255), font=font_badge)
        px += pw + 20

    # Save finalized RGB image
    out_path = os.path.join(OUTPUT_DIR, f"{p['id_slug']}.png")
    im.convert('RGB').save(out_path, quality=95)
    return out_path

def render_custom_ui(draw, p, x1, y1, x2, y2, accent):
    kind = p.get('ui_kind', 'default')

    if kind == 'chat':
        # WhatsApp Chat UI
        draw.rounded_rectangle([(x1 + 20, y1 + 18), (x1 + 380, y1 + 68)], radius=10, fill=(3, 35, 36), outline=(10, 112, 117), width=1)
        draw.text((x1 + 34, y1 + 30), p.get('chat_user', "Hi, want to book appointment"), fill=(255, 255, 255), font=font_regular)
        draw.text((x1 + 330, y1 + 45), "10:14 AM", fill=(107, 163, 190), font=font_mono_sm)

        draw.rounded_rectangle([(x2 - 400, y1 + 82), (x2 - 20, y1 + 142)], radius=10, fill=(5, 54, 40), outline=(34, 197, 94), width=1)
        draw.text((x2 - 384, y1 + 94), p.get('chat_bot', "Slot confirmed for Dr. Mehta!"), fill=(255, 255, 255), font=font_bold)
        draw.text((x2 - 384, y1 + 118), "✓ Saved to Google Sheets & Sent SMS", fill=(34, 197, 94), font=font_small)

    elif kind == 'code':
        # Code Editor / Terminal
        draw.text((x1 + 20, y1 + 18), "$ python3 main.py --service=ai-agent", fill=(34, 197, 94), font=font_mono)
        draw.text((x1 + 20, y1 + 46), "[INFO] Connecting to Meta Cloud API Webhook... OK", fill=(107, 163, 190), font=font_mono)
        draw.text((x1 + 20, y1 + 72), "[SUCCESS] LLM Engine Loaded: Claude-3.5 + GPT-4o", fill=(12, 150, 156), font=font_mono)
        draw.text((x1 + 20, y1 + 98), "[ACTIVE] Listening on https://0.0.0.0:8000/webhook", fill=(234, 179, 8), font=font_mono)

    elif kind == 'qr':
        # QR Code Graphic & Scanner
        qr_size = 110
        qx = x1 + 30
        qy = y1 + 20
        draw.rounded_rectangle([(qx, qy), (qx + qr_size, qy + qr_size)], radius=10, fill=(255, 255, 255))
        # Draw QR corners
        draw.rectangle([(qx + 10, qy + 10), (qx + 35, qy + 35)], fill=(0, 0, 0))
        draw.rectangle([(qx + 15, qy + 15), (qx + 30, qy + 30)], fill=(255, 255, 255))
        draw.rectangle([(qx + qr_size - 35, qy + 10), (qx + qr_size - 10, qy + 35)], fill=(0, 0, 0))
        draw.rectangle([(qx + qr_size - 30, qy + 15), (qx + qr_size - 15, qy + 30)], fill=(255, 255, 255))
        draw.rectangle([(qx + 10, qy + qr_size - 35), (qx + 35, qy + qr_size - 10)], fill=(0, 0, 0))
        draw.rectangle([(qx + 15, qy + qr_size - 30), (qx + 30, qy + qr_size - 15)], fill=(255, 255, 255))
        # QR dots
        for dot_x in range(qx + 42, qx + qr_size - 40, 12):
            for dot_y in range(qy + 42, qy + qr_size - 40, 12):
                draw.rectangle([(dot_x, dot_y), (dot_x + 6, dot_y + 6)], fill=(0, 0, 0))
        # Target Info on Right
        draw.text((qx + qr_size + 30, qy + 15), p.get('qr_target', "DYNAMIC TARGET: https://store.link/menu"), fill=(255, 255, 255), font=font_bold)
        draw.text((qx + qr_size + 30, qy + 45), "Total Scans: 14,820 • Unique Visitors: 9,410", fill=(12, 150, 156), font=font_regular)
        draw.text((qx + qr_size + 30, qy + 75), "✓ Editable anytime without changing the printed QR", fill=(34, 197, 94), font=font_small)

    elif kind == 'table':
        # Dashboard Table View
        cols = p.get('table_cols', ["PATIENT / CUSTOMER", "SERVICE", "STATUS", "AMOUNT"])
        cx = x1 + 20
        for c in cols:
            draw.text((cx, y1 + 16), c, fill=(107, 163, 190), font=font_bold)
            cx += 170
        draw.line([(x1 + 16, y1 + 42), (x2 - 16, y1 + 42)], fill=(10, 112, 117, 150), width=1)
        rows = p.get('table_rows', [
            ("Aarav Sharma", "Dental Checkup", "CONFIRMED", "₹800"),
            ("Priya Patel", "Consultation", "PREPARING", "₹1,500")
        ])
        ry = y1 + 54
        for r in rows:
            cx = x1 + 20
            for val in r:
                draw.text((cx, ry), val, fill=(255, 255, 255) if val not in ("CONFIRMED", "PAID") else (34, 197, 94), font=font_regular)
                cx += 170
            ry += 36

    elif kind == 'vault':
        # Mega Vault / Bundle Box
        draw.text((x1 + 30, y1 + 20), "★ ALL-ACCESS MEGA REPOSITORY UNLOCKED ★", fill=(245, 158, 11), font=font_bold)
        draw.text((x1 + 30, y1 + 52), "30+ SaaS Systems & AI Agents Included in Single Package:", fill=(255, 255, 255), font=font_regular)
        draw.text((x1 + 30, y1 + 82), "• WhatsApp Lead Agent • AI Studio Pro • Viral Shorts • QR Suite • Clinic • KOT", fill=(12, 150, 156), font=font_bold)
        draw.text((x1 + 30, y1 + 112), "• Full Unencrypted Source Code • Commercial White-Label License • Lifetime Updates", fill=(34, 197, 94), font=font_regular)

    else:
        # Generic High-Tech Feature Box
        feats = p.get('features', ["100% White-Label SaaS", "Plain PHP & MySQL / Python", "No Monthly Subscriptions", "Instant ZIP Download"])
        fy = y1 + 20
        for f in feats[:3]:
            draw.text((x1 + 30, fy), f"✔ {f}", fill=(255, 255, 255), font=font_bold)
            fy += 38
        draw.text((x1 + 30, fy + 8), p.get('best_for', "Agencies, freelancers, and businesses ready to launch"), fill=(107, 163, 190), font=font_small)

print("Product image builder initialized")
