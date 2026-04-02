import os
import glob

# 1. New Quick Menu HTML
new_html = """<div class="quick-menu">
        <a href="#" class="quick-item" title="네이버 예약">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <!-- Calendar -->
                <path d="M 14 16 A 6 6 0 0 0 8 22 V 52 A 6 6 0 0 0 14 58 H 50 A 6 6 0 0 0 56 52 V 22 A 6 6 0 0 0 50 16 Z" fill="none" stroke="#333" stroke-width="5" stroke-linejoin="round"/>
                <path d="M 8 26 h 48" stroke="#333" stroke-width="5"/>
                <rect x="20" y="10" width="6" height="10" rx="3" fill="#333"/>
                <rect x="38" y="10" width="6" height="10" rx="3" fill="#333"/>
                <rect x="23" y="34" width="18" height="16" rx="2" fill="#333"/>
                <path d="M 28 46 v -8 l 8 8 v -8" fill="none" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>
            </svg>
            <span>네이버 예약</span>
        </a>
        <a href="#" class="quick-item" title="네이버블로그">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M 12 14 H 52 A 10 10 0 0 1 62 24 V 40 A 10 10 0 0 1 52 50 H 38 L 32 58 L 30 50 H 12 A 10 10 0 0 1 2 40 V 24 A 10 10 0 0 1 12 14 Z" fill="#333" stroke="#333" stroke-linejoin="round"/>
                <!-- b -->
                <path d="M 17 24 v 16 Z" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="21" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2.5"/>
                <!-- l -->
                <path d="M 28 24 v 16 Z" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                <!-- o -->
                <circle cx="36" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2.5"/>
                <!-- g -->
                <circle cx="47" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2.5"/>
                <path d="M 51 36 v 5 A 4 4 0 0 1 43 41" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
            <span>네이버블로그</span>
        </a>
        <a href="#" class="quick-item" title="톡톡 상담">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <!-- Drop shadow behind -->
                <path d="M 16 19 H 48 A 10 10 0 0 1 58 29 V 43 A 10 10 0 0 1 48 53 H 38 L 28 62 V 53 H 16 A 10 10 0 0 1 6 43 V 29 A 10 10 0 0 1 16 19 Z" fill="#333"/>
                <!-- Bubble over it -->
                <path d="M 16 16 H 48 A 10 10 0 0 1 58 26 V 40 A 10 10 0 0 1 48 50 H 38 L 28 59 V 50 H 16 A 10 10 0 0 1 6 40 V 26 A 10 10 0 0 1 16 16 Z" fill="#fff" stroke="#333" stroke-width="6" stroke-linejoin="round"/>
                <rect x="22" y="27" width="6" height="12" rx="3" fill="#333"/>
                <rect x="36" y="27" width="6" height="12" rx="3" fill="#333"/>
            </svg>
            <span>톡톡 상담</span>
        </a>
        <a href="#" class="quick-item" title="카카오톡">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M 32 12 c -16 0 -28 9 -28 20 c 0 7 5 13 12 16.5 l -3.5 10 l 12 -8 c 2.5 0.5 5 1 7.5 1 c 16 0 28 -9 28 -20 S 48 12 32 12 Z" fill="#333"/>
                <!-- T -->
                <path d="M 15 28 H 23 M 19 28 V 40" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                <!-- A -->
                <path d="M 25 40 L 29 28 L 33 40 M 27 36 H 31" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                <!-- L -->
                <path d="M 37 28 V 40 H 42" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                <!-- K -->
                <path d="M 46 28 V 40 M 52 28 L 46 34 L 52 40" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>카카오톡</span>
        </a>
        <a href="#" class="quick-item" title="인스타그램">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <rect x="8" y="8" width="48" height="48" rx="14" fill="none" stroke="#333" stroke-width="6"/>
                <circle cx="32" cy="32" r="11" fill="none" stroke="#333" stroke-width="6"/>
                <circle cx="45" cy="19" r="4" fill="#333"/>
            </svg>
            <span>인스타그램</span>
        </a>
    </div>"""

# Ensure checkout of pristine HTML
os.system("git checkout 3041d89 -- *.html")

# 2. Iterate and apply specific updates
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Safe exact string replacement for quick menu!
    old_menu_start = content.find('<div class="quick-menu">')
    if old_menu_start != -1:
        # Find the END of the quick-menu by counting divs, or just find the explicit last item.
        # Original block ends after 인스타그램 </div>
        target = '<span>인스타그램</span>\n        </div>\n    </div>'
        old_menu_end = content.find(target, old_menu_start)
        if old_menu_end != -1:
            old_menu_end += len(target)
            old_block = content[old_menu_start:old_menu_end]
            content = content.replace(old_block, new_html)

    # 3. Specific file fixes that were requested earlier in this session
    if filepath == "index.html":
        content = content.replace('src="assets/포천 임플라인치과/원장.jpg"', 'src="assets/KakaoTalk_20260316_125348764_01.jpg"')
    elif filepath == "about.html":
        content = content.replace('src="assets/포천 임플라인치과/원장.jpg"', 'src="assets/KakaoTalk_20260316_125348764_01.jpg"')
        # user requested '실내2.jpg' in first gallery slot
        content = content.replace('src="assets/포천 임플라인치과/실내1.jpg" alt="내부모습 1"', 'src="assets/포천 임플라인치과/실내2.jpg" alt="내부모습 1"')
        # info logo box
        content = content.replace("""<div class="info-logo-box">
                    <div class="box-title">
                        임플<br>
                        라인<br>
                        <span>더 —</span>
                    </div>
                </div>""", """<div class="info-logo-box" style="background: none; overflow: hidden; border-radius: 4px;">
                    <img src="assets/포천 임플라인치과/실내1.jpg" alt="접수처(인포데스크) 이미지" style="width: 100%; height: 100%; object-fit: cover;">
                </div>""")

        # Also earlier removed hero-small-image from subpages, but wait... 
        # Those were done BEFORE 3041d89 so they MIGHT be safely untouched or if I need them, they are small.
        # BUT wait! We checked out 3041d89. So hero-small-image MIGHT be back.
        content = content.replace('<div class="hero-small-image">\n                    ', '<div class="hero-small-image" style="display:none;">\n                    ')
        content = content.replace('<div class="hero-left-images">\n                    ', '<div class="hero-left-images" style="display:none;">\n                    ')

    else:
        # Hide hero left images on other subpages
        content = content.replace('<div class="hero-small-image">\n                    ', '<div class="hero-small-image" style="display:none;">\n                    ')
        content = content.replace('<div class="hero-left-images">\n                    ', '<div class="hero-left-images" style="display:none;">\n                    ')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Restoration complete!")
