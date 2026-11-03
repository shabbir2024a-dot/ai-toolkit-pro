import os
import re
import urllib.request

OUTPUT_DIR = "/Users/bishal/ai_toolkit_pro_web/assets/products"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
}

ITEMS = [
    {"slug":"dji-osmo-pocket-3-creator-combo","asin":"B0FKT9K6CB","imgUrl":"https://m.media-amazon.com/images/I/41lh40NDDzL._AC_SL800_.jpg"},
    {"slug":"shure-mv7-plus-podcast-microphone","asin":"B0CTJ7PVN1","imgUrl":"https://m.media-amazon.com/images/I/81SkpwyPZnL._AC_SL800_.jpg"},
    {"slug":"rode-podmic-dynamic-podcasting-mic","asin":"B0CKPTX13H","imgUrl":"https://m.media-amazon.com/images/I/71cMV62ll5L._AC_SL800_.jpg"},
    {"slug":"elgato-wave-3-premium-usb-mic","asin":"B08SD8P1V2","imgUrl":"https://m.media-amazon.com/images/I/512OU96THWL._AC_SL800_.jpg"},
    {"slug":"logitech-mx-master-3s-wireless-mouse","asin":"B0FPM2VC6Q","imgUrl":"https://m.media-amazon.com/images/I/61z3ENJubZL._AC_SL800_.jpg"},
    {"slug":"focusrite-scarlett-2i2-studio-bundle","asin":"B07QR6Z1JB","imgUrl":"https://m.media-amazon.com/images/I/613veRuWtmL._AC_SL800_.jpg"},
    {"slug":"fifine-k688-usb-xlr-podcast-mic","asin":"B0D458QDVN","imgUrl":"https://m.media-amazon.com/images/I/71P1QQK4qYL._AC_SL800_.jpg"},
    {"slug":"rode-psa1-plus-professional-boom-arm","asin":"B09JBVR5B4","imgUrl":"https://m.media-amazon.com/images/I/41O6NJyDr2L._AC_SL800_.jpg"},
    {"slug":"sony-alpha-zve10-with-zoom-lens","asin":"B0DJSLJYCF","imgUrl":"https://m.media-amazon.com/images/I/81ST9EJe9QL._AC_SL800_.jpg"},
    {"slug":"godox-sl60w-continuous-led-video-light","asin":"B0FWRVVZJL","imgUrl":"https://m.media-amazon.com/images/I/61AegR3-mCL._AC_SL800_.jpg"},
    {"slug":"neewer-660-led-video-light-2pack-kit","asin":"B0DNFW6NSP","imgUrl":"https://m.media-amazon.com/images/I/71dJRRsEVTL._AC_SL800_.jpg"},
    {"slug":"elgato-cam-link-4k-usb-capture","asin":"B07K3FN5MR","imgUrl":"https://m.media-amazon.com/images/I/5146dDMeV6L._AC_SL800_.jpg"},
    {"slug":"ulanzi-vl49-rgb-pocket-led-light","asin":"B08MDQ3CJY","imgUrl":"https://m.media-amazon.com/images/I/71vp1ZCn5WL._AC_SL800_.jpg"},
    {"slug":"zotac-rtx-4060-twin-edge-gpu","asin":"B0FH6JPVZB","imgUrl":"https://m.media-amazon.com/images/I/71topOx+V9L._AC_SL800_.jpg"},
    {"slug":"corsair-vengeance-ddr5-32gb-ram","asin":"B0GGJ79NR3","imgUrl":"https://m.media-amazon.com/images/I/71xOTU97xEL._AC_SL800_.jpg"},
    {"slug":"samsung-odyssey-g7-32-inch-curved-gaming-monitor","asin":"B0FDL66T4D","imgUrl":"https://m.media-amazon.com/images/I/613ZGQ-kWoL._AC_SL800_.jpg"},
    {"slug":"lg-ultragear-27-inch-qhd-nano-ips-monitor","asin":"B0H451STZ4","imgUrl":"https://m.media-amazon.com/images/I/61ZRtNoPtWL._AC_SL800_.jpg"},
    {"slug":"keychron-k2-wireless-mechanical-keyboard","asin":"B0DXZ97PCG","imgUrl":"https://m.media-amazon.com/images/I/71WrD1r8KhL._AC_SL800_.jpg"},
    {"slug":"asus-rog-strix-850w-gold-psu","asin":"B0F5WSDWZQ","imgUrl":"https://m.media-amazon.com/images/I/81JTqeZxQDL._AC_SL800_.jpg"},
    {"slug":"ant-esports-ice-511mt-mesh-cabinet","asin":"B0CRNQJBWB","imgUrl":"https://m.media-amazon.com/images/I/71vjp8FqE1L._AC_SL800_.jpg"},
    {"slug":"green-soul-monster-ultimate-creator-chair","asin":"B085NPF8BK","imgUrl":"https://m.media-amazon.com/images/I/61HyPFzZG7L._AC_SL800_.jpg"},
    {"slug":"featherlite-liberate-high-back-chair","asin":"B08T7HGNMB","imgUrl":"https://m.media-amazon.com/images/I/71W+kposG2L._AC_SL800_.jpg"},
    {"slug":"jin-office-motorized-electric-standing-desk","asin":"B0FGJXBHS1","imgUrl":"https://m.media-amazon.com/images/I/81qpBFy-vGL._AC_SL800_.jpg"},
    {"slug":"benq-screenbar-halo-wireless-monitor-light","asin":"B0DK59YKRS","imgUrl":"https://m.media-amazon.com/images/I/41fmQI53UNL._AC_SL800_.jpg"},
    {"slug":"elgato-prompter-studio-teleprompter","asin":"B0CH3P9K1X","imgUrl":"https://m.media-amazon.com/images/I/711FhPjsfqL._AC_SL800_.jpg"},
    {"slug":"huion-kamvas-16-graphics-drawing-tablet","asin":"B0FBKF1899","imgUrl":"https://m.media-amazon.com/images/I/61ysj7farmL._AC_SL800_.jpg"},
    {"slug":"rife-dual-monitor-arm-gas-spring","asin":"B0CKW835X3","imgUrl":"https://m.media-amazon.com/images/I/41dpDQjPW+L._AC_SL800_.jpg"},
    {"slug":"portronics-clamp-x-laptop-stand","asin":"B0C9J63G2F","imgUrl":"https://m.media-amazon.com/images/I/61AS07l2cBL._AC_SL800_.jpg"}
]

def main():
    print(f"Downloading {len(ITEMS)} high-res Amazon product photos...")
    for item in ITEMS:
        out_file = os.path.join(OUTPUT_DIR, f"{item['slug']}.jpg")
        img_url = item['imgUrl']
        try:
            req = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                with open(out_file, 'wb') as f:
                    f.write(resp.read())
            print(f"  ✓ Saved {os.path.basename(out_file)} ({os.path.getsize(out_file)} bytes)")
        except Exception as e:
            # Fallback to direct raw url without SL800
            raw_url = re.sub(r'\._AC_[^\.]+\.', '.', img_url)
            try:
                req = urllib.request.Request(raw_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=10) as resp:
                    with open(out_file, 'wb') as f:
                        f.write(resp.read())
                print(f"  ✓ Saved {os.path.basename(out_file)} via raw URL ({os.path.getsize(out_file)} bytes)")
            except Exception as e2:
                print(f"  ✗ Failed for {item['slug']}: {e2}")

if __name__ == "__main__":
    main()
