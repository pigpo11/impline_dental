import os
import glob
import re

hero_images = {
    "wisdom-tooth.html": "assets/ct_room.png",
    "implant.html": "assets/implant.png",
    "sleep-treatment.html": "assets/포천 임플라인치과/실내3.jpg",
    "save-tooth.html": "assets/포천 임플라인치과/실내4.jpg",
    "cavity.html": "assets/포천 임플라인치과/실내4.jpg",
    "nerve.html": "assets/포천 임플라인치과/실내4.jpg",
    "scaling.html": "assets/포천 임플라인치과/실내4.jpg",
    "gums.html": "assets/포천 임플라인치과/실내4.jpg",
    "orthodontics.html": "assets/포천 임플라인치과/실내2.jpg",
    "whitening.html": "assets/포천 임플라인치과/실내2.jpg",
    "tmj.html": "assets/포천 임플라인치과/실내2.jpg",
}

def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove hero-small-image and hero-left-images
    # Matches <div class="hero-small-image ...">...</div> including nested contents
    # We'll use a simpler regex for the start and then try to find the balancing </div> if needed, 
    # but since these are usually empty or have comments, we can match explicitly.
    content = re.sub(r'<!--[^>]*작은 이미지 배치용 div[^>]*-->\s*<div class="hero-small-image[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="hero-small-image[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="hero-left-images[^>]*>.*?</div>', '', content, flags=re.DOTALL)

    # 2. Fix subpage main-hero-img
    filename = os.path.basename(filepath)
    if filename in hero_images:
        hero_src = hero_images[filename]
        # Find the main-hero-img div and insert the img tag
        pattern = r'(<div[^>]*class="[^"]*main-hero-img[^"]*"[^>]*>)(?!\s*<img)'
        img_tag = f'\n                        <img src="{hero_src}" alt="메인 이미지" style="width: 100%; height: 100%; object-fit: cover; border-radius: inherit;">'
        content = re.sub(pattern, rf'\1{img_tag}', content)

    # 3. Fix other generic placeholders
    # We'll use a pool of images
    pool = ["assets/포천 임플라인치과/실내1.jpg", "assets/포천 임플라인치과/실내2.jpg", "assets/포천 임플라인치과/실내3.jpg", "assets/포천 임플라인치과/실내4.jpg"]
    
    def replacer(match):
        full_div = match.group(0)
        # Choose based on class or just rotate
        if 'map-placeholder' in full_div:
            src = "assets/포천 임플라인치과/외관 (1).jpg"
        elif 'process-img' in full_div:
            src = "assets/포천 임플라인치과/실내2.jpg"
        else:
            src = pool[0] # Just use one consistently for now or pick based on count
            
        return full_div + f'\n    <img src="{src}" alt="병원 이미지" style="width: 100%; height: 100%; object-fit: cover; border-radius: inherit;">'

    # Match divs with image-placeholder that don't have an img yet
    # Note: about.html and index.html already have some manual fixes, so be careful.
    content = re.sub(r'(<div[^>]*class="[^"]*image-placeholder[^"]*"[^>]*>)(?!\s*<img)', replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob("*.html"):
    if filepath == "index.html":
        # index.html just needs removal of hero-small if any (unlikely)
        with open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'<div class="hero-small-image[^>]*>.*?</div>', '', c, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
    else:
        fix_html(filepath)

print("Image restoration and small-image removal complete!")
