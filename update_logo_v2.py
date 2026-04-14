import os
import re

def update_logo_v2():
    # Remove inline height to allow CSS media queries to work
    new_logo_html = '<a href="index.html" class="logo-link"><img src="assets/logo.png" alt="임플라인치과 포천점" class="header-logo-img"></a>'
    
    # Pattern to match the logo link we just created or the old one
    pattern = re.compile(r'<a href="index\.html" class="logo".*?>.*?</a>', re.DOTALL)
    
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
                print(f"Updated logo link in {file}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    update_logo_v2()
