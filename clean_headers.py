import os
import re

def clean_header_tags():
    # Remove inline styles from <header id="main-header" ...>
    pattern = re.compile(r'<header id="main-header".*?>', re.DOTALL)
    new_header_tag = '<header id="main-header">'
    
    files_updated = 0
    for file in os.listdir('.'):
        if file.endswith('.html'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                new_content = pattern.sub(new_header_tag, content)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                print(f"Cleaned header tag in {file}")

    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    clean_header_tags()
