import os
import re

def add_hamburger_menu():
    # Insert hamburger button inside the header
    pattern = re.compile(r'(<nav>.*?</nav>)', re.DOTALL)
    
    # We will wrap the existing nav in a desktop-nav class and add a mobile-menu-btn
    hamburger_btn_html = '''
        <div class="mobile-menu-btn">
            <span></span>
            <span></span>
            <span></span>
        </div>
        <nav class="desktop-nav">
'''
    
    files_updated = 0
    for file in os.listdir('.'):
        if file.endswith('.html'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '<nav class="desktop-nav">' in content:
                continue # Already updated

            if '<nav>' in content:
                # Replace <nav> with our new structure
                new_content = content.replace('<nav>', hamburger_btn_html)
                new_content = new_content.replace('</nav>', '</nav>\n        <div class="mobile-nav-overlay"></div>\n        <div class="mobile-nav-menu">\n            <ul class="mobile-nav-list">\n                <li><a href="about.html">임플라인 소개</a></li>\n                <li><a href="wisdom-tooth.html">사랑니발치</a></li>\n                <li><a href="implant.html">임플란트</a></li>\n                <li><a href="sleep-treatment.html">수면치료</a></li>\n                <li><a href="save-tooth.html">자연치아살리기</a></li>\n                <li><a href="orthodontics.html">치아교정</a></li>\n                <li><a href="whitening.html">치아미백</a></li>\n                <li><a href="tmj.html">턱관절치료</a></li>\n            </ul>\n        </div>')
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f"Added mobile menu structure to {file}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    add_hamburger_menu()
