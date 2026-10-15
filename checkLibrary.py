# ==============================================================================
# Library & Package Inspector (checkLibrary.py)
# ==============================================================================
import importlib.util
import importlib.metadata
import sys

def check_library_exists(library_name: str) -> bool:
    """Checks if a Python module/library is installed and prints version and location."""
    spec = importlib.util.find_spec(library_name)
    if spec is not None:
        print(f"✅ The library '{library_name}' exists.")
        
        # Try retrieving origin path
        if spec.origin:
            print(f"   Location: {spec.origin}")
            
        # Try retrieving version metadata
        try:
            version = importlib.metadata.version(library_name)
            print(f"   Installed Version: {version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"   (Built-in standard library module)")
        return True
    else:
        print(f"❌ The library '{library_name}' does not exist.")
        return False

def inspect_common_data_science_stack():
    """Batch-checks standard core and data science libraries."""
    common_libs = ["numpy", "pandas", "matplotlib", "scipy", "requests", "json", "sys", "os"]
    print("\n--- Inspecting Core Stack ---")
    for lib in common_libs:
        spec = importlib.util.find_spec(lib)
        status = "Available" if spec else "Not Installed"
        print(f"{lib:<12} : {status}")

if __name__ == "__main__":
    # Check default interactive or batch inspection
    print("Python Executable:", sys.executable)
    inspect_common_data_science_stack()
    
    print("\n--- Interactive Library Checker ---")
    user_choice = input("Enter a library name to check (or press Enter to skip): ").strip()
    if user_choice:
        check_library_exists(user_choice)
