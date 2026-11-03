import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/Users/bishal/ai_toolkit_pro_web/assets/gear"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fonts
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
except Exception:
    font_hero = ImageFont.load_default()
    font_title = font_hero
    font_price = font_hero
    font_mrp = font_hero
    font_bold = font_hero
    font_regular = font_hero
    font_small = font_hero
    font_badge = font_hero
    font_mono = font_hero

GEAR_PRODUCTS = [
    # =========================================================================
    # 🎙️ AUDIO & STUDIO MICS (14 Products)
    # =========================================================================
    {
        "slug": "fifine-am8-rgb-dynamic-mic",
        "title": "Fifine AmpliGame AM8 Dynamic Mic",
        "subtitle": "XLR & USB-C Dual Output • RGB Aura • Zero-Latency Monitoring",
        "brand": "FIFINE • STUDIO STREAMING",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹5,390",
        "mrp": "₹6,990",
        "discount": "23% OFF",
        "rating": "4.7 ★ (12,000+ Reviews)",
        "badge": "BESTSELLER 2026",
        "accent": (12, 150, 156), # Teal
        "specs": ["XLR & USB-C Dual Connectivity", "Cardioid Capsule & Noise Rejection", "Integrated Mute & Headphone Jack"],
        "url": "https://www.amazon.in/dp/B0BMFQP2ZZ?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission"
    },
    {
        "slug": "fifine-am8t-boom-arm-kit",
        "title": "Fifine AM8T Mic + Boom Arm Kit",
        "subtitle": "Complete Desk Rig • Heavy Duty C-Clamp Arm • Dual XLR/USB",
        "brand": "FIFINE • PRO PODCAST",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹7,490",
        "mrp": "₹9,990",
        "discount": "25% OFF",
        "rating": "4.8 ★ (3,400+ Reviews)",
        "badge": "CREATOR BUNDLE",
        "accent": (14, 165, 233),
        "specs": ["Reinforced Metal Desk Scissor Arm", "Shock-Mount & Built-in Pop Filter", "Touch Mute with LED Indicator"],
        "url": "https://www.amazon.in/dp/B0C74GYW3J?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission"
    },
    {
        "slug": "shure-sm7b-dynamic-vocal-mic",
        "title": "Shure SM7B Vocal Dynamic Studio Mic",
        "subtitle": "The Worldwide Podcasting & Broadcast Standard • Smooth Flat Response",
        "brand": "SHURE • LEGENDARY AUDIO",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹45,641",
        "mrp": "₹54,000",
        "discount": "15% OFF",
        "rating": "4.8 ★ (11,900+ Reviews)",
        "badge": "TOP COMM: ₹1,460",
        "accent": (245, 158, 11), # Gold
        "specs": ["Air-Suspension Shock Isolation", "Electromagnetic Hum Rejection", "Cardioid Polar Pattern for Warm Sound"],
        "url": "https://www.amazon.in/dp/B0002E4Z8M?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹1,460 Payout)"
    },
    {
        "slug": "shure-mv7-plus-podcast-microphone",
        "title": "Shure MV7+ Podcast Microphone (USB-C & XLR)",
        "subtitle": "Hybrid USB-C & XLR • Built-In DSP • Voice Isolation Technology",
        "brand": "SHURE • BROADCAST SERIES",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹26,990",
        "mrp": "₹33,990",
        "discount": "20% OFF",
        "rating": "4.8 ★ (4,100+ Reviews)",
        "badge": "STUDIO UPGRADE",
        "accent": (245, 158, 11),
        "specs": ["Hybrid USB-C & XLR Dual Outputs", "Customizable Multicolor LED Touch Panel", "Digital Popper Stopper & Real-Time Denoiser"],
        "url": "https://www.amazon.in/dp/B0CY6HDFY5?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹860 Payout)"
    },
    {
        "slug": "rode-wireless-go-ii-dual-channel-mic",
        "title": "Røde Wireless GO II Dual Wireless System",
        "subtitle": "Dual-Channel Wireless Mic • 200m Range • Onboard Recording 24+ Hrs",
        "brand": "RØDE • WIRELESS MOBILE",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹27,490",
        "mrp": "₹34,990",
        "discount": "21% OFF",
        "rating": "4.6 ★ (8,900+ Reviews)",
        "badge": "TOP CREATOR RIG",
        "accent": (14, 165, 233),
        "specs": ["200m Range Ultra-Stable 2.4GHz Digital Transmission", "Dual Channel: Record 2 Presenters Simultaneously", "On-Board Recording: 40+ Hours Internal Audio Memory"],
        "url": "https://www.amazon.in/dp/B08XFQ6KP9?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹880 Payout)"
    },
    {
        "slug": "focusrite-scarlett-2i2-4th-gen",
        "title": "Focusrite Scarlett 2i2 4th Gen Interface",
        "subtitle": "120dB Dynamic Range • Auto Gain & Clip Safe • Pro Studio Preamps",
        "brand": "FOCUSRITE • 4TH GEN",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹22,800",
        "mrp": "₹49,999",
        "discount": "54% OFF",
        "rating": "4.6 ★ (2,700+ Reviews)",
        "badge": "TOP COMM: ₹730",
        "accent": (239, 68, 68), # Red
        "specs": ["Flagship 192kHz/24-bit RedNet Converters", "Air Mode for Rich Acoustic Sparkle", "Custom Amp Headphone Output"],
        "url": "https://www.amazon.in/dp/B0C5JRTS3Y?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission"
    },
    {
        "slug": "focusrite-scarlett-2i2-studio-bundle",
        "title": "Focusrite Scarlett 2i2 Studio 4th Gen Pack",
        "subtitle": "Complete Recording Bundle • CM25 MkIII Condenser + SH-450 Cans",
        "brand": "FOCUSRITE • PRO PACK",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹32,500",
        "mrp": "₹59,999",
        "discount": "46% OFF",
        "rating": "4.7 ★ (1,500+ Reviews)",
        "badge": "COMPLETE STUDIO RIG",
        "accent": (239, 68, 68),
        "specs": ["Includes Studio Condenser Mic & XLR Cable", "Includes Closed-Back Monitoring Headphones", "Hitmaker Expansion Suite Included (Pro Tools, Ableton)"],
        "url": "https://www.amazon.in/dp/B0C5JSHQY4?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹1,040 Payout)"
    },
    {
        "slug": "elgato-stream-deck-mk2",
        "title": "Elgato Stream Deck MK.2 (15 LCD Keys)",
        "subtitle": "15 Customizable LCD Macro Keys • Hotkeys, Scene Switching & OBS Control",
        "brand": "ELGATO • STUDIO CONTROL",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹15,499",
        "mrp": "₹19,999",
        "discount": "22% OFF",
        "rating": "4.8 ★ (18,000+ Reviews)",
        "badge": "STREAM MUST-HAVE",
        "accent": (14, 165, 233),
        "specs": ["15 Custom LCD Keys with Visual Feedback", "Instant Triggers for OBS, Spotify, Discord, Philips Hue", "Detachable 45° Ergonomic Stand Included"],
        "url": "https://www.amazon.in/dp/B09738CV2G?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "audio-technica-at2020-condenser",
        "title": "Audio-Technica AT2020 Cardioid Studio Mic",
        "subtitle": "Studio Condenser Mic • High SPL Handling • Wide Dynamic Range",
        "brand": "AUDIO-TECHNICA • PRO",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹7,990",
        "mrp": "₹12,490",
        "discount": "36% OFF",
        "rating": "4.7 ★ (22,000+ Reviews)",
        "badge": "LEGENDARY VALUE",
        "accent": (168, 85, 247),
        "specs": ["Custom-Engineered Low-Mass Diaphragm", "Cardioid Polar Pattern Isolates Vocal Source", "Handles High SPL Levels with Ease"],
        "url": "https://www.amazon.in/dp/B0006H92QK?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission"
    },
    {
        "slug": "rode-podmic-dynamic-podcasting-mic",
        "title": "Røde PodMic Broadcast Dynamic Mic",
        "subtitle": "Integrated Pop Filter • Rugged All-Metal Construction • Rich Vocal Tone",
        "brand": "RØDE • PODCASTING",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹10,500",
        "mrp": "₹14,990",
        "discount": "30% OFF",
        "rating": "4.8 ★ (8,500+ Reviews)",
        "badge": "BROADCAST GRADE",
        "accent": (234, 88, 12),
        "specs": ["Broadcast-Quality Dynamic Capsule", "Internal Plosive Pop Shield", "Integrated Swing Mount for Mic Arm"],
        "url": "https://www.amazon.in/dp/B07MS612CV?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission"
    },
    {
        "slug": "beyerdynamic-dt-770-pro-80-ohm",
        "title": "Beyerdynamic DT 770 PRO 80 Ohm Studio Cans",
        "subtitle": "Closed-Back Studio Reference • Bass Reflex • Velour Ear Pads",
        "brand": "BEYERDYNAMIC • STUDIO MONITORING",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹12,490",
        "mrp": "₹16,990",
        "discount": "26% OFF",
        "rating": "4.7 ★ (18,000+ Reviews)",
        "badge": "INDUSTRY STANDARD",
        "accent": (12, 150, 156),
        "specs": ["Detailed Audio Reproduction (5 - 35,000 Hz)", "Extreme Comfort Velour Ear Pads for 12hr Sessions", "High Ambient Noise Attenuation (Closed-Back)"],
        "url": "https://www.amazon.in/dp/B0016MNAAI?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹400 Payout)"
    },
    {
        "slug": "elgato-wave-3-premium-usb-mic",
        "title": "Elgato Wave:3 Premium USB Condenser Mic",
        "subtitle": "Clipguard Anti-Distortion • 24-bit 96kHz • Wave Link Digital Mixer",
        "brand": "ELGATO • STREAMING AUDIO",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹13,999",
        "mrp": "₹18,990",
        "discount": "26% OFF",
        "rating": "4.6 ★ (7,300+ Reviews)",
        "badge": "STREAMER CHOICE",
        "accent": (14, 165, 233),
        "specs": ["Proprietary Clipguard Anti-Clipping Distortion", "Wave Link App Controls Up to 9 Audio Inputs", "Capacitive Touch Mute with LED Halo Ring"],
        "url": "https://www.amazon.in/dp/B088HH405J?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹448 Payout)"
    },
    {
        "slug": "fifine-k688-usb-xlr-podcast-mic",
        "title": "Fifine K688 Dynamic USB & XLR Studio Mic",
        "subtitle": "Cardioid Broadcast Pattern • Headphone Volume & Gain Knobs",
        "brand": "FIFINE • BROADCAST VALUE",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹6,290",
        "mrp": "₹8,490",
        "discount": "26% OFF",
        "rating": "4.7 ★ (5,200+ Reviews)",
        "badge": "BUDGET BEAST",
        "accent": (12, 150, 156),
        "specs": ["Clean Dynamic Capsule: Rejects AC/Fan & Room Echo", "Direct Headphone Jack with Zero-Latency Monitoring", "Includes Shock Mount & Standard Thread Adapter"],
        "url": "https://www.amazon.in/dp/B0B2F5X5M4?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission"
    },
    {
        "slug": "rode-psa1-plus-professional-boom-arm",
        "title": "Røde PSA1+ Professional Studio Boom Arm",
        "subtitle": "Silent Damped Springs • 360° Rotation • Integrated Cable Management",
        "brand": "RØDE • STUDIO HARDWARE",
        "category": "audio",
        "category_name": "Studio & Audio",
        "price": "₹11,990",
        "mrp": "₹15,490",
        "discount": "23% OFF",
        "rating": "4.8 ★ (3,900+ Reviews)",
        "badge": "SILENT SPRING ARM",
        "accent": (234, 88, 12),
        "specs": ["Completely Silent Movement with Damped Springs", "Supports Heavy Mics Up to 1.2kg (SM7B, PodMic, MV7+)", "Desk Clamp & In-Desk Grommet Mounts Included"],
        "url": "https://www.amazon.in/dp/B09KTGQ7B5?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "3.2% Commission (₹383 Payout)"
    },

    # =========================================================================
    # 🎥 CAMERAS, LENSES & LIGHTING (12 Products)
    # =========================================================================
    {
        "slug": "dji-osmo-pocket-3-creator-combo",
        "title": "DJI Osmo Pocket 3 Creator Combo 4K/120fps",
        "subtitle": "1-Inch CMOS Sensor • 3-Axis Gimbal • 2' Rotating OLED Touchscreen",
        "brand": "DJI • VLOG & MOBILE PRODUCTION",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹54,990",
        "mrp": "₹68,990",
        "discount": "20% OFF",
        "rating": "4.8 ★ (4,600+ Reviews)",
        "badge": "TOP COMM: ₹1,446",
        "accent": (245, 158, 11),
        "specs": ["1-Inch CMOS Sensor: Astounding Low-Light Performance", "True 4K/120fps Slow-Mo & 10-bit D-Log M Color Profile", "Creator Combo: Wireless Mic 2 + Battery Handle Included"],
        "url": "https://www.amazon.in/dp/B0CL5K7443?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.63% Commission (₹1,446 Payout)"
    },
    {
        "slug": "sony-alpha-zve10-camera-body",
        "title": "Sony Alpha ZV-E10 4K Creator Camera (Body)",
        "subtitle": "24.2 MP APS-C Sensor • Product Showcase Setting • Real-time Eye AF",
        "brand": "SONY • VLOGGING SERIES",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹56,990",
        "mrp": "₹69,990",
        "discount": "19% OFF",
        "rating": "4.6 ★ (3,200+ Reviews)",
        "badge": "TOP COMM: ₹1,500",
        "accent": (245, 158, 11),
        "specs": ["APS-C Sensor with Cinematic Background Defocus", "Directional 3-Capsule Mic with Windscreen", "Clean HDMI Out for 4K Studio Streaming"],
        "url": "https://www.amazon.in/dp/B09F9QMR1T?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.63% Commission (₹1,500 Payout)"
    },
    {
        "slug": "sony-alpha-zve10-with-zoom-lens",
        "title": "Sony Alpha ZV-E10 + 16-50mm Power Zoom",
        "subtitle": "Interchangeable Lens Kit • Flip Screen • 4K HDR • Instant Webcam",
        "brand": "SONY • COMPLETE RIG",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹65,990",
        "mrp": "₹79,990",
        "discount": "18% OFF",
        "rating": "4.7 ★ (4,100+ Reviews)",
        "badge": "TOP COMM: ₹1,735",
        "accent": (245, 158, 11),
        "specs": ["Includes 16-50mm Power Zoom Lens (SELP1650)", "Vari-Angle LCD Screen for Perfect Vlogging", "4K HDR (HLG) Video Recording & S-Log Profiles"],
        "url": "https://www.amazon.in/dp/B09F9YCGCR?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.63% Commission (₹1,735 Payout)"
    },
    {
        "slug": "sigma-16mm-f14-dc-dn-contemporary-lens",
        "title": "Sigma 16mm f/1.4 DC DN Contemporary Lens",
        "subtitle": "Ultra-Wide Prime • f/1.4 Massive Aperture • Cinematic Creamy Bokeh",
        "brand": "SIGMA • CINEMA OPTICS",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹28,490",
        "mrp": "₹36,000",
        "discount": "21% OFF",
        "rating": "4.8 ★ (6,800+ Reviews)",
        "badge": "CREAMY BOKEH LENS",
        "accent": (245, 158, 11),
        "specs": ["Huge f/1.4 Maximum Aperture for Ultra Creamy Bokeh", "16mm Wide Angle (24mm Equiv) Ideal for Desk Setup", "Stepping AF Motor for Silent & Smooth Autofocus"],
        "url": "https://www.amazon.in/dp/B077BWD2BB?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.63% Commission (₹749 Payout)"
    },
    {
        "slug": "godox-sl60w-continuous-led-video-light",
        "title": "Godox SL60W 5600K Continuous LED Light",
        "subtitle": "60W High Power • Bowens Mount • 93+ CRI / 95+ TLCI Studio Daylight",
        "brand": "GODOX • STUDIO LIGHTING",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹9,990",
        "mrp": "₹14,500",
        "discount": "31% OFF",
        "rating": "4.7 ★ (8,100+ Reviews)",
        "badge": "STUDIO KEY LIGHT",
        "accent": (245, 158, 11),
        "specs": ["5600K Daylight Balanced Studio Key Light", "Bowens Mount: Fits Softboxes, Lanterns & Grids", "Ultra-Silent Heat Sink Cooling for Noise-Free Audio"],
        "url": "https://www.amazon.in/dp/B077B8475F?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission (₹425 Payout)"
    },
    {
        "slug": "neewer-660-led-video-light-2pack-kit",
        "title": "Neewer 2-Pack Dimmable Bi-Color 660 LED Light Kit",
        "subtitle": "3200K-5600K • 6.5ft Light Stands • Barndoors & Carrying Case",
        "brand": "NEEWER • DUAL LIGHT RIG",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹14,999",
        "mrp": "₹22,990",
        "discount": "35% OFF",
        "rating": "4.6 ★ (9,400+ Reviews)",
        "badge": "2-POINT LIGHTING KIT",
        "accent": (245, 158, 11),
        "specs": ["660 Individual LED Beads (330 White + 330 Yellow)", "3200K to 5600K Bi-Color Dial Adjustment & CRI 96+", "Includes 2 Solid Metal Light Stands & Padded Carrying Bag"],
        "url": "https://www.amazon.in/dp/B07X1V5QPB?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission (₹637 Payout)"
    },
    {
        "slug": "kreo-slab-led-video-light",
        "title": "Kreo Slab Adjustable LED Video Light",
        "subtitle": "Bi-Color Warm to Daylight • Desk Clamp Mount • Ultra-Thin Edge Lit",
        "brand": "KREO • INDIAN CREATOR GEAR",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹4,299",
        "mrp": "₹6,999",
        "discount": "39% OFF",
        "rating": "4.5 ★ (980+ Reviews)",
        "badge": "VALUE LIGHT",
        "accent": (245, 158, 11),
        "specs": ["Edge-Lit Diffusion: Zero Eye Strain", "3200K - 5600K Adjustable Temperature", "Multi-Angle Heavy Duty Desk Clamp"],
        "url": "https://www.amazon.in/dp/B0CKYSLNQ8?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission"
    },
    {
        "slug": "elgato-key-light-professional-panel",
        "title": "Elgato Key Light Professional Panel",
        "subtitle": "2800 Lumens • App & Stream Deck Control • 2900K - 7000K Color Temp",
        "brand": "ELGATO • STUDIO LIGHT",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹18,990",
        "mrp": "₹25,999",
        "discount": "27% OFF",
        "rating": "4.7 ★ (4,900+ Reviews)",
        "badge": "TOP COMM: ₹800",
        "accent": (245, 158, 11),
        "specs": ["2800 Lumens Ultra-Bright Edge-Lit LEDs", "Wi-Fi Enabled: Adjust from PC, Mac, iPhone, Android", "Master Mount S Clamp Included"],
        "url": "https://www.amazon.in/dp/B07L755X9G?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission"
    },
    {
        "slug": "elgato-cam-link-4k-usb-capture",
        "title": "Elgato Cam Link 4K USB Broadcast Capture",
        "subtitle": "DSLR/Mirrorless to 4K Webcam • Ultra-Low Latency • HDMI to USB",
        "brand": "ELGATO • BROADCAST CAPTURE",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹11,490",
        "mrp": "₹15,999",
        "discount": "28% OFF",
        "rating": "4.7 ★ (11,000+ Reviews)",
        "badge": "4K DSLR STREAM CARD",
        "accent": (245, 158, 11),
        "specs": ["Turns Sony, Canon, Nikon DSLR into High-End 4K Webcam", "Broadcast in Up to 4K 30fps or 1080p 60fps", "Plug & Play on Windows and macOS via USB 3.0"],
        "url": "https://www.amazon.in/dp/B07K3FN5KQ?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.80% Commission (₹321 Payout)"
    },
    {
        "slug": "ulanzi-vl49-rgb-pocket-led-light",
        "title": "Ulanzi VL49 RGB Pocket LED Video Light",
        "subtitle": "2000mAh Battery • Full Color RGB • 3 Cold Shoe Mounts",
        "brand": "ULANZI • PORTABLE LIGHTING",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹1,999",
        "mrp": "₹2,999",
        "discount": "33% OFF",
        "rating": "4.5 ★ (4,800+ Reviews)",
        "badge": "POCKET RGB LIGHT",
        "accent": (245, 158, 11),
        "specs": ["360° Full RGB Hues + 2500K-9000K Color Temperature", "Built-In 2000mAh Rechargeable Battery (Up to 10hrs)", "3 Cold Shoe Mounts for Expanding Mics & Lights"],
        "url": "https://www.amazon.in/dp/B0892D4K2Q?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission (₹85 Payout)"
    },
    {
        "slug": "logitech-brio-4k-ultra-hd-webcam",
        "title": "Logitech Brio 4K Ultra HD Webcam",
        "subtitle": "RightLight 3 with HDR • Dual Noise-Canceling Mics • Windows Hello",
        "brand": "LOGITECH • PRO VIDEO",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹17,490",
        "mrp": "₹24,995",
        "discount": "30% OFF",
        "rating": "4.5 ★ (15,000+ Reviews)",
        "badge": "4K HDR WEBCAM",
        "accent": (14, 165, 233),
        "specs": ["True 4K Streaming at 30fps or 1080p at 60fps", "HDR Automatic Low-Light Correction", "Adjustable Field of View (65°, 78°, 90°)"],
        "url": "https://www.amazon.in/dp/B01N5NYRES?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "logitech-c922-pro-stream-webcam",
        "title": "Logitech C922 Pro Stream Webcam",
        "subtitle": "Full 1080p at 30fps / 720p at 60fps • Free Tripod Included",
        "brand": "LOGITECH • STREAMING",
        "category": "video",
        "category_name": "Cameras & Lighting",
        "price": "₹8,490",
        "mrp": "₹12,995",
        "discount": "35% OFF",
        "rating": "4.6 ★ (25,000+ Reviews)",
        "badge": "PROVEN VALUE",
        "accent": (14, 165, 233),
        "specs": ["Smooth 60fps in 720p for Fast Motion", "Dual Stereo Microphones for Clean Capture", "Automatic Autofocus and Light Correction"],
        "url": "https://www.amazon.in/dp/B01LXCDPPK?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },

    # =========================================================================
    # 💻 WORKSTATIONS, GPUS & HARDWARE (12 Products)
    # =========================================================================
    {
        "slug": "zotac-rtx-5060-4070-graphics-card",
        "title": "Zotac Gaming GeForce RTX 4070 Super / 5060 GPU",
        "subtitle": "12GB GDDR6X • DLSS 3.5 AI Frame Generation • 3D Blender Fast Render",
        "brand": "ZOTAC GAMING • GPU",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹59,990",
        "mrp": "₹74,990",
        "discount": "20% OFF",
        "rating": "4.7 ★ (2,100+ Reviews)",
        "badge": "TOP COMM: ₹1,680",
        "accent": (59, 130, 246), # Electric Blue
        "specs": ["NVIDIA Ada Lovelace Architecture & 12GB VRAM", "Unmatched Blender 3D & Unreal Engine 5 Acceleration", "IceStorm 2.0 Advanced Cooling with Dual Fans"],
        "url": "https://www.amazon.in/dp/B0F8T73MZP?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission (₹1,680 Payout)"
    },
    {
        "slug": "zotac-rtx-4060-twin-edge-gpu",
        "title": "Zotac Gaming GeForce RTX 4060 8GB OC",
        "subtitle": "Compact Dual Fan • Ray Tracing Cores • Budget 3D Rendering Beast",
        "brand": "ZOTAC • BUDGET GPU",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹28,990",
        "mrp": "₹36,000",
        "discount": "19% OFF",
        "rating": "4.6 ★ (3,800+ Reviews)",
        "badge": "TOP COMM: ₹810",
        "accent": (59, 130, 246),
        "specs": ["8GB GDDR6 VRAM with DLSS 3 Support", "Low 115W Power Consumption", "Dual Slot Compact Design Fits Any Micro-ATX Case"],
        "url": "https://www.amazon.in/dp/B0C8JY4599?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission (₹810 Payout)"
    },
    {
        "slug": "amd-ryzen-9-7900x-desktop-processor",
        "title": "AMD Ryzen 9 7900X 12-Core 24-Thread CPU",
        "subtitle": "5.6 GHz Max Boost • Zen 4 Architecture • 76MB Cache • PCIe 5.0",
        "brand": "AMD • WORKSTATION CPU",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹38,990",
        "mrp": "₹54,990",
        "discount": "29% OFF",
        "rating": "4.7 ★ (3,100+ Reviews)",
        "badge": "TOP COMM: ₹1,091",
        "accent": (239, 68, 68),
        "specs": ["12 Cores & 24 Processing Threads for Blender & After Effects", "Up to 5.6 GHz Max Boost Clock with DDR5 Support", "PCIe 5.0 Ready for Ultra-Fast Next-Gen NVMe SSDs"],
        "url": "https://www.amazon.in/dp/B0BBJ59WJ4?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission (₹1,091 Payout)"
    },
    {
        "slug": "samsung-990-pro-2tb-nvme-ssd",
        "title": "Samsung 990 PRO 2TB PCIe 4.0 NVMe SSD",
        "subtitle": "Up to 7,450 MB/s Read Speed • V-NAND TLC • Video Timeline Caching",
        "brand": "SAMSUNG • FASTEST SSD",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹16,999",
        "mrp": "₹28,999",
        "discount": "41% OFF",
        "rating": "4.8 ★ (14,000+ Reviews)",
        "badge": "TOP SPEED SSD",
        "accent": (14, 165, 233),
        "specs": ["Blazing 7450 MB/s Sequential Read Speeds", "Nickel-Coated Controller & Smart Heat Management", "Perfect for 4K 60fps Multi-Cam Premiere Pro Timelines"],
        "url": "https://www.amazon.in/dp/B0BHJJ9Y77?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "crucial-p3-plus-1tb-nvme-ssd",
        "title": "Crucial P3 Plus 1TB PCIe 4.0 3D NAND SSD",
        "subtitle": "Up to 5,000 MB/s Read • Fast Game & Project Loading • Gen4 Performance",
        "brand": "CRUCIAL • STORAGE VALUE",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹6,199",
        "mrp": "₹10,500",
        "discount": "41% OFF",
        "rating": "4.6 ★ (28,000+ Reviews)",
        "badge": "BESTSELLER SSD",
        "accent": (14, 165, 233),
        "specs": ["5000 MB/s Reads: 8.9x Faster than SATA SSDs", "Gen4 NVMe Technology at Budget Gen3 Pricing", "Micron Advanced 3D NAND Flash Memory"],
        "url": "https://www.amazon.in/dp/B0B25NXWC7?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "corsair-vengeance-ddr5-32gb-ram",
        "title": "Corsair Vengeance DDR5 32GB (2x16GB) RAM",
        "subtitle": "6000MHz CL36 Intel XMP / AMD EXPO • Aluminum Heat Spreader",
        "brand": "CORSAIR • HIGH SPEED RAM",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹10,490",
        "mrp": "₹16,500",
        "discount": "36% OFF",
        "rating": "4.7 ★ (6,500+ Reviews)",
        "badge": "DDR5 WORKSTATION",
        "accent": (245, 158, 11),
        "specs": ["6000MHz Ultra-Fast DDR5 Memory Frequency", "Custom Performance PCB for Signal Quality", "Onboard Voltage Regulation for Easy Overclocking"],
        "url": "https://www.amazon.in/dp/B0B7748V6K?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "samsung-odyssey-g7-32-inch-curved-gaming-monitor",
        "title": "Samsung Odyssey G7 32-Inch 1000R 240Hz Monitor",
        "subtitle": "QHD 2560x1440 • QLED Quantum Dot • 1ms GtG • G-Sync Compatible",
        "brand": "SAMSUNG • CURVED PRO DISPLAY",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹44,990",
        "mrp": "₹62,000",
        "discount": "27% OFF",
        "rating": "4.6 ★ (4,200+ Reviews)",
        "badge": "TOP COMM: ₹1,259",
        "accent": (59, 130, 246),
        "specs": ["Deep 1000R Curvature Matches Human Eye Field of View", "Blistering 240Hz Refresh Rate with 1ms Fast Response", "QLED Quantum Dot Technology with 125% sRGB Coverage"],
        "url": "https://www.amazon.in/dp/B086BL7NNS?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission (₹1,259 Payout)"
    },
    {
        "slug": "lg-ultragear-27-inch-qhd-nano-ips-monitor",
        "title": "LG UltraGear 27-inch QHD Nano IPS Monitor",
        "subtitle": "2560x1440 • 165Hz Refresh Rate • 1ms GtG • DCI-P3 98% Accurate Color",
        "brand": "LG • COLOR ACCURATE IPS",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹24,990",
        "mrp": "₹37,000",
        "discount": "32% OFF",
        "rating": "4.6 ★ (5,200+ Reviews)",
        "badge": "COLOR ACCURATE",
        "accent": (239, 68, 68),
        "specs": ["Nano IPS Display with 98% DCI-P3 Color Gamut", "HDR10 & NVIDIA G-Sync / AMD FreeSync Premium", "Pivot, Height & Tilt Ergonomic Stand"],
        "url": "https://www.amazon.in/dp/B09V7DY8NW?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "logitech-mx-master-3s-wireless-mouse",
        "title": "Logitech MX Master 3S Wireless Mouse",
        "subtitle": "8K DPI Any-Surface Tracking • Quiet Clicks • MagSpeed Scroll",
        "brand": "LOGITECH • PRO PRODUCTIVITY",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹8,995",
        "mrp": "₹10,995",
        "discount": "18% OFF",
        "rating": "4.7 ★ (16,000+ Reviews)",
        "badge": "#1 CREATOR MOUSE",
        "accent": (59, 130, 246),
        "specs": ["MagSpeed Electromagnetic Scroll: 1,000 Lines Per Second", "8,000 DPI Sensor Tracks Even on Glass Surfaces", "Quiet Clicks (90% Less Noise) & Multi-Device Flow"],
        "url": "https://www.amazon.in/dp/B0B11LDY4R?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission (₹252 Payout)"
    },
    {
        "slug": "keychron-k2-wireless-mechanical-keyboard",
        "title": "Keychron K2 Wireless Mechanical Keyboard",
        "subtitle": "75% Compact Layout • Gateron G Pro Switches • Mac & Windows Keys",
        "brand": "KEYCHRON • MECHANICAL KEYS",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹8,499",
        "mrp": "₹10,999",
        "discount": "23% OFF",
        "rating": "4.6 ★ (2,800+ Reviews)",
        "badge": "CODER & CREATOR FAVORITE",
        "accent": (59, 130, 246),
        "specs": ["Connects Up to 3 Devices via Bluetooth 5.1 or Type-C", "Dedicated Mac Layout with Option/Command Keys Included", "4000mAh Battery: Up to 240 Hours Typing Time"],
        "url": "https://www.amazon.in/dp/B08669NZM6?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission (₹238 Payout)"
    },
    {
        "slug": "asus-rog-strix-850w-gold-psu",
        "title": "ASUS ROG Strix 850W Gold Modular PSU",
        "subtitle": "80 Plus Gold Certified • Axial-Tech Fan • 10-Year Warranty",
        "brand": "ASUS ROG • POWER SUPPLY",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹14,990",
        "mrp": "₹21,000",
        "discount": "29% OFF",
        "rating": "4.8 ★ (1,800+ Reviews)",
        "badge": "10-YEAR WARRANTY",
        "accent": (239, 68, 68),
        "specs": ["ROG Heatsinks cover critical components for 0dB silent operation", "Japanese 105°C Capacitors ensure continuous clean power", "Fully modular cables for ultra-clean workstation cable management"],
        "url": "https://www.amazon.in/dp/B08851B97C?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },
    {
        "slug": "ant-esports-ice-511mt-mesh-cabinet",
        "title": "Ant Esports ICE-511MT Mid Tower Cabinet",
        "subtitle": "High Airflow Mesh Front • 4x Auto-RGB 120mm Fans Included",
        "brand": "ANT ESPORTS • PC CASE",
        "category": "hardware",
        "category_name": "Workstations & GPUs",
        "price": "₹4,290",
        "mrp": "₹7,999",
        "discount": "46% OFF",
        "rating": "4.4 ★ (4,100+ Reviews)",
        "badge": "COOL AIRFLOW",
        "accent": (14, 165, 233),
        "specs": ["Front Diamond Mesh Panel for High Air Intake", "Pre-Installed 4x 120mm RGB Fans with Lighting Control", "Supports Up to 360mm Liquid Cooler Radiator on Front"],
        "url": "https://www.amazon.in/dp/B0821M9K7F?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.8% Commission"
    },

    # =========================================================================
    # 🪑 WORKSPACE & ERGONOMICS (9 Products)
    # =========================================================================
    {
        "slug": "green-soul-jupiter-pro-ergonomic-chair",
        "title": "Green Soul Jupiter Pro Ergonomic Chair",
        "subtitle": "High Back Breathable Mesh • 2D Adjustable Lumbar • 3-Year Warranty",
        "brand": "GREEN SOUL • ERGONOMICS",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹8,990",
        "mrp": "₹17,490",
        "discount": "49% OFF",
        "rating": "4.4 ★ (14,200+ Reviews)",
        "badge": "TOP COMM: 4.72%",
        "accent": (34, 197, 94), # Green
        "specs": ["High-Density Molded Foam Seat Cushion (10+ hr comfort)", "2D Headrest & 2D Armrest for Posture Alignment", "Heavy Duty Metal Base Tested for Up to 125kg Weight"],
        "url": "https://www.amazon.in/dp/B0D46XSFYG?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.72% Commission (₹424 Payout)"
    },
    {
        "slug": "green-soul-monster-ultimate-creator-chair",
        "title": "Green Soul Monster Ultimate Creator Chair",
        "subtitle": "SpandX Fabric Breathable Weave • Memory Foam Lumbar • 4D Armrests",
        "brand": "GREEN SOUL • FLAGSHIP",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹18,490",
        "mrp": "₹32,990",
        "discount": "44% OFF",
        "rating": "4.6 ★ (8,900+ Reviews)",
        "badge": "TOP COMM: ₹870",
        "accent": (34, 197, 94),
        "specs": ["Breathable SpandX Cool Fabric (Zero Sweat in Hot Climates)", "Magnetic Memory Foam Headrest & Lumbar Cushion", "180° Full Recline with Multi-Angle Tilt Lock"],
        "url": "https://www.amazon.in/dp/B09V7N7Y6T?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.72% Commission (₹870 Payout)"
    },
    {
        "slug": "featherlite-liberate-high-back-chair",
        "title": "Featherlite Liberate Game High Back Chair",
        "subtitle": "Dynaflex Dynamic Back Support • Multi-Lock Synchronous Mechanism",
        "brand": "FEATHERLITE • PREMIUM SEATING",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹14,990",
        "mrp": "₹21,500",
        "discount": "30% OFF",
        "rating": "4.5 ★ (4,900+ Reviews)",
        "badge": "TOP COMM: ₹707",
        "accent": (168, 85, 247),
        "specs": ["Dynaflex Dynamic System Moves with Your Spine Continuously", "Breathable Mesh Back Keeps Back Cool in Indian Summer", "3-Year Manufacturer Warranty & Class 4 Gas Lift"],
        "url": "https://www.amazon.in/dp/B07W94Q3V9?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.72% Commission (₹707 Payout)"
    },
    {
        "slug": "jin-office-motorized-electric-standing-desk",
        "title": "Jin Office Dual Motor Electric Standing Desk",
        "subtitle": "Solid 140x70cm Teak Top • 4 Preset Memory Heights • Anti-Collision",
        "brand": "JIN OFFICE • SIT-STAND RIG",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹24,990",
        "mrp": "₹39,990",
        "discount": "38% OFF",
        "rating": "4.7 ★ (1,100+ Reviews)",
        "badge": "TOP COMM: ₹1,060",
        "accent": (245, 158, 11),
        "specs": ["Dual Heavy-Duty Electric Motors Lift Up to 100kg", "Smooth 35mm/s Height Adjustment from 71cm to 117cm", "Digital Display with 4 One-Touch Memory Presets"],
        "url": "https://www.amazon.in/dp/B09G3B7X1P?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission (₹1,060 Payout)"
    },
    {
        "slug": "benq-screenbar-halo-wireless-monitor-light",
        "title": "BenQ ScreenBar Halo Wireless Monitor Light",
        "subtitle": "Zero Screen Glare • Wireless Controller • Backlight Ambient Glow",
        "brand": "BENQ • DESK ERGONOMICS",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹15,990",
        "mrp": "₹19,990",
        "discount": "20% OFF",
        "rating": "4.8 ★ (3,500+ Reviews)",
        "badge": "ZERO-GLARE LIGHT",
        "accent": (168, 85, 247),
        "specs": ["Patented Asymmetrical Optical Design: Zero Screen Glare", "Wireless Smart Rotary Controller with Precision Touch", "Front & Rear Dual Illumination for True Eye Comfort"],
        "url": "https://www.amazon.in/dp/B09NLHBC2L?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission (₹679 Payout)"
    },
    {
        "slug": "elgato-prompter-studio-teleprompter",
        "title": "Elgato Prompter - Studio Teleprompter & 9' Display",
        "subtitle": "Built-In 9' Screen • True Eye Contact • Direct OBS & Stream Deck Integration",
        "brand": "ELGATO • BROADCAST HARDWARE",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹27,990",
        "mrp": "₹34,999",
        "discount": "20% OFF",
        "rating": "4.7 ★ (1,800+ Reviews)",
        "badge": "DIRECT EYE CONTACT",
        "accent": (168, 85, 247),
        "specs": ["Built-In 9-Inch Monitor: No Secondary Tablet/Phone Required", "Direct Eye Contact with Video Viewers While Reading Scripts", "Single USB-C Cable Powers Display & Direct Stream Deck Integration"],
        "url": "https://www.amazon.in/dp/B0CHXG534G?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.80% Commission (₹783 Payout)"
    },
    {
        "slug": "huion-kamvas-16-graphics-drawing-tablet",
        "title": "Huion Kamvas 16 Full HD Pen Display Tablet",
        "subtitle": "15.6' IPS Anti-Glare Screen • 8192 Pressure Levels • Battery-Free Stylus",
        "brand": "HUION • CREATIVE TABLET",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹29,990",
        "mrp": "₹39,999",
        "discount": "25% OFF",
        "rating": "4.6 ★ (3,100+ Reviews)",
        "badge": "3D SCULPTING PAD",
        "accent": (168, 85, 247),
        "specs": ["15.6-inch 1080p IPS Display with 120% sRGB Color Gamut", "PW517 Battery-Free Stylus with ±60° Tilt Recognition", "Full-Laminated Screen Minimizes Parallax for Precise Drawing"],
        "url": "https://www.amazon.in/dp/B08SQ8F67C?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "2.80% Commission (₹839 Payout)"
    },
    {
        "slug": "rife-dual-monitor-arm-gas-spring",
        "title": "Rife Heavy Duty Dual Monitor Arm Mount",
        "subtitle": "Gas Spring 360° Full Articulation • Fits 17' to 32' Screens • Cable Tidy",
        "brand": "RIFE • MOUNTING RIGS",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹3,999",
        "mrp": "₹7,999",
        "discount": "50% OFF",
        "rating": "4.5 ★ (3,600+ Reviews)",
        "badge": "50% OFF DEAL",
        "accent": (14, 165, 233),
        "specs": ["Counterbalance Gas Spring holds up to 9kg per arm effortlessly", "Supports VESA 75x75mm and 100x100mm mounting patterns", "Includes both Heavy Duty C-Clamp & Grommet desk mounts"],
        "url": "https://www.amazon.in/dp/B08B9P2J6K?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission"
    },
    {
        "slug": "portronics-clamp-x-laptop-stand",
        "title": "Portronics Clamp X Multi-Angle Stand",
        "subtitle": "Aircraft Grade Aluminum • Ventilated Heat Dissipation • Foldable",
        "brand": "PORTRONICS • ACCESSORIES",
        "category": "workspace",
        "category_name": "Workspace & Ergonomics",
        "price": "₹899",
        "mrp": "₹1,999",
        "discount": "55% OFF",
        "rating": "4.4 ★ (12,500+ Reviews)",
        "badge": "BUDGET FAVORITE",
        "accent": (168, 85, 247),
        "specs": ["Supports All Laptops from 11-inch to 17-inch MacBooks and PCs", "4 Adjustable Ergonomic Angles to prevent neck strain", "Anti-Skid Silicone pads protect your desk and device from scratches"],
        "url": "https://www.amazon.in/dp/B08DFGZJ7R?tag=aitoolkitpro-21",
        "type": "amazon",
        "comm_est": "4.25% Commission"
    },

    # =========================================================================
    # 🚀 HIGH-YIELD SAAS & CLOUD (7 Platforms)
    # =========================================================================
    {
        "slug": "hostinger-cloud-web-hosting",
        "title": "Hostinger Cloud & Web VPS Hosting",
        "subtitle": "Host AI Apps, Portfolios & Fast Websites • Free Domain + SSL Included",
        "brand": "HOSTINGER • WEB CLOUD",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "₹149 / mo",
        "mrp": "₹599 / mo",
        "discount": "75% OFF + FREE DOMAIN",
        "rating": "4.8 ★ (Over 3M Websites)",
        "badge": "60% COMM: UP TO ₹7,500",
        "accent": (103, 58, 183), # Hostinger Purple
        "specs": ["Deploy up to 100 Websites with 99.9% Uptime Guarantee", "Ultra-Fast NVMe Storage & LiteSpeed Web Server Engine", "Free 1-Click WordPress, Node.js & Docker Container Installs"],
        "url": "https://www.hostinger.in/referral?REF=AITOOLKITPRO",
        "type": "saas",
        "comm_est": "Flat 60% Commission per Sale"
    },
    {
        "slug": "elevenlabs-ai-voice-studio",
        "title": "ElevenLabs Hyper-Realistic AI Voices",
        "subtitle": "Generate Professional YouTube Voiceovers in 1-Click • 29+ Languages",
        "brand": "ELEVENLABS • AI AUDIO",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "$5.00 / mo",
        "mrp": "$22.00 / mo",
        "discount": "FREE TIER AVAILABLE",
        "rating": "4.9 ★ (Used by Top Creators)",
        "badge": "22% RECURRING / MO",
        "accent": (14, 165, 233),
        "specs": ["1000+ Lifelike Human Voices across 29 Languages", "Voice Cloning from 1-Minute Audio Sample", "Instant MP3 Export for Video Editors"],
        "url": "https://elevenlabs.io/affiliates",
        "type": "saas",
        "comm_est": "22% Monthly Recurring Commission"
    },
    {
        "slug": "make-automation-ai-workflows",
        "title": "Make.com (Integromat) - Visual AI Automation",
        "subtitle": "Connect 1,500+ Apps • No-Code Webhook Pipelines • OpenAI & Claude Nodes",
        "brand": "MAKE • ENTERPRISE AUTOMATION",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "₹749 / mo",
        "mrp": "₹1,499 / mo",
        "discount": "50% ANNUAL DEAL",
        "rating": "4.9 ★ (14,000+ Reviews)",
        "badge": "40% RECURRING LIFETIME",
        "accent": (16, 185, 129),
        "specs": ["Visual Drag-and-Drop Canvas for Complex Multi-Step Automation", "Direct API Connectors for ChatGPT, Claude, Vercel, YouTube & Slack", "Generous Free Tier: 1,000 Operations Every Month"],
        "url": "https://www.make.com/en/register?aff=aitoolkitpro",
        "type": "saas",
        "comm_est": "40% Recurring Monthly ($10 - $120/mo)"
    },
    {
        "slug": "descript-ai-video-podcast-editor",
        "title": "Descript AI - Text-Based Video & Audio Editor",
        "subtitle": "Edit Video by Editing Text • Studio Sound Voice Enhancer • AI Eye Contact",
        "brand": "DESCRIPT • NEXT-GEN VIDEO",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "₹999 / mo",
        "mrp": "₹1,899 / mo",
        "discount": "47% OFF PRO DEAL",
        "rating": "4.8 ★ (8,700+ Reviews)",
        "badge": "30% RECURRING COMM",
        "accent": (16, 185, 129),
        "specs": ["Automatic Instant Audio Transcription with 95%+ Accuracy", "1-Click 'Studio Sound' AI Replaces Noisy Rooms with Studio Audio", "AI Eye Contact Corrects Gaze Directly into Camera Lens"],
        "url": "https://www.descript.com/?lmref=aitoolkitpro",
        "type": "saas",
        "comm_est": "30% Recurring Share ($8 - $60/mo)"
    },
    {
        "slug": "fiverr-creative-freelance-network",
        "title": "Fiverr Freelance & Creative Network",
        "subtitle": "Hire 3D Animators, Video Editors & Web Devs • $15 - $150 CPA",
        "brand": "FIVERR • CREATIVE SERVICES",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "From $5.00",
        "mrp": "Custom Quotes",
        "discount": "INSTANT HIRES",
        "rating": "4.8 ★ (Global Marketplace)",
        "badge": "$15 - $150 CPA",
        "accent": (34, 197, 94), # Fiverr Green
        "specs": ["Vetted Pro Freelancers with Portfolio Reviews", "Safe Escrow Payment Protection", "1-Day Turnaround on Shorts & Thumbnails"],
        "url": "https://affiliates.fiverr.com/",
        "type": "saas",
        "comm_est": "$15 - $150 CPA per First Order"
    },
    {
        "slug": "envato-elements-creative-assets",
        "title": "Envato Elements Unlimited Creative Pass",
        "subtitle": "Unlimited Stock Footage, Sound Effects, Premiere & After Effects Templates",
        "brand": "ENVATO • CREATOR ASSETS",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "$16.50 / mo",
        "mrp": "$33.00 / mo",
        "discount": "UNLIMITED DOWNLOADS",
        "rating": "4.8 ★ (10M+ Assets)",
        "badge": "$20 - $120 CPA",
        "accent": (130, 179, 63), # Envato Green
        "specs": ["Commercial License on Millions of Audio & Video Files", "Sound Effects Specifically Engineered for Shorts & TikTok", "Over 50,000 Premiere Pro Motion Templates"],
        "url": "https://elements.envato.com/affiliate-program",
        "type": "saas",
        "comm_est": "$20 - $120 CPA Payout"
    },
    {
        "slug": "invideo-ai-video-generator",
        "title": "InVideo AI Script-to-Video Engine",
        "subtitle": "Generate Full YouTube Shorts with Voice, Footage & Captions in 30 Seconds",
        "brand": "INVIDEO AI • AUTO VIDEO",
        "category": "saas",
        "category_name": "High-Yield SaaS",
        "price": "$20.00 / mo",
        "mrp": "$30.00 / mo",
        "discount": "FREE TRIAL INCLUDED",
        "rating": "4.7 ★ (Over 7M Creators)",
        "badge": "30% RECURRING / MO",
        "accent": (236, 72, 153),
        "specs": ["Text Prompt to Complete Polished Vertical Short", "Auto-Generated Dynamic Animated Subtitles", "iStock Access with Zero Watermarks"],
        "url": "https://invideo.io/affiliates/",
        "type": "saas",
        "comm_est": "30% Monthly Lifetime Commission"
    },
    # =========================================================================
    # 🚀 EXPANDED FLAGSHIP CREATOR GEAR (16 Additional Rigs - 70 Total)
    # =========================================================================
    {'slug': 'rode-nt1-5th-gen-condenser-mic', 'title': 'Røde NT1 5th Gen Studio Condenser Mic', 'subtitle': '32-Bit Float On-Board Recording • XLR & USB-C Dual Output • Revolution Preamp', 'brand': 'RØDE • BROADCAST STUDIO', 'category': 'audio', 'category_name': 'Studio & Audio', 'price': '₹23,990', 'mrp': '₹28,500', 'discount': '16% OFF', 'rating': '4.8 ★ (3,400+ Reviews)', 'badge': '32-BIT FLOAT', 'accent': (12, 150, 156), 'specs': ['Ultra-Low Noise (4dBA) Capsule', '32-Bit Float USB Recording Zero Clipping', 'Internal DSP with APHEX Audio Effects'], 'url': 'https://www.amazon.in/dp/B0BSV45N62?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'yamaha-hs5-powered-studio-monitors', 'title': 'Yamaha HS5 Powered Studio Monitors (Pair)', 'subtitle': '5-Inch Cone Woofer • 1-Inch Dome Tweeter • Bi-Amp 70W Nearfield Monitors', 'brand': 'YAMAHA • AUDIO REFERENCE', 'category': 'audio', 'category_name': 'Studio & Audio', 'price': '₹31,990', 'mrp': '₹38,000', 'discount': '16% OFF', 'rating': '4.7 ★ (4,800+ Reviews)', 'badge': 'STUDIO STANDARD', 'accent': (12, 150, 156), 'specs': ['54Hz - 30kHz Flat Frequency Response', 'Room Control and High TRIM Filters', 'Bi-Amplified 70W High-Performance Output'], 'url': 'https://www.amazon.in/dp/B00CFOX420?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'lewitt-lct-440-pure-condenser-mic', 'title': 'Lewitt LCT 440 PURE Large Diaphragm Mic', 'subtitle': '1-Inch True Condenser Capsule • Gold Sputtered Mylar • Zero Distortion', 'brand': 'LEWITT • VIENNA AUDIO', 'category': 'audio', 'category_name': 'Studio & Audio', 'price': '₹24,490', 'mrp': '₹29,990', 'discount': '18% OFF', 'rating': '4.9 ★ (1,150+ Reviews)', 'badge': 'PURE CLARITY', 'accent': (12, 150, 156), 'specs': ['Gold-Sputtered 3-Micron Mylar Capsule', 'Outstanding High-End Vocal Presence', 'Magnetic Pop Filter & Shock Mount Included'], 'url': 'https://www.amazon.in/dp/B06XQ2G8W2?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'rodecaster-pro-ii-audio-studio', 'title': 'Rodecaster Pro II Audio Production Studio', 'subtitle': 'Quad Revolution Preamps • Dual USB-C Audio • APHEX DSP Processing', 'brand': 'RØDE • ALL-IN-ONE MIXER', 'category': 'audio', 'category_name': 'Studio & Audio', 'price': '₹64,990', 'mrp': '₹74,990', 'discount': '13% OFF', 'rating': '4.8 ★ (2,400+ Reviews)', 'badge': 'FLAGSHIP CONSOLE', 'accent': (12, 150, 156), 'specs': ['4 High-Gain Combo XLR/TRS Revolution Preamps', '8 Fully Programmable SMART Trigger Pads', 'Dual USB-C Audio Interfaces for 2 PCs'], 'url': 'https://www.amazon.in/dp/B0B17V9V6M?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'elgato-stream-deck-plus', 'title': 'Elgato Stream Deck + (Console & Touch Strip)', 'subtitle': '8 LCD Keys • 4 Rotary Encoders • Dynamic Touch Strip • Wave Link Hub', 'brand': 'ELGATO • WORKFLOW AUTOMATION', 'category': 'audio', 'category_name': 'Studio & Audio', 'price': '₹19,990', 'mrp': '₹23,990', 'discount': '17% OFF', 'rating': '4.8 ★ (5,200+ Reviews)', 'badge': 'CREATOR CONSOLE', 'accent': (12, 150, 156), 'specs': ['4 Tactile Push Encoders for Audio & Dials', 'Dynamic Touch Strip Display with Swipe Navigation', 'Deep OBS Studio & Premiere Pro Integrations'], 'url': 'https://www.amazon.in/dp/B0BHTR7M4Z?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'sony-fx30-cinema-line-camera', 'title': 'Sony FX30 Cinema Line Super 35 Camera', 'subtitle': 'Dual Base ISO 800/2500 • 4K 120p 10-bit 4:2:2 • S-Cinetone Color Science', 'brand': 'SONY CINEMA LINE • PROFESSIONAL VIDEO', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹1,79,990', 'mrp': '₹1,99,990', 'discount': '10% OFF', 'rating': '4.8 ★ (1,450+ Reviews)', 'badge': 'CINEMA PRO', 'accent': (12, 150, 156), 'specs': ['Super 35 Back-Illuminated 6K Sensor', '4K 120p 10-bit 4:2:2 All-Intra Recording', 'Active Cooling Fan for Unlimited 4K Capture'], 'url': 'https://www.amazon.in/dp/B0BGJBMK6W?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'sigma-24-70mm-f2-8-dg-dn-art-lens', 'title': 'Sigma 24-70mm f/2.8 DG DN Art Lens (Sony E)', 'subtitle': 'Constant f/2.8 Aperture • 11-Blade Circular Diaphragm • Nano Porous Coating', 'brand': 'SIGMA • ART SERIES OPTICS', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹98,900', 'mrp': '₹1,24,900', 'discount': '21% OFF', 'rating': '4.9 ★ (2,100+ Reviews)', 'badge': 'FLAGSHIP GLASS', 'accent': (12, 150, 156), 'specs': ['Constant f/2.8 Maximum Aperture Throughout Zoom', 'Hyper Sonic Stepping Motor for Fast Silent AF', 'Dust & Splash-Proof Brass Bayonet Mount'], 'url': 'https://www.amazon.in/dp/B0829RP85S?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'elgato-4k-x-capture-card', 'title': 'Elgato 4K X External USB-C Capture Card', 'subtitle': '4K144 Pass-Through & Capture • 1080p240 Refresh • VRR & HDR10 Support', 'brand': 'ELGATO • BROADCAST CAPTURE', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹21,990', 'mrp': '₹26,990', 'discount': '19% OFF', 'rating': '4.7 ★ (1,850+ Reviews)', 'badge': '4K 144FPS', 'accent': (12, 150, 156), 'specs': ['HDMI 2.1 Ultra-Low Latency Pass-Through', 'Up to 4K144 / 1080p240 High Frame Rate Capture', 'Driverless Plug & Play on Mac, Windows, iPad'], 'url': 'https://www.amazon.in/dp/B0CP2CS95L?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'aputure-amaran-100d-s-led-light', 'title': 'Aputure Amaran 100d S Daylight LED Light', 'subtitle': '100W Ultra-High Color Quality • 5600K Daylight • CRI 95+ TLCI 97+ • Bowens Mount', 'brand': 'APUTURE • AMARAN CINEMA', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹18,490', 'mrp': '₹22,990', 'discount': '20% OFF', 'rating': '4.8 ★ (3,600+ Reviews)', 'badge': 'PRO STUDIO LIGHT', 'accent': (12, 150, 156), 'specs': ['Ultra-High SSI Color Accuracy CRI 95+ TLCI 97+', 'Universal Bowens Mount for Studio Softboxes', 'Sidus Link Smartphone App Wireless Bluetooth Control'], 'url': 'https://www.amazon.in/dp/B0BXFSW9J9?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'aputure-light-dome-se-softbox', 'title': 'Aputure Light Dome SE 33.5" Softbox Diffuser', 'subtitle': '16-Sided Hexadecagon Softbox • 1.5 & 2.5 Stop Diffusion • 45° Fabric Grid', 'brand': 'APUTURE • STUDIO MODIFIER', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹8,990', 'mrp': '₹11,500', 'discount': '22% OFF', 'rating': '4.7 ★ (2,900+ Reviews)', 'badge': 'CINEMA SOFT LIGHT', 'accent': (12, 150, 156), 'specs': ['Deep Parabolic 16-Sided Hexadecagon Shape', 'Dual Front Diffusion Fabrics & 45° Honeycomb Grid', 'Lightweight Fiberglass Rods for Fast Studio Setup'], 'url': 'https://www.amazon.in/dp/B08YRPQDF7?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'dji-rs-3-mini-camera-gimbal', 'title': 'DJI RS 3 Mini 3-Axis Camera Gimbal', 'subtitle': 'Ultra-Lightweight 795g Body • 2kg Tested Payload • Native Vertical Video', 'brand': 'DJI • PROFESSIONAL STABILIZER', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹25,990', 'mrp': '₹32,990', 'discount': '21% OFF', 'rating': '4.7 ★ (4,100+ Reviews)', 'badge': 'NATIVE VERTICAL', 'accent': (12, 150, 156), 'specs': ['795g Ultra-Compact Lightweight Design', 'Native Vertical Shooting for YouTube Shorts & Reels', 'Bluetooth Wireless Shutter Control Integration'], 'url': 'https://www.amazon.in/dp/B0BSH7Y1XQ?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'zhiyun-crane-m3s-gimbal-stabilizer', 'title': 'Zhiyun Crane M3S Gimbal Stabilizer', 'subtitle': 'Built-in Lumen Amplifier Fill Light • Quick Release 4.0 • Bluetooth Shutter', 'brand': 'ZHIYUN • CREATOR GIMBAL', 'category': 'video', 'category_name': 'Cameras & Optics', 'price': '₹26,490', 'mrp': '₹34,000', 'discount': '22% OFF', 'rating': '4.6 ★ (1,300+ Reviews)', 'badge': 'PORTABLE VLOGGING', 'accent': (12, 150, 156), 'specs': ['Built-in 1000 Lux Bi-Color Video Fill Light', 'Quick Release Plate without Rebalancing Between Battery Swaps', 'PD Fast Charging 100% in 2 Hours'], 'url': 'https://www.amazon.in/dp/B0C6DB7Q5X?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'asus-proart-pa278cv-designer-monitor', 'title': 'ASUS ProArt Display PA278CV 27-Inch 1440p', 'subtitle': '2560 x 1440 IPS • 100% sRGB / Rec.709 • Calman Verified Delta E < 2 • 65W USB-C', 'brand': 'ASUS PROART • COLOR ACCURACY', 'category': 'hardware', 'category_name': 'Rig Hardware', 'price': '₹28,990', 'mrp': '₹37,000', 'discount': '22% OFF', 'rating': '4.7 ★ (3,100+ Reviews)', 'badge': 'CALMAN VERIFIED', 'accent': (12, 150, 156), 'specs': ['100% sRGB & 100% Rec. 709 Wide Color Gamut', 'Calman Verified Factory Pre-Calibrated Delta E < 2', '65W USB-C Single Cable Video, Data & Fast Charging'], 'url': 'https://www.amazon.in/dp/B08LCP296A?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'benq-pd2705u-4k-designer-monitor', 'title': 'BenQ PD2705U 27-Inch 4K UHD Designer Monitor', 'subtitle': '3840 x 2160 UHD • AQCOLOR Technology • 99% sRGB / Rec.709 • KVM Switch', 'brand': 'BENQ • PROFESSIONAL DISPLAY', 'category': 'hardware', 'category_name': 'Rig Hardware', 'price': '₹44,990', 'mrp': '₹56,000', 'discount': '20% OFF', 'rating': '4.7 ★ (1,700+ Reviews)', 'badge': '4K UHD AQCOLOR', 'accent': (12, 150, 156), 'specs': ['4K UHD (3840x2160) IPS Anti-Glare Panel', 'Integrated KVM Switch for Instant Dual PC Control', 'Hotkey Puck G2 Controller for Instant Color Profile Switching'], 'url': 'https://www.amazon.in/dp/B09Q8562B1?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'logitech-mx-mechanical-wireless-keyboard', 'title': 'Logitech MX Mechanical Wireless Tactile Keyboard', 'subtitle': 'Low-Profile Tactile Quiet Mechanical Switches • Smart Backlighting • Multi-OS', 'brand': 'LOGITECH • MASTER SERIES', 'category': 'hardware', 'category_name': 'Rig Hardware', 'price': '₹14,990', 'mrp': '₹18,995', 'discount': '21% OFF', 'rating': '4.8 ★ (4,900+ Reviews)', 'badge': 'MASTER SERIES', 'accent': (12, 150, 156), 'specs': ['Low-Profile Quiet Tactile Mechanical Switches', 'Smart Backlighting with Hand Proximity Sensors', 'Multi-OS Dual Bluetooth and Logi Bolt Wireless Support'], 'url': 'https://www.amazon.in/dp/B09LK2R8D2?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
    {'slug': 'sihoo-doro-c300-ergonomic-creator-chair', 'title': 'Sihoo Doro C300 Ergonomic Creator Chair', 'subtitle': 'Dynamic Self-Adaptive Lumbar Support • 6D Coordinated Armrests • Cloud Mesh', 'brand': 'SIHOO • ERGONOMIC SEATING', 'category': 'workspace', 'category_name': 'Ergonomics & Desk', 'price': '₹28,990', 'mrp': '₹42,000', 'discount': '31% OFF', 'rating': '4.7 ★ (5,800+ Reviews)', 'badge': 'ALL-DAY COMFORT', 'accent': (12, 150, 156), 'specs': ['Dynamic Self-Adaptive Lumbar Support Follows Posture', '6D Synchronized Mechanical Armrests', 'Pressure-Relieving Cloud Mesh with Waterfall Seat Edge'], 'url': 'https://www.amazon.in/dp/B0BYRMDV55?tag=aitoolkitpro-21', 'type': 'amazon', 'comm_est': '3.5% Commission'},
]

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_gear_card(p):
    W, H = 1200, 675
    img = Image.new("RGBA", (W, H), (3, 23, 22, 255)) # Dark teal
    draw = ImageDraw.Draw(img)

    # 1. Background radial gradients & subtle grid
    accent_col = p["accent"]
    # Top-right glow
    for r in range(400, 0, -25):
        alpha = int(45 * (1 - r / 400))
        draw.ellipse([(950 - r, 120 - r), (950 + r, 120 + r)], fill=(*accent_col, alpha))
    # Bottom-left glow
    for r in range(350, 0, -25):
        alpha = int(35 * (1 - r / 350))
        draw.ellipse([(150 - r, 550 - r), (150 + r, 550 + r)], fill=(12, 150, 156, alpha))

    # Grid lines
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=(7, 56, 58, 40), width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=(7, 56, 58, 40), width=1)

    # Card background container
    draw_rounded_rect(draw, [40, 40, W - 40, H - 40], radius=24, fill=(4, 36, 38, 235), outline=(12, 150, 156, 120), width=2)

    # Top Brand Bar
    # Category badge
    draw_rounded_rect(draw, [70, 70, 380, 115], radius=12, fill=(27, 56, 71, 240), outline=(*accent_col, 180), width=1)
    draw.text((86, 82), p["brand"], font=font_badge, fill=accent_col)

    # High-Yield / Commission badge (Top Right)
    badge_txt = p["badge"]
    draw_rounded_rect(draw, [W - 390, 70, W - 70, 115], radius=12, fill=(*accent_col, 45), outline=(*accent_col, 220), width=1)
    draw.text((W - 370, 82), f"⚡ {badge_txt}", font=font_badge, fill=(255, 255, 255))

    # Title & Subtitle
    draw.text((70, 145), p["title"], font=font_hero, fill=(255, 255, 255))
    draw.text((70, 200), p["subtitle"], font=font_regular, fill=(107, 163, 190))

    # Divider
    draw.line([(70, 245), (W - 70, 245)], fill=(12, 150, 156, 80), width=1)

    # Left Column: Specs List
    sy = 275
    draw.text((70, sy), "VERIFIED CREATOR SPECIFICATIONS:", font=font_bold, fill=(255, 255, 255))
    sy += 38
    for spec in p["specs"]:
        # Bullet circle
        draw.ellipse([(72, sy + 4), (84, sy + 16)], fill=accent_col)
        draw.text((98, sy), spec, font=font_regular, fill=(220, 240, 245))
        sy += 36

    # Rating & Platform Tag
    sy += 15
    draw_rounded_rect(draw, [70, sy, 380, sy + 44], radius=10, fill=(3, 23, 22, 240), outline=(12, 150, 156, 100), width=1)
    draw.text((86, sy + 11), f"⭐ {p['rating']}", font=font_bold, fill=(245, 158, 11))

    # Right Column: Price Box & CTA Simulation
    px1, py1, px2, py2 = W - 480, 275, W - 70, 580
    draw_rounded_rect(draw, [px1, py1, px2, py2], radius=20, fill=(3, 23, 22, 250), outline=(*accent_col, 160), width=2)

    # Price section
    draw.text((px1 + 30, py1 + 25), "LIVE VERIFIED DEAL:", font=font_small, fill=(107, 163, 190))
    draw.text((px1 + 30, py1 + 55), p["price"], font=font_price, fill=(255, 255, 255))
    
    # MRP & Discount
    draw.text((px1 + 230, py1 + 65), f"MRP {p['mrp']}", font=font_mrp, fill=(107, 163, 190))
    draw_rounded_rect(draw, [px1 + 30, py1 + 120, px1 + 210, py1 + 160], radius=8, fill=(34, 197, 94, 40), outline=(34, 197, 94, 180), width=1)
    draw.text((px1 + 45, py1 + 130), f"🔥 {p['discount']}", font=font_bold, fill=(34, 197, 94))

    # Commission tag
    draw.text((px1 + 30, py1 + 185), f"💰 {p['comm_est']}", font=font_bold, fill=accent_col)

    # Action CTA Simulation Bar
    btn_fill = (255, 153, 0) if p["type"] == "amazon" else (12, 150, 156)
    btn_txt_col = (0, 0, 0) if p["type"] == "amazon" else (255, 255, 255)
    btn_label = "BUY ON AMAZON INDIA ↗" if p["type"] == "amazon" else "CLAIM CREATOR DEAL ↗"
    draw_rounded_rect(draw, [px1 + 30, py2 - 80, px2 - 30, py2 - 25], radius=12, fill=btn_fill, outline=None)
    draw.text((px1 + 55, py2 - 62), btn_label, font=font_bold, fill=btn_txt_col)

    # Bottom watermark footer
    draw.text((70, H - 75), "AI TOOLKIT PRO • OFFICIAL CREATOR STORE • AMAZON ID: aitoolkitpro-21", font=font_mono, fill=(107, 163, 190, 180))

    out_path = os.path.join(OUTPUT_DIR, f"{p['slug']}.png")
    img.save(out_path, "PNG", optimize=True)
    return out_path

def main():
    total = len(GEAR_PRODUCTS)
    print(f"Generating {total} high-resolution gear preview assets in {OUTPUT_DIR}...")
    for i, p in enumerate(GEAR_PRODUCTS, 1):
        path = render_gear_card(p)
        print(f"[{i:02d}/{total}] Created {os.path.basename(path)}")
    print(f"All {total} product preview assets created successfully!")

if __name__ == "__main__":
    main()
