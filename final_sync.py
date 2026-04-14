import os
import re

def final_sync_fix():
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['preview.html', 'preview2.html']]
    
    # Standard header structure that works globally
    working_header = """    <header id="main-header">
        <a href="index.html" class="logo-link"><img src="assets/logo.png" alt="임플라인치과 포천점" class="header-logo-img"></a>
        <div class="mobile-menu-btn">
            <span></span>
            <span></span>
            <span></span>
        </div>
        <nav class="desktop-nav">
"""

    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Remove ANY floating mobile-menu-btn outside header
        content = re.sub(r'<body>\s*<div class="mobile-menu-btn">.*?</div>', '<body>', content, flags=re.DOTALL)
        
        # 2. Re-standardize the header interior
        # We target from <header id="main-header"> up to <nav class="desktop-nav">
        header_regex = re.compile(r'<header id="main-header">.*?(<nav class="desktop-nav">)', re.DOTALL)
        content = header_regex.sub(working_header, content)
        
        # 3. Specific cleanup for index.html if diagnostic styles remained
        if filename == 'index.html':
            content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
            content = re.sub(r'\s*home-body\s*', '', content)
            content = content.replace(' class=""', '') # cleanup empty class tags
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Synchronized {len(html_files)} files to ultimate standard.")

if __name__ == "__main__":
    final_sync_fix()
