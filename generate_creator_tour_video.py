import asyncio
import os
import re
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
import edge_tts

BASE_DIR = "/Users/bishal/ai_toolkit_pro_web"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
PRODUCTS_DIR = os.path.join(ASSETS_DIR, "products")
OUTPUT_VIDEO = os.path.join(BASE_DIR, "creator_store_flow_tour.mp4")
AUDIO_FILE = os.path.join(BASE_DIR, "creator_tour_narration.mp3")
FRAMES_DIR = os.path.join(BASE_DIR, "temp_video_frames")
FFMPEG = "/Users/bishal/yt-kids-channel/06_production_assets/bin/ffmpeg"

os.makedirs(FRAMES_DIR, exist_ok=True)

# 1. Narration Script (100% focused on product & website, ZERO commission talk)
SCRIPT_TEXT = (
    "Every creator, animator, and developer wants to build a world-class studio. "
    "But finding the right gear with verified specs and fast delivery can be exhausting. "
    "Welcome to AI Toolkit Pro: the definitive platform built to help creators compare, test, and assemble production-grade setups in minutes. "
    "Explore over 54 battle-tested creator rigs with direct Amazon Prime delivery. "
    "From broadcast-grade Shure SM7B dynamic microphones and Sony 4K cameras, to DJI Pocket 3 gimbals and high-power RTX 4070 rendering workstations. "
    "Power your workflow with dual-motor standing desks and all-day ergonomic seating. "
    "Plus, get instant access to 33 production-ready Micro-SaaS source codes and a completely free Claude Opus 5 studio. "
    "Stop guessing. Build your dream setup this week. "
    "Visit ai-toolkit-pro-eta.vercel.app and unlock the full creator vault today."
)

async def generate_narration():
    print("Generating cinematic neural voiceover with en-US-ChristopherNeural...")
    communicate = edge_tts.Communicate(SCRIPT_TEXT, "en-US-ChristopherNeural", rate="+6%", pitch="+0Hz")
    await communicate.save(AUDIO_FILE)
    print(f"Voiceover saved to {AUDIO_FILE}")

def get_audio_duration(file_path):
    cmd = [
        FFMPEG, "-i", file_path
    ]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    m = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2}\.\d{2})", res.stderr)
    if m:
        h, mn, s = m.groups()
        return int(h) * 3600 + int(mn) * 60 + float(s)
    return 48.0

# Setup Fonts
try:
    font_hero = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 40)
    font_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 34)
    font_pill = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30)
    font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
    font_mono = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 28)
except Exception:
    font_hero = ImageFont.load_default()
    font_sub = font_hero
    font_body = font_hero
    font_pill = font_hero
    font_small = font_hero
    font_mono = font_hero

def load_and_contain_image(img_path, max_w, max_h):
    if not os.path.exists(img_path):
        return None
    try:
        im = Image.open(img_path).convert("RGBA")
        im.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
        return im
    except Exception:
        return None

