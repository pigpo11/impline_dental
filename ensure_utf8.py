import os

def convert_to_utf8(filename):
    try:
        # Try reading as UTF-8
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return # Already UTF-8
    except UnicodeDecodeError:
        # Try reading as CP949 (Korean Windows default)
        try:
            with open(filename, 'r', encoding='cp949') as f:
                content = f.read()
            # Rewrite as UTF-8
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Converted {filename} from CP949 to UTF-8")
        except UnicodeDecodeError:
            try:
                with open(filename, 'r', encoding='utf-16') as f:
                    content = f.read()
                # Rewrite as UTF-8
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Converted {filename} from UTF-16 to UTF-8")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

for file in os.listdir('.'):
    if file.endswith('.html'):
        convert_to_utf8(file)
