import importlib.util

def check_library_exists(library_name):
    spec = importlib.util.find_spec(library_name)
    if spec is not None:
        print(f"The library '{library_name}' exists.")
    else:
        print(f"The library '{library_name}' does not exist.")

# Take dynamic input from the user
library_name = input("Enter the library name to check: ")
check_library_exists(library_name)
