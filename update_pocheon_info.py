import os
import re

# Information provided by the user
pocheon_info = {
    "name": "임플라인치과의원 포천점",
    "address_full": "경기 포천시 일동면 화동로 1052-1 3층",
    "business_number": "374-92-01491",
    "representative": "허인범",
    "tel": "031-8089-7582",
    "fax": "031-8089-7585",
    "copyright": "© Copyright 2022. 임플라인치과의원 포천점 All Rights Reserved."
}

def update_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update main-new-footer (Table part)
    # Address
    content = re.sub(r'(<div class="info-label">주소</div>\s*<div class="info-value">)\s*.*?(?=<a|</div>)', 
                     rf'\1\n                            {pocheon_info["address_full"]}<br>\n                            ', content, flags=re.DOTALL)
    
    # Parking (Since address changed, parking info might be invalid, but I'll keep it or update tel)
    content = re.sub(r'\(발렛파킹 불가 시 전화로 문의해주세요 .*?\)', 
                     f'(발렛파킹 불가 시 전화로 문의해주세요 {pocheon_info["tel"]})', content)

    # Tel Number in table
    content = re.sub(r'(<div class="tel-number".*?>).*?(</div>)', 
                     rf'\1{pocheon_info["tel"]}\2', content)

    # 2. Update main-new-footer (Bottom part)
    bottom_regex = r'<div class="footer-bottom-info">.*?</div>'
    bottom_replacement = f"""<div class="footer-bottom-info">
                <p>{pocheon_info["name"]} | 대표원장: {pocheon_info["representative"]} | 사업자등록번호 {pocheon_info["business_number"]} | T. {pocheon_info["tel"]} | F. {pocheon_info["fax"]}</p>
                <p>{pocheon_info["address_full"]}</p>
                <p class="copyright" style="margin-top: 5px;">{pocheon_info["copyright"]}</p>
            </div>"""
    content = re.sub(bottom_regex, bottom_replacement, content, flags=re.DOTALL)

    # 3. Update sub-footer (Map footer style)
    # Address
    content = re.sub(r'(<div class="label">주소</div>\s*<div class="value">).*?(</div>)', 
                     rf'\1{pocheon_info["address_full"]} ({pocheon_info["name"]})\2', content)
    # Tel
    content = re.sub(r'(<div class="label">예약안내</div>\s*<div class="value tel">).*?(</div>)', 
                     rf'\1{pocheon_info["tel"]}\2', content)
    # Copyright
    content = re.sub(r'(<p class="copyright">).*?(</p>)', 
                     rf'\1{pocheon_info["copyright"]}\2', content)

    # 4. Update About.html specific table
    if "about.html" in file_path:
        # Address in table
        content = re.sub(r'(<th>오시는길</th>\s*<td>).*?(</td>)', 
                         rf'\1{pocheon_info["address_full"]} ({pocheon_info["name"]})\2', content)
        # Tel in table
        content = re.sub(r'(<th>예약안내</th>\s*<td>).*?(</td>)', 
                         rf'\1{pocheon_info["tel"]}\2', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Target all html files in the root
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        update_html_file(filename)
        print(f"Updated {filename}")
