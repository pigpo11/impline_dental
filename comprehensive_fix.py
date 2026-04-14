import os
import re

def fix_index_hero():
    path = 'index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add greeting and fix line breaks
    pattern = r'(<h1 style="font-size: 48px; line-height: 1\.3;">)(.*?)(</h1>)'
    replacement = r'\1안녕하세요. 임플라인치과입니다.<br><br>소신진료 & 최소진료<br>환자들의 편에서<br>진정한 진료를 하겠습니다.\3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html hero section")

def fix_copyright():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('Copyright 2022', 'Copyright 2021')
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated copyright in {filename}")

def fix_style_css():
    path = 'style.css'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("url('assets/hero_main.png')", "url('assets/hero_main_new.png')")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed style.css hero image")

def adjust_philosophy_section():
    path = 'index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target the Medical Philosophy section
    # Find the block and replace it with the adjusted ratio
    old_block = r'''<div class="feature-text" style="padding-left: 120px; flex: 1.5; min-width: 0;">'''
    new_block = r'''<div class="feature-text" style="flex: 1; min-width: 0;">'''
    content = content.replace(old_block, new_block)
    
    old_img = r'''<div class="feature-image" style="flex: 1.5; justify-content: center;">
                    <img src="assets/doctor_philosophy.jpg" style="width: 100%; max-width: 650px; height: auto; border-radius: 10px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                </div>'''
    new_img = r'''<div class="feature-image" style="flex: 1.2; display: flex; justify-content: flex-start; align-items: center;">
                    <img src="assets/doctor_philosophy.jpg" style="width: 100%; max-width: 800px; height: auto; border-radius: 15px; box-shadow: 0 30px 60px rgba(0,0,0,0.12);">
                </div>'''
    content = content.replace(old_img, new_img)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Adjusted Medical Philosophy section")

if __name__ == "__main__":
    fix_index_hero()
    fix_copyright()
    fix_style_css()
    adjust_philosophy_section()
