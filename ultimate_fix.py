import os
import re

def ultimate_fix():
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'preview.html' and f != 'preview2.html']
    
    # Target mobile menu button structure
    standard_btn = """    <div class="mobile-menu-btn">
        <span></span>
        <span></span>
        <span></span>
    </div>"""
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Remove ANY existing mobile-menu-btn (including #forced-mobile-btn)
        content = re.sub(r'<(div|button)[^>]*class=["\'][^"\']*mobile-menu-btn[^"\']*["\'][^>]*>.*?</\1>', '', content, flags=re.DOTALL)
        
        # 2. Specifically for index.html, remove the diagnostic style block
        if filename == 'index.html':
            content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
            content = re.sub(r'\s*home-body\s*', '', content) # Clean up class
            content = re.sub(r'<body[^>]*>', '<body>', content) # Reset body tag
            # Also remove diagnostic border from header
            content = content.replace(' style="border: 5px solid green !important;"', '')
        
        # 3. Inject standard button as FIRST child of body
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + standard_btn, content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Repaired {len(html_files)} files.")

if __name__ == "__main__":
    ultimate_fix()
