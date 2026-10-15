# ==============================================================================
# Comprehensive Guide to Python Strings (YtoCodes)
# ==============================================================================
print("String")

# 1. String Creation & Immutability
# Strings are immutable sequences of Unicode characters in Python.
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple quotes for
multi-line strings'''

original = "Python"
# original[0] = 'J' # TypeError: 'str' object does not support item assignment
new_str = "J" + original[1:]  # Create a new string instead
print(f"Original: {original}, Modified new: {new_str}")

# 2. String Indexing & Slicing
# Syntax: string[start:stop:step]
text = "Mastering Python"
print("\n--- Slicing Tricks ---")
print(f"First 4 chars:        {text[:4]}")
print(f"From index 10 to end: {text[10:]}")
print(f"Every 2nd char:       {text[::2]}")
print(f"Reverse a string:     {text[::-1]}")  # Classic python idiom
print(f"Negative indexing:    {text[-6:]}")

# 3. Essential String Methods
print("\n--- Essential String Methods ---")
sample = "  hello world, welcome to python programming!  "
print(f"strip():       '{sample.strip()}'")
print(f"upper():       '{sample.upper().strip()}'")
print(f"title():       '{sample.title().strip()}'")
print(f"capitalize():  '{sample.strip().capitalize()}'")
print(f"replace():     '{sample.strip().replace('python', 'advanced Python')}'")
print(f"count('o'):    {sample.count('o')}")
print(f"startswith:    {sample.strip().startswith('hello')}")
print(f"endswith:      {sample.strip().endswith('!')}")
print(f"find('world'): {sample.find('world')}")

# 4. Splitting and Joining
words = sample.strip().split()
print("\n--- Splitting & Joining ---")
print(f"split():       {words}")
joined = " - ".join(words)
print(f"join():        {joined}")

# 5. String Validation Methods
print("\n--- Validation Methods ---")
print(f"'12345'.isdigit():   {'12345'.isdigit()}")
print(f"'Python3'.isalnum(): {'Python3'.isalnum()}")
print(f"'hello'.isalpha():   {'hello'.isalpha()}")
print(f"'   '.isspace():     {'   '.isspace()}")

# 6. Modern String Formatting
name = "Alex"
score = 98.6754
count = 42

print("\n--- Modern Formatting (f-strings) ---")
# Basic interpolation
print(f"Student: {name}, Score: {score}")
# Decimal precision formatting
print(f"Formatted score: {score:.2f}")
# Padding and alignment
print(f"Padded number:   {count:05d}")       # 00042
print(f"Left aligned:    {name:<10}|")
print(f"Right aligned:   {name:>10}|")
print(f"Center aligned:  {name:^10}|")
# Self-documenting expressions (Python 3.8+)
print(f"Debug expression: {name=}, {score=}")

# 7. String Interning & Memory Optimization
# Small strings and identifiers are interned by CPython to save memory.
import sys
a = "python_identifier"
b = "python_identifier"
print(f"\nString Interning (a is b): {a is b}")  # True due to interning
explicit_a = sys.intern("dynamically created string with spaces")
explicit_b = sys.intern("dynamically created string with spaces")
print(f"Explicit sys.intern check: {explicit_a is explicit_b}")

# 8. Unicode & Encoding (Text vs Bytes)
unicode_text = "Python (Unicode \\u03b1\\u03b2\\u03b3: alpha beta gamma)"
encoded_bytes = unicode_text.encode('utf-8')
decoded_text = encoded_bytes.decode('utf-8')
print("\n--- Unicode & Byte Encoding ---")
print(f"Text:    {unicode_text} (type: {type(unicode_text).__name__})")
print(f"Bytes:   {encoded_bytes} (type: {type(encoded_bytes).__name__})")
print(f"Decoded: {decoded_text}")