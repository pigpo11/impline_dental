import os
import re
import glob

# Step 1: Restore structure from 3041d89
os.system("git checkout 3041d89 -- *.html")

# Step 2: Global info replacement
info = {
    "addr_new": "경기도 포천시 소흘읍 송우로 61, 7층 (임플라인치과의원 포천점)",
    "tel_new": "031-541-2875",
    "doctor_new": "허인범",
    "specialty_new": "보건복지부 인증 통합치의학과 전문의",
    "hours_new": "월/수/금 09:30-18:30, 화/목(야간) 09:30-20:30, 토 09:30-14:00"
}

hero_images = {
    "wisdom-tooth.html": "assets/ct_room.png",
    "implant.html": "assets/implant.png",
    "sleep-treatment.html": "assets/포천 임플라인치과/실내3.jpg",
    "about.html": "assets/포천 임플라인치과/실내3.jpg"
}

def master_fix(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Restoration of Pocheon Specifics
    content = content.replace("김규대", info["doctor_new"])
    content = content.replace("구강악안면외과 전문의", info["specialty_new"])
    content = content.replace("경기 포천시 일동면 화동로 1052-1 3층", info["addr_new"])
    content = content.replace("031-8089-7582", info["tel_new"])
    
    # Hour replacement (multiple variants)
    content = re.sub(r'09:30 - 18:30.*?09:30 - 13:30', info["hours_new"], content, flags=re.DOTALL)

    # Footer Info Restoration
    footer_pattern = re.compile(r'<div class="footer-info-area">.*?<p class="copyright">.*?</p>\s+</div>', re.DOTALL)
    new_footer = f"""<div class="footer-info-area">
                <div class="info-row">
                    <div class="label">주소</div>
                    <div class="value">{info["addr_new"]}</div>
                </div>
                <div class="info-row">
                    <div class="label">예약안내</div>
                    <div class="value tel">{info["tel_new"]}</div>
                </div>
                <div class="info-row">
                    <div class="label">진료시간</div>
                    <div class="value times">
                        <span>월/수/금</span> 09:30 - 18:30<br>
                        <span>화/목(야간)</span> 09:30 - 20:30<br>
                        <span>토요일</span> 09:30 - 14:00<br>
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
    content = footer_pattern.sub(new_footer, content)

    # Images: Hero Image Fix
    fname = os.path.basename(filepath)
    if fname in hero_images:
        src = hero_images[fname]
        def repl(m):
            return m.group(1) + f'\n<img src="{src}" style="width:100%;height:100%;object-fit:cover;">'
        content = re.sub(r'(<div[^>]*class="[^"]*main-hero-img[^"]*"[^>]*>)(?!\s*<img)', repl, content)

    # Remove hero-small-image
    content = re.sub(r'<div class="hero-small-image[^>]*>.*?</div>', '', content, flags=re.DOTALL)

    # Remove Quick Menu (The goal of THIS turn)
    # Be VERY careful. Match from <!-- Floating Quick Menu --> until AND INCLUDING the </div> of the menu.
    # Our quick menu block in 3041d89 is usually:
    # <!-- Floating Quick Menu -->
    # <div class="quick-menu"> ... </div>
    content = re.sub(r'<!-- Floating Quick Menu -->\s*<div class="quick-menu">.*?</div>\s+</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="quick-menu">.*?</div>\s+</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="quick-menu">.*?</div>', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Special Fix for index.html because it has a slightly different structure
def fix_index():
    with open("index.html", "r", encoding="utf-8") as f:
        c = f.read()
    
    # Restore Hero Section if missing
    if "hero-text" not in c:
        hero_section = """
    <!-- Main Content -->
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-content">
                <div class="hero-text">
                    <h1>소통하는 치과,<br>환자를 먼저 생각하는<br>임플라인치과 포천점입니다.</h1>
                    <p>우리는 환자를 가족처럼 생각하며, 정직하고 정직한 진단으로<br>환자에게 꼭 필요한 진료만을 시행합니다.</p>
                </div>
                <div class="hero-image"></div>
            </div>
        </section>"""
        c = c.replace('</header>', '</header>' + hero_section)
    
    # Add <main> if missing
    if "<main>" not in c:
        c = c.replace('</header>', '</header>\n    <main>')
    
    # Global info
    c = c.replace("김규대", "허인범")
    c = c.replace("구강악안면외과 전문의", "통합치의학과 전문의")
    c = c.replace("031-8089-7582", "031-541-2875")
    
    # Quick menu
    c = re.sub(r'<!-- Floating Quick Menu -->\s*<div class="quick-menu">.*?</div>\s+</div>', '', c, flags=re.DOTALL)
    c = re.sub(r'<div class="quick-menu">.*?</div>\s+</div>', '', c, flags=re.DOTALL)
    c = re.sub(r'<div class="quick-menu">.*?</div>', '', c, flags=re.DOTALL)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(c)

for fpath in glob.glob("*.html"):
    if fpath == "index.html":
        fix_index()
    elif fpath not in ["preview.html", "preview2.html"]:
        master_fix(fpath)

# CSS Hide
css_path = "style.css"
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    if ".quick-menu {" in css and "display: none" not in css:
        css = css.replace(".quick-menu {", ".quick-menu { display: none !important; ", 1)
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)

print("Master restoration and Quick Menu removal complete.")