def render_frame(frame_idx, total_frames, duration):
    t = (frame_idx / total_frames) * duration
    W, H = 1080, 1920
    
    # Dark luxury teal background with pulsing radial glow
    img = Image.new("RGBA", (W, H), (3, 23, 22, 255))
    draw = ImageDraw.Draw(img)

    # Ambient animated background glow
    pulse = math.sin(t * 1.5) * 40
    # Top glow
    draw.ellipse([(W//2 - 400 - int(pulse), -100 - int(pulse)), 
                  (W//2 + 400 + int(pulse), 700 + int(pulse))], fill=(12, 150, 156, 40))
    # Bottom glow
    draw.ellipse([(W//2 - 500, H - 600), (W//2 + 500, H + 400)], fill=(10, 112, 117, 30))

    # Grid background lines
    for x in range(0, W, 90):
        draw.line([(x, 0), (x, H)], fill=(7, 56, 58, 30), width=1)
    for y in range(0, H, 90):
        draw.line([(0, y), (W, y)], fill=(7, 56, 58, 30), width=1)

    # Universal Header Branding (Mobile Safe Top)
    draw.rounded_rectangle([60, 80, W - 60, 160], radius=18, fill=(4, 36, 38, 220), outline=(12, 150, 156, 120), width=2)
    draw.ellipse([(90, 108), (114, 132)], fill=(255, 153, 0))
    draw.text((130, 102), "AI TOOLKIT PRO • CREATOR STORE", font=font_pill, fill=(255, 255, 255))
    draw.text((W - 250, 105), "PRIME 1-DAY", font=font_mono, fill=(0, 168, 225))

    # Scene Director
    # Scene 1: 0.0 - 7.5s (The Creator Problem)
    if t < 7.5:
        # Pill
        draw.rounded_rectangle([W//2 - 250, 240, W//2 + 250, 310], radius=35, fill=(239, 68, 68, 40), outline=(239, 68, 68, 180), width=2)
        draw.text((W//2 - 210, 258), "⚠️ THE CREATOR STRUGGLE", font=font_pill, fill=(255, 100, 100))
        
        draw.text((W//2, 380), "BUILDING A STUDIO", font=font_hero, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 460), "SHOULDN'T BE GUESSWORK", font=font_hero, fill=(255, 153, 0), anchor="mm")

        # Visual Card Box (Centered)
        draw.rounded_rectangle([80, 560, W - 80, 1360], radius=28, fill=(4, 36, 38, 240), outline=(12, 150, 156, 140), width=2)
        
        # Draw question icons & spec hurdles
        draw.text((W//2, 660), "Searching for the right gear?", font=font_sub, fill=(255, 255, 255), anchor="mm")
        
        hurdles = [
            ("❌ Fake or misleading specifications", (255, 120, 120)),
            ("❌ Confusing audio interfaces & XLR cables", (255, 180, 120)),
            ("❌ Weeks of waiting for shipping", (255, 120, 120)),
            ("❌ Overpaying on overpriced retail", (255, 180, 120))
        ]
        hy = 770
        for txt, col in hurdles:
            draw.rounded_rectangle([130, hy, W - 130, hy + 90], radius=16, fill=(3, 23, 22, 220), outline=(12, 150, 156, 80), width=1)
            draw.text((160, hy + 26), txt, font=font_body, fill=col)
            hy += 120

        # Subtitle caption
        draw.rounded_rectangle([80, 1480, W - 80, 1680], radius=22, fill=(3, 23, 22, 230), outline=(255, 153, 0, 140), width=2)
        draw.text((W//2, 1540), "Every creator wants a world-class studio.", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1610), "Here is how to build it without guesswork.", font=font_body, fill=(107, 163, 190), anchor="mm")

    # Scene 2: 7.5 - 17.0s (The Gateway Solution)
    elif t < 17.0:
        draw.rounded_rectangle([W//2 - 280, 240, W//2 + 280, 310], radius=35, fill=(12, 150, 156, 40), outline=(12, 150, 156, 180), width=2)
        draw.text((W//2 - 240, 258), "⚡ THE ALL-IN-ONE SOLUTION", font=font_pill, fill=(12, 150, 156))
        
        draw.text((W//2, 380), "MEET AI TOOLKIT PRO", font=font_hero, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 460), "OFFICIAL CREATOR STORE", font=font_hero, fill=(12, 150, 156), anchor="mm")

        # Feature showcase container
        draw.rounded_rectangle([80, 560, W - 80, 1360], radius=28, fill=(255, 255, 255), outline=None)
        
        # Display authentic gear image
        gear_img = load_and_contain_image(os.path.join(PRODUCTS_DIR, "shure-sm7b-dynamic-vocal-mic.jpg"), 700, 550)
        if gear_img:
            img.paste(gear_img, (W//2 - gear_img.width//2, 600), gear_img)
            
        # Amazon-style overlay badges inside photo
        draw.rounded_rectangle([120, 600, 360, 660], radius=8, fill=(230, 122, 0), outline=None)
        draw.text((140, 616), "#1 Best Seller", font=font_pill, fill=(255, 255, 255))

        draw.rounded_rectangle([120, 1180, W - 120, 1320], radius=16, fill=(4, 36, 38, 250), outline=(12, 150, 156, 160), width=2)
        draw.text((W//2, 1225), "54+ Verified Studio Setups", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1275), "Direct Amazon Prime 1-Day Delivery Across India", font=font_small, fill=(0, 168, 225), anchor="mm")

        # Caption
        draw.rounded_rectangle([80, 1480, W - 80, 1680], radius=22, fill=(3, 23, 22, 230), outline=(12, 150, 156, 140), width=2)
        draw.text((W//2, 1540), "Compare, test, and assemble your rig.", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1610), "Everything tested for YouTubers & 3D animators.", font=font_body, fill=(107, 163, 190), anchor="mm")

    # Scene 3: 17.0 - 27.0s (Audio & Cameras - Shure, Sony, DJI)
    elif t < 27.0:
        draw.rounded_rectangle([W//2 - 270, 240, W//2 + 270, 310], radius=35, fill=(255, 153, 0, 40), outline=(255, 153, 0, 180), width=2)
        draw.text((W//2 - 230, 258), "🎙️ BROADCAST AUDIO & 4K", font=font_pill, fill=(255, 153, 0))

        draw.text((W//2, 380), "FLAGSHIP AUDIO & VIDEO", font=font_hero, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 460), "STUDIO BROADCAST GEAR", font=font_hero, fill=(255, 153, 0), anchor="mm")

        # Dual Showcase Container
        box_w = 420
        # Left Box: Sony ZV-E10
        draw.rounded_rectangle([80, 560, 80 + box_w, 1150], radius=20, fill=(255, 255, 255), outline=None)
        c_img = load_and_contain_image(os.path.join(PRODUCTS_DIR, "sony-alpha-zve10-with-zoom-lens.jpg"), 360, 360)
        if c_img:
            img.paste(c_img, (80 + (box_w - c_img.width)//2, 600), c_img)
        draw.rounded_rectangle([100, 960, 80 + box_w - 20, 1120], radius=12, fill=(4, 36, 38, 250), outline=(12, 150, 156, 120), width=1)
        draw.text((80 + box_w//2, 1000), "Sony Alpha ZV-E10", font=font_pill, fill=(255, 255, 255), anchor="mm")
        draw.text((80 + box_w//2, 1045), "4K 60fps • Real Eye AF", font=font_small, fill=(107, 163, 190), anchor="mm")
        draw.text((80 + box_w//2, 1085), "✔ Prime 1-Day", font=font_small, fill=(0, 168, 225), anchor="mm")

        # Right Box: DJI Osmo Pocket 3
        draw.rounded_rectangle([W - 80 - box_w, 560, W - 80, 1150], radius=20, fill=(255, 255, 255), outline=None)
        d_img = load_and_contain_image(os.path.join(PRODUCTS_DIR, "dji-osmo-pocket-3-creator-combo.jpg"), 360, 360)
        if d_img:
            img.paste(d_img, (W - 80 - box_w + (box_w - d_img.width)//2, 600), d_img)
        draw.rounded_rectangle([W - 80 - box_w + 20, 960, W - 100, 1120], radius=12, fill=(4, 36, 38, 250), outline=(12, 150, 156, 120), width=1)
        draw.text((W - 80 - box_w//2, 1000), "DJI Osmo Pocket 3", font=font_pill, fill=(255, 255, 255), anchor="mm")
        draw.text((W - 80 - box_w//2, 1045), "1' CMOS • 3-Axis Gimbal", font=font_small, fill=(107, 163, 190), anchor="mm")
        draw.text((W - 80 - box_w//2, 1085), "✔ Prime 1-Day", font=font_small, fill=(0, 168, 225), anchor="mm")

        # Wide highlight ribbon below
        draw.rounded_rectangle([80, 1200, W - 80, 1360], radius=18, fill=(4, 36, 38, 240), outline=(255, 153, 0, 140), width=2)
        draw.text((W//2, 1250), "Shure SM7B • Fifine AM8 • Focusrite Scarlett 2i2", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1310), "Full cardioid voice rejection with clean studio preamps", font=font_body, fill=(107, 163, 190), anchor="mm")

        # Caption
        draw.rounded_rectangle([80, 1480, W - 80, 1680], radius=22, fill=(3, 23, 22, 230), outline=(255, 153, 0, 140), width=2)
        draw.text((W//2, 1540), "Broadcast microphones & 4K cameras.", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1610), "Instant uncompressed video capture & podcast audio.", font=font_body, fill=(107, 163, 190), anchor="mm")

    # Scene 4: 27.0 - 37.0s (Workstations, GPUs & Standing Desks)
    elif t < 37.0:
        draw.rounded_rectangle([W//2 - 280, 240, W//2 + 280, 310], radius=35, fill=(59, 130, 246, 40), outline=(59, 130, 246, 180), width=2)
        draw.text((W//2 - 240, 258), "💻 3D RENDERING & WORKSPACE", font=font_pill, fill=(59, 130, 246))

        draw.text((W//2, 380), "FAST WORKSTATIONS", font=font_hero, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 460), "ERGONOMIC SIT-STAND RIGS", font=font_hero, fill=(59, 130, 246), anchor="mm")

        # White Container with RTX 4070 & Standing Desk
        draw.rounded_rectangle([80, 560, W - 80, 1360], radius=28, fill=(255, 255, 255), outline=None)
        
        gpu_img = load_and_contain_image(os.path.join(PRODUCTS_DIR, "zotac-rtx-5060-4070-graphics-card.jpg"), 450, 420)
        if gpu_img:
            img.paste(gpu_img, (120, 600), gpu_img)

        desk_img = load_and_contain_image(os.path.join(PRODUCTS_DIR, "green-soul-jupiter-pro-ergonomic-chair.jpg"), 400, 420)
        if desk_img:
            img.paste(desk_img, (W - 480, 600), desk_img)

        draw.rounded_rectangle([120, 1080, W - 120, 1320], radius=18, fill=(4, 36, 38, 250), outline=(59, 130, 246, 160), width=2)
        draw.text((W//2, 1140), "Zotac RTX 4070 12GB • DLSS 3.5 Frame Gen", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1210), "Jin Office Dual-Motor Desk • Green Soul Ergonomics", font=font_sub, fill=(59, 130, 246), anchor="mm")
        draw.text((W//2, 1270), "Blender 3D & Unreal Engine 5 accelerated rendering", font=font_small, fill=(107, 163, 190), anchor="mm")

        # Caption
        draw.rounded_rectangle([80, 1480, W - 80, 1680], radius=22, fill=(3, 23, 22, 230), outline=(59, 130, 246, 140), width=2)
        draw.text((W//2, 1540), "Power your timeline with RTX rendering.", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1610), "Protect your posture with 10+ hour ergonomic seating.", font=font_body, fill=(107, 163, 190), anchor="mm")

    # Scene 5: 37.0 - 45.0s (Source Codes & Free Claude Opus 5 Studio)
    elif t < 45.0:
        draw.rounded_rectangle([W//2 - 280, 240, W//2 + 280, 310], radius=35, fill=(16, 185, 129, 40), outline=(16, 185, 129, 180), width=2)
        draw.text((W//2 - 240, 258), "🚀 CODE VAULT & AI STUDIO", font=font_pill, fill=(16, 185, 129))

        draw.text((W//2, 380), "33+ PRODUCTION CODES", font=font_hero, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 460), "FREE CLAUDE OPUS 5 STUDIO", font=font_hero, fill=(16, 185, 129), anchor="mm")

        # Grid of Codes & AI Features
        draw.rounded_rectangle([80, 560, W - 80, 1360], radius=28, fill=(4, 36, 38, 240), outline=(16, 185, 129, 140), width=2)
        
        cards_y = 620
        tools = [
            ("⚡ 33+ Micro-SaaS Codes", "Deploy your own apps this week. Own 100% of code."),
            ("🧠 Free Claude Opus 5", "No API key or credit card required. Direct access."),
            ("🎬 YouTube Shorts Engine", "Auto-script, edit, and schedule multi-quest videos."),
            ("💼 Client Booking Portals", "Razorpay & Stripe ready digital checkout systems.")
        ]
        for t_title, t_sub in tools:
            draw.rounded_rectangle([120, cards_y, W - 120, cards_y + 140], radius=16, fill=(3, 23, 22, 240), outline=(16, 185, 129, 90), width=1)
            draw.text((150, cards_y + 35), t_title, font=font_sub, fill=(255, 255, 255))
            draw.text((150, cards_y + 85), t_sub, font=font_small, fill=(16, 185, 129))
            cards_y += 170

        # Caption
        draw.rounded_rectangle([80, 1480, W - 80, 1680], radius=22, fill=(3, 23, 22, 230), outline=(16, 185, 129, 140), width=2)
        draw.text((W//2, 1540), "Own production software without subscriptions.", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1610), "Full code ownership + frontier AI playground.", font=font_body, fill=(107, 163, 190), anchor="mm")

    # Scene 6: 45.0 - End (Call To Action & URL)
    else:
        draw.rounded_rectangle([W//2 - 250, 240, W//2 + 250, 310], radius=35, fill=(255, 153, 0, 40), outline=(255, 153, 0, 180), width=2)
        draw.text((W//2 - 210, 258), "🔥 START BUILDING TODAY", font=font_pill, fill=(255, 153, 0))

        draw.text((W//2, 380), "LEVEL UP YOUR STUDIO", font=font_hero, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 460), "VISIT AI TOOLKIT PRO", font=font_hero, fill=(255, 153, 0), anchor="mm")

        # Big CTA Box
        draw.rounded_rectangle([80, 560, W - 80, 1360], radius=28, fill=(4, 36, 38, 250), outline=(255, 153, 0, 160), width=2)

        draw.text((W//2, 660), "Everything You Need in One Place", font=font_sub, fill=(255, 255, 255), anchor="mm")
        
        # Checklist
        chk = [
            "✔ 54+ Verified Studio & Tech Hardware Rigs",
            "✔ Direct Amazon Prime 1-Day Delivery",
            "✔ 33+ Production-Ready Micro-SaaS Source Codes",
            "✔ Free Anthropic Claude Opus 5 Access",
            "✔ 100% Genuine Brand Warranties"
        ]
        cy = 750
        for c in chk:
            draw.text((140, cy), c, font=font_body, fill=(220, 240, 245))
            cy += 80

        # Big URL Button inside box
        draw.rounded_rectangle([120, 1200, W - 120, 1300], radius=25, fill=(255, 216, 20), outline=None)
        draw.text((W//2, 1250), "ai-toolkit-pro-eta.vercel.app ➔", font=font_sub, fill=(15, 17, 17), anchor="mm")

        # Caption
        draw.rounded_rectangle([80, 1480, W - 80, 1680], radius=22, fill=(3, 23, 22, 230), outline=(255, 153, 0, 140), width=2)
        draw.text((W//2, 1540), "Stop guessing your creator setup.", font=font_sub, fill=(255, 255, 255), anchor="mm")
        draw.text((W//2, 1610), "Explore all 54+ rigs and source codes now.", font=font_body, fill=(107, 163, 190), anchor="mm")

    # Bottom Footer
    draw.text((W//2, H - 90), "ai-toolkit-pro-eta.vercel.app • Verified Studio Tech", font=font_mono, fill=(107, 163, 190, 180), anchor="mm")

    out_frame = os.path.join(FRAMES_DIR, f"frame_{frame_idx:05d}.jpg")
    img.convert("RGB").save(out_frame, "JPEG", quality=90)

async def main():
    await generate_narration()
    dur = get_audio_duration(AUDIO_FILE)
    print(f"Total audio duration: {dur:.2f} seconds")

    fps = 30
    total_frames = int(dur * fps)
    print(f"Rendering {total_frames} frames at {fps} FPS...")

    for i in range(total_frames):
        render_frame(i, total_frames, dur)
        if i % 150 == 0 or i == total_frames - 1:
            print(f"  Frame {i}/{total_frames} ({int(i/total_frames*100)}%)")

    print(f"All {total_frames} frames rendered! Compiling MP4 with FFmpeg...")
    
    cmd = [
        FFMPEG, "-y",
        "-r", str(fps),
        "-i", os.path.join(FRAMES_DIR, "frame_%05d.jpg"),
        "-i", AUDIO_FILE,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "fast",
        "-crf", "20",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    subprocess.run(cmd, check=True)
    print(f"Master Video created at {OUTPUT_VIDEO} ({os.path.getsize(OUTPUT_VIDEO)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
