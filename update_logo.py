import os
import re

def update_logo():
    new_logo_html = '<a href="index.html" class="logo" style="display: flex; align-items: center;"><img src="assets/logo.png" alt="임플라인치과 포천점" style="height: 50px; width: auto;"></a>'
    
    # Pattern to match the logo link with variations in styles but same text
    pattern = re.compile(r'<a href="index\.html" class="logo".*?>임플라인치과 <span>\| 포천점</span></a>', re.DOTALL)
    
    files_updated = 0
    for file in os.listdir('.'):
        if file.endswith('.html'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                new_content = pattern.sub(new_logo_html, content)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f"Updated logo in {file}")
            else:
                # Try a simpler match if the first one fails
                pattern2 = re.compile(r'<a href="index\.html" class="logo".*?>.*?</a>', re.DOTALL)
                # But we must be careful not to replace other logos if any. 
                # Given the context, this should be fine.
                pass 

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    update_logo()
