import os

path = 'index.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(path, 'r', encoding='cp949') as f:
        content = f.read()

print(f"Content start: {content[:1000]}")
old_text = '안녕하세요. 임플라인치과입니다.<br>소신진료'
new_text = '안녕하세요. 임플라인치과입니다.<br><br>소신진료'

if old_text in content:
    content = content.replace(old_text, new_text)
    print("Text replaced successfully.")
else:
    # Try alternate with different spacing or if it already has double break
    print("Target text not found exactly. Checking for variants...")
    if '안녕하세요. 임플라인치과입니다.<br><br>소신진료' in content:
        print("Already updated.")
    else:
        print("Content search failed. Check file content.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
