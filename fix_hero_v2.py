import os
import re

path = 'index.html'

try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
except:
    with open(path, 'r', encoding='cp949', errors='ignore') as f:
        content = f.read()

# Regular expression to find the h1 tag in the hero section
# Pattern targets the h1 with font-size 48px
pattern = r'(<h1 style="font-size: 48px; line-height: 1\.3;">)(.*?)(</h1>)'
replacement = r'\1안녕하세요. 임플라인치과입니다.<br><br>소신진료 & 최소진료<br>환자들의 편에서<br>진정한 진료를 하겠습니다.\3'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    print("Replacement made using regex.")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
else:
    print("Regex match failed. Printing current context around h1 for debugging...")
    h1_match = re.search(r'<h1.*?>.*?</h1>', content, re.DOTALL)
    if h1_match:
        print(f"Match found: {h1_match.group(0)}")
    else:
        print("No h1 tag found at all.")
