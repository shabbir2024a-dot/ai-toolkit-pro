import os
from PIL import Image

src = "/Users/bishal/ai_toolkit_pro_web/assets/pinterest_creator_gear_pin.jpg"
dst = "/Users/bishal/ai_toolkit_pro_web/assets/pinterest_creator_gear_cover_1080x1920.jpg"

im = Image.open(src)
# Create 1080x1920 canvas with the dark teal background
canvas = Image.new("RGB", (1080, 1920), (3, 23, 22))

# Resize im to fit width 1080 (1080, 1620)
im_resized = im.resize((1080, int(im.height * 1080 / im.width)), Image.Resampling.LANCZOS)

# Paste centered vertically
y_off = (1920 - im_resized.height) // 2
canvas.paste(im_resized, (0, y_off))

canvas.save(dst, "JPEG", quality=95)
print(f"Cover image saved with exact dimensions 1080x1920: {dst}")
