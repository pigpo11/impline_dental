import os
import re
import glob

# 1. Info Definition
pocheon = {
    "name": "임플라인치과의원 포천점",
    "doctor": "허인범",
    "address": "경기도 포천시 소흘읍 송우로 61, 7층 (임플라인치과의원 포천점)",
    "tel": "031-541-2875",
    "specialty": "보건복지부 인증 통합치의학과 전문의",
    "hours_html": """<div class="time-col">월·수·금</div><div class="time-col">09:30 ~ 18:30</div>
                            <div class="time-col">화·목(야간)</div><div class="time-col">09:30 ~ 20:30</div>
                            <div class="time-col">토요일</div><div class="time-col">09:30 ~ 14:00</div>
                            <div class="time-col">점심시간</div><div class="time-col">13:00 ~ 14:00</div>""",
    "hours_list": """<span>월/수/금</span> 09:30 - 18:30<br>
                        <span>화/목(야간)</span> 09:30 - 20:30<br>
                        <span>토요일</span> 09:30 - 14:00<br>
                        <span>점심시간</span> 13:00 - 14:00<br>
                        <span class="holiday">휴진</span> 일요일, 공휴일"""
}

# 2. Hero Image Map
hero_images = {
    "wisdom-tooth.html": "assets/ct_room.png",
    "implant.html": "assets/implant.png",
    "sleep-treatment.html": "assets/포천 임플라인치과/실내3.jpg",
    "about.html": "assets/포천 임플라인치과/실내3.jpg"
}

def clean_info(content):
    # Address fixes
    content = re.sub(r'서울특별시 송파구 백제고분로.*?\)', pocheon["address"], content)
    content = content.replace("서울특별시 송파구 백제고분로 198, GM빌딩 2층(9호선 삼전역 3번 출구 앞)", pocheon["address"])
    content = content.replace("경기 포천시 일동면 화동로 1052-1 3층", pocheon["address"])
    
    # Tel fixes
    content = content.replace("02 415 2080", pocheon["tel"])
    content = content.replace("02-415-2080", pocheon["tel"])
    content = content.replace("031-8089-7582", pocheon["tel"])
    
    # Doctor / Specialty
    content = content.replace("김규대", pocheon["doctor"])
    content = content.replace("구강악안면외과 전문의", pocheon["specialty"])
    
    # Hours (grid)
    content = re.sub(r'<div class="times-grid">.*?</div>\s+</div>', f'<div class="times-grid">{pocheon["hours_html"]}</div>', content, flags=re.DOTALL)
    
    # Hours (list/footer)
    content = re.sub(r'<div class="value times">.*?</div>', f'<div class="value times">{pocheon["hours_list"]}</div>', content, flags=re.DOTALL)
    
    # Clinic Name
    content = content.replace("한걸음더치과", "임플라인치과의원")
    
    # Parking Phone
    content = re.sub(r'비상등을 켜주세요.*?02 415 2080', f'전화로 문의해주세요 {pocheon["tel"]}', content, flags=re.DOTALL)

    return content

def fill_images(filepath, content):
    filename = os.path.basename(filepath)
    
    # Main Hero Img (Subpages)
    if filename in hero_images:
        src = hero_images[filename]
        content = re.sub(r'(<div[^>]*class="[^"]*main-hero-img[^"]*"[^>]*>)(?!\s*<img)', rf'\1\n<img src="{src}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;">', content)

    # Doctor Profile
    if 'profile-image' in content or 'doctor-image' in content:
        content = re.sub(r'(<div[^>]*class="[^"]*(?:profile-image|doctor-image)[^"]*"[^>]*>)(?!\s*<img)', rf'\1\n<img src="assets/KakaoTalk_20260316_125348764_01.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;">', content)

    # Map / Location
    content = re.sub(r'(<div[^>]*class="[^"]*(?:info-map|map-placeholder)[^"]*"[^>]*>)(?!\s*<img)', rf'\1\n<img src="assets/포천 임플라인치과/외관 (1).jpg" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;">', content)

    # All other image-placeholders
    pool = ["assets/포천 임플라인치과/실내1.jpg", "assets/포천 임플라인치과/실내2.jpg", "assets/포천 임플라인치과/실내3.jpg", "assets/포천 임플라인치과/실내4.jpg"]
    
    placeholders = list(re.finditer(r'(<div[^>]*class="[^"]*image-placeholder[^"]*"[^>]*>)(?!\s*<img)', content))
    
    # Replace from end to avoid index shift
    for i, match in enumerate(reversed(placeholders)):
        src = pool[i % len(pool)]
        tag = f'\n<img src="{src}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;">'
        start, end = match.span()
        content = content[:end] + tag + content[end:]

    return content

for filepath in glob.glob("*.html"):
    if filepath in ["preview.html", "preview2.html"]: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    c = clean_info(c)
    c = fill_images(filepath, c)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Final Image Filling and Info Restoration Complete.")
