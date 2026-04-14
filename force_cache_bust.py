import os
import re
import time

def force_cache_bust():
    # Update style.css?v=... to a timestamp-based version
    v_num = int(time.time())
    pattern = re.compile(r'href="style\.css\?v=\d+"')
    new_href = f'href="style.css?v={v_num}"'
    
    files_updated = 0
    for file in os.listdir('.'):
        if file.endswith('.html'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                new_content = pattern.sub(new_href, content)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f"Updated CSS version in {file} to {v_num}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    force_cache_bust()
