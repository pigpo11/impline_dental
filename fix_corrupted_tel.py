import os

# Define the broken string and correct replacements
broken_str = "C1-8089-7582</div>"
tel = "031-8089-7582"

# Specific replacements for different structures
replacements = [
    (broken_str, f'{tel}</div>'),
    ('<div class="tel-number" style="font-size: 20px; font-weight: 500; margin-bottom: 12px; color: #222;">\n                            ' + broken_str, 
     f'<div class="tel-number" style="font-size: 20px; font-weight: 500; margin-bottom: 12px; color: #222;">{tel}</div>'),
    ('<div class="label">예약안내</div>\s*<div class="value tel">\s*' + broken_str,
     f'<div class="label">예약안내</div>\n                    <div class="value tel">{tel}</div>')
]

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generic fix for the corrupted tag end
    content = content.replace(broken_str, f'{tel}</div>')
    
    # Fix the missing labels if they were swallowed (if any)
    # Based on about.html view, the label part was NOT swallowed, just the content inside the tag.
    # index.html view: 168: <div class="info-value"> 169: C1-8089-7582</div>
    # about.html view: 238: <div class="info-row"> 239: C1-8089-7582</div>
    
    # Wait, in index.html, the label "예약상담" is at line 167. 
    # Line 169 was the tel-number div.
    
    # I'll just look for the pattern and restore the proper wrappers
    if "index.html" in file_path:
        # Restore index.html tel div
        import re
        content = re.sub(r'<div class="info-value">\s*031-8089-7582</div>', 
                         r'<div class="info-value">\n                            <div class="tel-number" style="font-size: 20px; font-weight: 500; margin-bottom: 12px; color: #222;">031-8089-7582</div>', 
                         content)
    else:
        # Restore subpage tel div
        import re
        content = re.sub(r'<div class="info-row">\s*031-8089-7582</div>', 
                         r'<div class="info-row">\n                    <div class="label">예약안내</div>\n                    <div class="value tel">031-8089-7582</div>', 
                         content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        fix_file(filename)
        print(f"Fixed {filename}")
