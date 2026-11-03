import os
import re
import time
import urllib.request
import urllib.parse
from generate_gear_assets import GEAR_PRODUCTS

OUTPUT_DIR = "/Users/bishal/ai_toolkit_pro_web/assets/products"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

def clean_amazon_img_url(raw_url):
    # Remove sizing tokens like ._SX679_. or ._SL1500_. so we can get high-res ._SL800_.
    # e.g. https://m.media-amazon.com/images/I/71LYHO3+wnL._SL1356_.jpg -> base + ._SL800_.jpg
    m = re.match(r'(https://m\.media-amazon\.com/images/I/[A-Za-z0-9\+\%_-]+)(?:\.[^.]+)?\.(jpg|png)', raw_url)
    if m:
        return f"{m.group(1)}._AC_SL800_.{m.group(2)}"
    return raw_url

def fetch_image_for_asin(asin, title):
    url = f"https://www.amazon.in/dp/{asin}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            if resp.status == 200:
                html = resp.read().decode('utf-8', errors='ignore')
                # 1. hiRes or data-old-hires
                m = re.search(r'data-old-hires=\"(https://m\.media-amazon\.com/images/I/[^\"]+)\"', html)
                if m: return clean_amazon_img_url(m.group(1)), asin
                
                m = re.search(r'\"hiRes\":\"(https://m\.media-amazon\.com/images/I/[^\"]+)\"', html)
                if m: return clean_amazon_img_url(m.group(1)), asin

                m = re.search(r'\"large\":\"(https://m\.media-amazon\.com/images/I/[^\"]+)\"', html)
                if m: return clean_amazon_img_url(m.group(1)), asin

                m = re.search(r'id=\"landingImage\"[^>]+src=\"(https://m\.media-amazon\.com/images/I/[^\"]+)\"', html)
                if m: return clean_amazon_img_url(m.group(1)), asin
    except Exception as e:
        print(f"  [Direct ASIN {asin} error]: {e}")

    # Fallback: Search Amazon.in for the product title
    search_query = urllib.parse.quote(title[:45])
    search_url = f"https://www.amazon.in/s?k={search_query}"
    s_req = urllib.request.Request(search_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(s_req, timeout=8) as resp:
            s_html = resp.read().decode('utf-8', errors='ignore')
            # Extract first search result image and ASIN
            s_asin_m = re.search(r'data-asin=\"(B[0-9A-Z]{9})\"', s_html)
            s_img_m = re.search(r'src=\"(https://m\.media-amazon\.com/images/I/[A-Za-z0-9\+\%_-]+[^\"]*\.jpg)\"[^>]*class=\"s-image\"', s_html)
            if s_img_m:
                found_asin = s_asin_m.group(1) if s_asin_m else asin
                return clean_amazon_img_url(s_img_m.group(1)), found_asin
    except Exception as e:
        print(f"  [Search fallback error]: {e}")

    return None, asin

def download_image(img_url, out_path):
    req = urllib.request.Request(img_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as resp:
        with open(out_path, 'wb') as f:
            f.write(resp.read())

def main():
    print(f"Processing {len(GEAR_PRODUCTS)} products for real image assets...")
    results = {}
    
    for idx, p in enumerate(GEAR_PRODUCTS, 1):
        slug = p['slug']
        out_file = os.path.join(OUTPUT_DIR, f"{slug}.jpg")
        
        if p['type'] == 'amazon':
            asin_match = re.search(r'/dp/([A-Z0-9]{10})', p['url'])
            asin = asin_match.group(1) if asin_match else ""
            print(f"[{idx:02d}/54] Fetching {p['title'][:35]} (ASIN: {asin})...")
            
            img_url, new_asin = fetch_image_for_asin(asin, p['title'])
            if img_url:
                try:
                    download_image(img_url, out_file)
                    print(f"  ✓ Downloaded {os.path.basename(out_file)} ({os.path.getsize(out_file)} bytes)")
                    results[slug] = {
                        "img_path": f"/assets/products/{slug}.jpg",
                        "img_url": img_url,
                        "asin": new_asin
                    }
                except Exception as e:
                    print(f"  ✗ Failed to download {img_url}: {e}")
            else:
                print(f"  ✗ Could not find image for {slug}")
            time.sleep(0.3)
        else:
            print(f"[{idx:02d}/54] SaaS Product: {slug} (will generate branded visual)")
            results[slug] = {
                "img_path": f"/assets/gear/{slug}.png",
                "img_url": "",
                "asin": ""
            }

    print(f"\nCompleted! Downloaded {len([k for k, v in results.items() if v['img_url']])} product photos.")
    
    import json
    with open("/Users/bishal/ai_toolkit_pro_web/product_images_map.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
