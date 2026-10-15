# ==============================================================================
# Comprehensive File Handling & I/O in Python
# ==============================================================================

# open syntax
# filePointer = open('filename.type', 'mode', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)

# file modes:
# r = read -- by default
# w = write (if file exists, deletes all data + overwrites; create if not exist)
# a = appends code if file exists 
# x = exclusive (operation fails if a file exists)
# b = binary mode
# rb = read binary
# wb = write binary
# r+ = read + write
# w+ = write + read
# a+ = appending + read/write

import os
import io
import json
import csv
from pathlib import Path

# Ensure target directory exists for demonstration
os.makedirs("File Handling", exist_ok=True)
demo_path = os.path.join("File Handling", "demo1.txt")

# 1. Writing to a file using the 'with' statement (Context Manager - Auto Close)
with open(demo_path, "w", encoding="utf-8") as f:
    f.write("Line 1: Welcome to Python File Handling\n")
    f.write("Line 2: Python makes file management simple and safe.\n")
    f.writelines(["Line 3: First extra line\n", "Line 4: Second extra line\n"])

print("File created and written successfully.")

# 2. Reading files safely: try - except - finally vs with
print("\n--- Reading Files (Methods) ---")
# Using with block
with open(demo_path, "r", encoding="utf-8") as f:
    # read(n): reads n characters or whole file if omitted
    whole_content = f.read()
    print("Full file content:\n", whole_content)

with open(demo_path, "r", encoding="utf-8") as f:
    # readline(): reads one line at a time
    print("First line:", f.readline().strip())
    # readlines(): returns list of all lines
    remaining_lines = f.readlines()
    print("Remaining lines as list:", [l.strip() for l in remaining_lines])

# 3. File Object Attributes & Capabilities
with open(demo_path, "r", encoding="utf-8") as f:
    print("\n--- File Attributes ---")
    print("File Name:    ", f.name)
    print("File Mode:    ", f.mode)
    print("File Encoding:", f.encoding)
    print("Is Readable:  ", f.readable())
    print("Is Writable:  ", f.writable())
print("Is Closed:    ", f.closed)  # True outside 'with' block

# 4. File Pointers: tell() and seek()
print("\n--- File Pointer Control (tell & seek) ---")
with open(demo_path, "r", encoding="utf-8") as f:
    print("Pointer at start:", f.tell())  # 0
    sample_text = f.read(10)
    print(f"Read 10 chars: '{sample_text}', Pointer now at:", f.tell())
    
    # seek(offset, whence): 0 = start, 1 = current, 2 = end
    f.seek(0)  # Reset pointer to beginning of file
    print("Pointer reset to start via seek(0):", f.tell())
    print("Re-reading first 5 chars:", f.read(5))

# 5. Binary File I/O (rb, wb)
binary_file_path = os.path.join("File Handling", "binary_sample.bin")
binary_data = b"\x00\x01\x02\x03\x04\x05PythonBytes"

with open(binary_file_path, "wb") as f_bin:
    f_bin.write(binary_data)

with open(binary_file_path, "rb") as f_bin:
    read_bytes = f_bin.read()
    print("\n--- Binary Mode ---")
    print("Written bytes:", read_bytes)

# 6. In-Memory Streams: io.StringIO and io.BytesIO
print("\n--- In-Memory Streams (io module) ---")
# StringIO: treat in-memory string as a file object
string_stream = io.StringIO()
string_stream.write("In-memory text stream buffer.\nLine 2.")
string_stream.seek(0)
print("StringIO content:\n", string_stream.read())

# BytesIO: treat in-memory bytes as a binary file
bytes_stream = io.BytesIO()
bytes_stream.write(b"Binary in-memory stream")
bytes_stream.seek(0)
print("BytesIO content: ", bytes_stream.read())

# 7. Modern Path Manipulation using pathlib (Python 3.4+)
print("\n--- Modern pathlib.Path Usage ---")
p = Path("File Handling") / "demo1.txt"
print("Path exists:      ", p.exists())
print("Is file:          ", p.is_file())
print("File suffix (ext):", p.suffix)
print("File stem (name): ", p.stem)
print("Parent directory: ", p.parent)
# Direct convenience reading & writing without explicit open():
print("Path.read_text() shortcut:\n", p.read_text(encoding="utf-8")[:38], "...")

# 8. Structured Data: JSON & CSV
print("\n--- Structured File Formats (JSON & CSV) ---")
# JSON
json_path = os.path.join("File Handling", "demo_config.json")
config_data = {"version": "3.12", "features": ["async", "type_hints", "match_case"], "enabled": True}
with open(json_path, "w", encoding="utf-8") as jf:
    json.dump(config_data, jf, indent=4)

with open(json_path, "r", encoding="utf-8") as jf:
    loaded_config = json.load(jf)
    print("Loaded JSON configuration:", loaded_config)

# CSV
csv_path = os.path.join("File Handling", "demo_data.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as cf:
    writer = csv.writer(cf)
    writer.writerow(["ID", "Item", "Quantity"])
    writer.writerow([1, "Apples", 15])
    writer.writerow([2, "Oranges", 25])

with open(csv_path, "r", encoding="utf-8") as cf:
    reader = csv.DictReader(cf)
    print("Loaded CSV rows:")
    for row in reader:
        print("  ", dict(row))
