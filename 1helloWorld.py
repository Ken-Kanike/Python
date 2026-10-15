# ==============================================================================
# Chapter 0: Welcome to Python & The Execution Model
# ==============================================================================
# In Python, everything starts with simple, readable syntax.
# Python is an interpreted, dynamically typed, multi-paradigm language.

# 1. The Classic First Program
print("Hello World")

# 2. Python's Execution Model:
#    Source Code (.py) -> Bytecode (.pyc) -> Python Virtual Machine (PVM)
import sys
import platform

print("\n--- Python Environment Info ---")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Bytecode magic number: {sys.byteorder} endian")

# 3. Dynamic Typing & Variables
message = "Python is dynamically typed"
print(f"\nMessage: {message} (type: {type(message).__name__})")
message = 42  # Variables can be rebound to different types
print(f"Rebound message: {message} (type: {type(message).__name__})")

# 4. The Standard Entrypoint Pattern (__name__ == '__main__')
# When a Python file is run directly, its __name__ is set to '__main__'.
# When imported as a module into another file, __name__ is the module's name.
def main():
    print("\n--- Execution Context ---")
    print("Code is running directly as the main script!")

if __name__ == "__main__":
    main()