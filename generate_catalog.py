import os
import json
import re

EXCLUDE_DIRS = {'.git', '.vs', '__pycache__', 'Python_backup_pre_clean', '.system_generated'}
EXCLUDE_FILES = {'generate_catalog.py', 'code_catalog.json', 'code_catalog.js', 'package.json', 'package-lock.json'}

def get_category(filepath: str) -> str:
    fp = filepath.replace('\\', '/')
    if any(fp.startswith(p) for p in ['chapter7_', 'chapter8_', 'chapter9_', 'chapter10_', 'chapter11_', 'chapter12_', 'chapter13_', 'chapter14_']):
        return "Advanced Masterclasses"
    elif any(fp.startswith(p) for p in ['1helloWorld', '2Operators', 'chapter1', 'chapter2', 'chapter3', 'chapter4', 'chapter5', 'chapter6', 'YtoCodes']):
        return "Core Fundamentals"
    elif any(fp.startswith(p) for p in ['NumpyDemo', 'PandasDemo', 'MatplotlibDemo', 'File Handling', 'MyMathPackage', 'PyMySQL']):
        return "Data Science & Packages"
    elif any(fp.startswith(p) for p in ['Practcals', 'manual pr', 'Ct1Qb', 'Ct2Qb']):
        return "Lab Practicals & Exams"
    elif any(fp.startswith(p) for p in ['PythonProjects', 'TrackFlexBot', 'E_MP', 'chatBot', 'chatbotFlask', 'giminiPython', 'turtleDemo']):
        return "Projects & Applications"
    return "Other Code"

def build_catalog():
    catalog = []
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for root, dirs, files in os.walk(base_dir):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        
        for file in sorted(files):
            if file in EXCLUDE_FILES or file.startswith('.'):
                continue
            
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.py', '.html', '.css', '.js', '.txt', '.json', '.md']:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir).replace('\\', '/')
                
                # Skip large files or certain text files if not code
                if file in ['code_catalog.json', 'data.json'] or 'backup' in rel_path.lower():
                    continue

                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Sanitize any accidental absolute system paths
                    content = re.sub(r'[a-zA-Z]:[/\\]Users[/\\][a-zA-Z0-9_-]+[/\\]Desktop[/\\]coding[/\\]Python[/\\]?', '', content, flags=re.I)
                    content = re.sub(r'[a-zA-Z]:[/\\]Users[/\\][a-zA-Z0-9_-]+', '~', content, flags=re.I)
                    
                    catalog.append({
                        "path": rel_path,
                        "name": file,
                        "category": get_category(rel_path),
                        "language": "python" if ext == '.py' else ext[1:],
                        "lines": len(content.splitlines()),
                        "content": content
                    })
                except Exception as e:
                    print(f"Error reading {rel_path}: {e}")

    output_path = os.path.join(base_dir, "code_catalog.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)

    js_output_path = os.path.join(base_dir, "code_catalog.js")
    with open(js_output_path, "w", encoding="utf-8") as f:
        f.write("window.CODE_CATALOG = " + json.dumps(catalog, indent=2) + ";\n")

    print(f"Successfully generated catalog with {len(catalog)} files -> {output_path} and {js_output_path}")

if __name__ == "__main__":
    build_catalog()
