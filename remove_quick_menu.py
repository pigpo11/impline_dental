import os
import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Matches <div class="quick-menu"> till the closing </div> of that block
    # We'll use a regex that handles the nested divs inside (quick-item)
    # Our quick-menu block always starts with <div class="quick-menu"> 
    # and ends with 인스타그램 </a>\n    </div>
    
    pattern = re.compile(r'<!-- Floating Quick Menu -->\s*<div class="quick-menu">.*?</div>\s+</div>', re.DOTALL)
    new_content = pattern.sub('', content)
    
    # Just in case the comment was different or missing
    if new_content == content:
        pattern2 = re.compile(r'<div class="quick-menu">.*?</div>\s+</div>', re.DOTALL)
        new_content = pattern2.sub('', content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed quick-menu from {filepath}")

# Optional: Clean up style.css to prevent any ghost containers
with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Just hide the class via CSS as a fail-safe
if ".quick-menu {" in css_content:
    css_content = css_content.replace(".quick-menu {", ".quick-menu { display: none !important; ", 1)
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Hidden .quick-menu in style.css")

print("Quick menu removal complete!")
