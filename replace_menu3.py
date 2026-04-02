import os
import glob
import re

new_html = """<div class="quick-menu">
        <a href="#" class="quick-item" title="네이버 예약">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M14 16 A 6 6 0 0 0 8 22 L 8 52 A 6 6 0 0 0 14 58 L 50 58 A 6 6 0 0 0 56 52 L 56 22 A 6 6 0 0 0 50 16 Z" fill="none" stroke="#333" stroke-width="5" stroke-linejoin="round"/>
                <path d="M10 26 h 44" stroke="#333" stroke-width="5"/>
                <rect x="23" y="34" width="18" height="15" rx="3" fill="#333"/>
                <path d="M28 45 v-6 l6 7 v-7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>
                <rect x="20" y="8" width="6" height="12" rx="3" fill="#333"/>
                <rect x="38" y="8" width="6" height="12" rx="3" fill="#333"/>
            </svg>
            <span>네이버 예약</span>
        </a>
        <a href="#" class="quick-item" title="네이버블로그">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 14 A 10 10 0 0 0 2 24 L 2 40 A 10 10 0 0 0 12 50 L 26 50 L 32 58 L 38 50 L 52 50 A 10 10 0 0 0 62 40 L 62 24 A 10 10 0 0 0 52 14 Z" fill="#333" stroke="#333" stroke-linejoin="round"/>
                <!-- Paths for 'blog' to be exactly identical everywhere -->
                <!-- b -->
                <path d="M17 26 v16 M17 38 A 3 3 0 1 1 17 38.1 Z" fill="#fff" fill-rule="evenodd"/>
                <path d="M17 34 c2 -2 6 -2 6 2 c0 4 -4 6 -6 3" fill="none" stroke="#fff" stroke-width="4"/>
                <path d="M17 26 v15" fill="none" stroke="#fff" stroke-width="4"/>
                <!-- l -->
                <path d="M28 26 v15" fill="none" stroke="#fff" stroke-width="4"/>
                <!-- o -->
                <ellipse cx="37" cy="38" rx="4" ry="4" fill="none" stroke="#fff" stroke-width="4"/>
                <!-- g -->
                <path d="M51 38 c-2 -2 -6 -2 -6 2 c0 4 4 6 6 3" fill="none" stroke="#fff" stroke-width="4"/>
                <path d="M51 34 v8 c0 4 -6 4 -6 2" fill="none" stroke="#fff" stroke-width="4"/>
            </svg>
            <span>네이버블로그</span>
        </a>
        <a href="#" class="quick-item" title="톡톡 상담">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <!-- Drop shadow behind -->
                <path d="M18 19 A 10 10 0 0 0 8 29 L 8 43 A 10 10 0 0 0 18 53 L 26 53 L 26 62 L 36 53 L 46 53 A 10 10 0 0 0 56 43 L 56 29 A 10 10 0 0 0 46 19 Z" fill="#333"/>
                <!-- White bubble -->
                <path d="M16 16 A 10 10 0 0 0 6 26 L 6 40 A 10 10 0 0 0 16 50 L 22 50 L 22 58 L 32 50 L 44 50 A 10 10 0 0 0 54 40 L 54 26 A 10 10 0 0 0 44 16 Z" fill="#fff" stroke="#333" stroke-width="6" stroke-linejoin="round"/>
                <rect x="18" y="27" width="5" height="10" rx="2.5" fill="#333"/>
                <rect x="35" y="27" width="5" height="10" rx="2.5" fill="#333"/>
            </svg>
            <span>톡톡 상담</span>
        </a>
        <a href="#" class="quick-item" title="카카오톡">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M32 12 c -16 0 -28 9 -28 20 c 0 7 5 13 12 16.5 l -3.5 10 l 12 -8 c 2.5 0.5 5 1 7.5 1 c 16 0 28 -9 28 -20 S 48 12 32 12 Z" fill="#333"/>
                <!-- T -->
                <path d="M15 28 h8 M19 28 v11" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
                <!-- A -->
                <path d="M28 39 l3 -11 l3 11 M29 35 h4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                <!-- L -->
                <path d="M38 28 v11 h5" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                <!-- K -->
                <path d="M46 28 v11 M51 28 l-4 6 l4 5" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
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

pattern = re.compile(r'<div class="quick-menu">.*?</div>\s+</div>', re.DOTALL)

count = 0
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if 'class="quick-menu"' in content:
        new_content = pattern.sub(new_html, content, count=1)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1

print(f"Replaced {count} HTML files.")
