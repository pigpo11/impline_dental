import re

def sync_headers():
    # Read working header from about.html
    with open('about.html', 'r', encoding='utf-8') as f:
        about_content = f.read()
    
    # Extract header part
    header_pattern = re.compile(r'(<header id="main-header">.*?</header>)', re.DOTALL)
    match = header_pattern.search(about_content)
    if not match:
        print("Could not find header in about.html")
        return
    
    working_header = match.group(1)
    
    # Read index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Replace index.html header with working header
    new_index_content = header_pattern.sub(working_header, index_content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_index_content)
    
    print("Synced index.html header with about.html")

if __name__ == "__main__":
    sync_headers()
