import os
import glob
import re

new_html = """<div class="quick-menu">
        <a href="#" class="quick-item" title="네이버 예약">
            <svg viewBox="0 0 24 24" width="30" height="30" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 6h16v14c0 1.1-.9 2-2 2H6c-1.1 0-2-.9-2-2V6z" fill="none" stroke="#333" stroke-width="2"/>
                <path d="M4 10h16v-4c0-1.1-.9-2-2-2H6c-1.1 0-2 .9-2 2v4z" fill="#333"/>
                <rect x="8" y="13" width="8" height="7" fill="#333" rx="1"/>
                <path d="M10.5 18.5v-4h1.2l1.6 2.5v-2.5h1.2v4h-1.2l-1.6-2.6v2.6h-1.2z" fill="#fff"/>
                <path d="M8 2v4M16 2v4" stroke="#333" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <span>네이버 예약</span>
        </a>
        <a href="#" class="quick-item" title="네이버블로그">
            <svg viewBox="0 0 24 24" width="30" height="30" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 6c0-2.2 1.8-4 4-4h8c2.2 0 4 1.8 4 4v9c0 2.2-1.8 4-4 4h-2.5l-3.5 4v-4H8c-2.2 0-4-1.8-4-4V6z" fill="#333"/>
                <text x="12" y="15" font-family="'Arial Black', sans-serif" font-weight="900" font-size="8.5" fill="#fff" text-anchor="middle">blog</text>
            </svg>
            <span>네이버블로그</span>
        </a>
        <a href="#" class="quick-item" title="톡톡 상담">
            <svg viewBox="0 0 24 24" width="30" height="30" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 7c0-2.2 1.8-4 4-4h8c2.2 0 4 1.8 4 4v6c0 2.2-1.8 4-4 4h-2.5L9 20v-3H8c-2.2 0-4-1.8-4-4V7z" fill="#fff" stroke="#333" stroke-width="2.5" stroke-linejoin="round"/>
                <path d="M4 14c0 2.2 1.8 4 4 4h1v3l2.8-2l0 0M21 7v6c0 2.2-1.8 4-4 4h-4" fill="none" stroke="#333" stroke-width="4.5" stroke-linejoin="miter" stroke-linecap="round"/>
                <rect x="9" y="9" width="2" height="4" rx="1" fill="#333"/>
                <rect x="15" y="9" width="2" height="4" rx="1" fill="#333"/>
            </svg>
            <span>톡톡 상담</span>
        </a>
        <a href="#" class="quick-item" title="카카오톡">
            <svg viewBox="0 0 24 24" width="30" height="30" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 4c-5.5 0-10 3.5-10 7.8 0 2.7 1.6 5.1 4.1 6.6L5 23l5.3-3.6c.5.1 1.1.1 1.7.1 5.5 0 10-3.5 10-7.8S17.5 4 12 4z" fill="#333"/>
                <text x="12" y="15" font-family="'Arial Black', sans-serif" font-weight="900" font-size="8.5" fill="#fff" text-anchor="middle">TALK</text>
            </svg>
            <span>카카오톡</span>
        </a>
        <a href="#" class="quick-item" title="인스타그램">
            <svg viewBox="0 0 24 24" width="30" height="30" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="#333" stroke-width="2.5"/>
                <circle cx="12" cy="12" r="4.5" fill="none" stroke="#333" stroke-width="2.5"/>
                <circle cx="17" cy="7" r="1.5" fill="#333"/>
            </svg>
            <span>인스타그램</span>
        </a>
    </div>"""

pattern = re.compile(r'<div class="quick-menu">.*?</div>\s+</div>', re.DOTALL)

count = 0
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if 'class="quick-menu"' in content and '<svg' not in content[content.find('class="quick-menu"'):content.find('class="quick-menu"')+200]:
        # only replace if not already replaced
        new_content = pattern.sub(new_html, content, count=1)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
print(f"Replaced quick menu in {count} HTML files using regex.")
