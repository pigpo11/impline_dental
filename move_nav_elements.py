import os
import re

def move_mobile_nav_elements():
    # Move overlay and menu outside the header tag
    # Existing structure inside <header>:
    # <nav class="desktop-nav">...</nav>
    # <div class="mobile-nav-overlay"></div>
    # <div class="mobile-nav-menu">...</div>
    # </header>
    
    pattern = re.compile(r'(<div class="mobile-nav-overlay"></div>\s*<div class="mobile-nav-menu">.*?</div>\s*)(</header>)', re.DOTALL)
    
    files_updated = 0
    for file in os.listdir('.'):
        if file.endswith('.html'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                # Extract the elements and put them after </header>
                matches = pattern.search(content)
                nav_elements = matches.group(1)
                new_content = pattern.sub(r'</header>\n    ' + nav_elements.strip(), content)
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f"Moved mobile nav elements in {file}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    move_mobile_nav_elements()
