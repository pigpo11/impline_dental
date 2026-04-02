import os
import glob
import re

# Precise replacement of ONLY the quick-menu block
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for exactly where it is.
    # It usually starts with <!-- Floating Quick Menu -->\n    <div class="quick-menu">
    # and ends with 인스타그램</span>\n        </a>\n    </div>
    
    # Let's try to match from <div class="quick-menu"> until the </div> that closes it.
    # We'll use a slightly safer non-greedy match and verify it has the expected content.
    
    pattern = re.compile(r'<!-- Floating Quick Menu -->\s*<div class="quick-menu">.*?</div>\s+</div>', re.DOTALL)
    
    # If the comment is missing:
    if not pattern.search(content):
        pattern = re.compile(r'<div class="quick-menu">.*?</div>\s+</div>', re.DOTALL)

    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Properly removed quick-menu from {filepath}")
    else:
        print(f"FAILED TO FIND quick-menu in {filepath}")

# Still hide in CSS as a backup
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()
if ".quick-menu {" in css and "display: none" not in css:
    css = css.replace(".quick-menu {", ".quick-menu { display: none !important; ", 1)
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Hidden in style.css")
