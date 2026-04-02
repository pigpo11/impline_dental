import os
import re
import random

images = [
    "assets/포천 임플라인치과/실내1.jpg",
    "assets/포천 임플라인치과/실내2.jpg",
    "assets/포천 임플라인치과/실내3.jpg",
    "assets/포천 임플라인치과/실내4.jpg",
    "assets/implant.png",
    "assets/ct_room.png"
]

map_image = "assets/포천 임플라인치과/외관 (1).jpg"

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

def replace_placeholder(match):
    full_tag = match.group(0)
    
    if 'map-placeholder' in full_tag:
        img_src = map_image
    elif 'implant' in full_tag or 'ct_room' in full_tag:
        img_src = "assets/implant.png"
    else:
        img_src = random.choice(images)
    
    img_tag = f'\n    <img src="{img_src}" alt="치과 이미지" style="width: 100%; height: 100%; object-fit: cover; border-radius: inherit;">'
    
    # To avoid double insertion if script is run multiple times
    return full_tag + img_tag

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <div ... class="...image-placeholder..." ...> that does NOT immediately have an <img following it
    # We will just do a simple substitution and check if <img is already inside. Since this is a one-off, we can just replace.
    # To ensure we don't duplicate, we could read, then findall, then replace only if no <img> is in the next few characters.
    
    # We use a regex that matches the div tag
    pattern = re.compile(r'(<div\s+[^>]*class="[^"]*image-placeholder[^"]*"[^>]*>)(?!\s*<img)')
    
    new_content = pattern.sub(replace_placeholder, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Processed {len(html_files)} files.")
