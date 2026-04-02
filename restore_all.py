import os
import glob
import re

# 1. The Perfect Vector SVG Menu
svg_menu = """<div class="quick-menu">
        <a href="#" class="quick-item" title="네이버 예약">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
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
                <path d="M 17 24 v 16 Z" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="21" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2.5"/>
                <path d="M 28 24 v 16 Z" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="36" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2.5"/>
                <circle cx="47" cy="36" r="4" fill="none" stroke="#fff" stroke-width="2.5"/>
                <path d="M 51 36 v 5 A 4 4 0 0 1 43 41" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
            <span>네이버블로그</span>
        </a>
        <a href="#" class="quick-item" title="톡톡 상담">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M 16 19 H 48 A 10 10 0 0 1 58 29 V 43 A 10 10 0 0 1 48 53 H 38 L 28 62 V 53 H 16 A 10 10 0 0 1 6 43 V 29 A 10 10 0 0 1 16 19 Z" fill="#333"/>
                <path d="M 16 16 H 48 A 10 10 0 0 1 58 26 V 40 A 10 10 0 0 1 48 50 H 38 L 28 59 V 50 H 16 A 10 10 0 0 1 6 40 V 26 A 10 10 0 0 1 16 16 Z" fill="#fff" stroke="#333" stroke-width="6" stroke-linejoin="round"/>
                <rect x="22" y="27" width="6" height="12" rx="3" fill="#333"/>
                <rect x="36" y="27" width="6" height="12" rx="3" fill="#333"/>
            </svg>
            <span>톡톡 상담</span>
        </a>
        <a href="#" class="quick-item" title="카카오톡">
            <svg viewBox="0 0 64 64" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
                <path d="M 32 12 c -16 0 -28 9 -28 20 c 0 7 5 13 12 16.5 l -3.5 10 l 12 -8 c 2.5 0.5 5 1 7.5 1 c 16 0 28 -9 28 -20 S 48 12 32 12 Z" fill="#333"/>
                <path d="M 15 28 H 23 M 19 28 V 40" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                <path d="M 25 40 L 29 28 L 33 40 M 27 36 H 31" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M 37 28 V 40 H 42" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
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

# 2. Correct Footer Content (Subpage Style)
new_footer_info = """<div class="footer-info-area">
                <div class="info-row">
                    <div class="label">주소</div>
                    <div class="value">경기도 포천시 소흘읍 송우로 61, 7층 (임플라인치과의원 포천점)</div>
                </div>
                <div class="info-row">
                    <div class="label">예약안내</div>
                    <div class="value tel">031-541-2875</div>
                </div>
                <div class="info-row">
                    <div class="label">진료시간</div>
                    <div class="value times">
                        <span>월/수/금</span> 09:30 - 18:30<br>
                        <span>화/목(야간)</span> 09:30 - 20:30<br>
                        <span>토요일</span> 09:30 - 14:00<br>
                        <span>점심시간</span> 13:00 - 14:00<br>
                        <span class="holiday">휴진</span> 일요일, 공휴일
                    </div>
                </div>
                <div class="footer-bottom-links">
                    <a href="index.html">임플라인치과</a>
                    <a href="#">이용약관</a>
                    <a href="#">개인정보 취급방침</a>
                </div>
                <p class="copyright">© Copyright 2022. 임플라인치과의원 포천점 All Rights Reserved.</p>
            </div>"""

for filepath in glob.glob("*.html"):
    if filepath in ["index.html", "about.html"]:
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Repair Quick Menu
    content = re.sub(r'<div class="quick-menu">.*?</div>', svg_menu, content, flags=re.DOTALL)
    
    # Repair Footer Info
    content = re.sub(r'<div class="footer-info-area">.*?<p class="copyright">.*?</p>\s+</div>', new_footer_info, content, flags=re.DOTALL)
    
    # Correct Map Area
    content = content.replace('<div class="image-placeholder map-placeholder">\n                    <!-- 지도 영역 -->\n                </div>', '<img src="assets/포천 임플라인치과/외관 (1).jpg" alt="약도" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">')

    # Fix Specialty Text (Heo In-beom is Integrated Dentistry)
    content = content.replace("구강악안면외과 전문의", "통합치의학과 전문의")
    content = content.replace("김규대", "허인범")
    
    # Specific fix for subpage hero images? 
    # Let's keep them as placeholders if no specific request, but user might want them.
    # However, for now, let's just make the PAGE functional and accurate.

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Global restoration of all subpages complete!")
