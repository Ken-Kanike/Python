# ==============================================================================
# Comprehensive Guide to Python Functions (YtoCodes)
# ==============================================================================

# 1. Simple function definition and invocation
def simple_functions():
    print("Hello World!\n")

simple_functions()  # function call


# 2. Return values
def add_interactive():
    a = 10
    b = 20
    return a + b

print("Sum of two nums =", add_interactive())


# 3. Positional vs Keyword Arguments
def add(a, b): 
    print(f"\na = {a}, b = {b}")
    print("Sum of two nums =", a + b)

add(10, 20)           # Positional
add(b=10, a=20)       # Keyword


# 4. Function Argument Types:
#    1) No Arg No Return
#    2) With Arg No Return
#    3) No Arg With Return
#    4) With Arg With Return


# 5. Default Arguments
# Rule: Non-default arguments must precede default arguments.
def sum3(a, b=5, c=5):
    print(f"sum3 result: {a + b + c}")

sum3(5)
sum3(5, 10)
sum3(2, 2, 2)


# 6. Break & Continue inside loops
print("\nBreak Example : print 1-5")
i = 1
while i <= 5:
    if i < 4:
        print(i)
        i += 1
    else:
        print("Break at", i)
        i += 1
        break
    
print("\nContinue Example : print 1-5")
i = 1
while i <= 5:
    if i == 4:
        print(i)
        i += 1
    else:
        print("Continue at", i)
        i += 1
        continue


# ==============================================================================
# Advanced Function Topics (Completed Data)
# ==============================================================================

# 7. Variable-Length Arguments: *args and **kwargs
print("\n--- *args and **kwargs ---")
def flexible_function(*args, **kwargs):
    """Accepts any number of positional (*args) and keyword (**kwargs) arguments."""
    print("Positional arguments (as tuple):", args)
    print("Keyword arguments (as dict):", kwargs)

flexible_function(1, 2, 3, "apple", name="Alice", role="Admin")

# Argument Unpacking
nums = [10, 20, 30]
metadata = {"sep": " -> ", "end": "\n"}
print(*nums, **metadata)


# 8. Special Parameter Markers: Positional-Only (/) and Keyword-Only (*)
print("\n--- Positional-Only (/) & Keyword-Only (*) Parameters ---")
# Parameters before '/' CANNOT be passed as keyword arguments.
# Parameters after '*' MUST be passed as keyword arguments.
def advanced_signature(pos_only, /, standard, *, kw_only="default"):
    print(f"pos_only: {pos_only}, standard: {standard}, kw_only: {kw_only}")

# Valid calls:
advanced_signature("must_be_positional", standard="can_be_keyword", kw_only="explicit_keyword")
advanced_signature("must_be_positional", "can_be_positional", kw_only="explicit_keyword")
# advanced_signature(pos_only="error", standard=2, kw_only=3) # Raises TypeError!


# 9. The Mutable Default Argument Gotcha & Idiomatic Fix
print("\n--- Mutable Default Argument Trap ---")
# WRONG: def bad_append(item, lst=[]): lst.append(item); return lst
# The default list is evaluated ONCE when the function is defined, not per call!
def safe_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Call 1:", safe_append("a"))
print("Call 2:", safe_append("b"))  # Stays separate, clean!


# 10. Closures and Scope (LEGB Rule: Local -> Enclosing -> Global -> Built-in)
print("\n--- Closures & nonlocal Keyword ---")
def make_multiplier(factor):
    """Enclosing scope holding 'factor' (free variable)."""
    def multiplier(number):
        # Accesses 'factor' from enclosing scope
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print("Double of 5:", double(5))
print("Triple of 5:", triple(5))

# Using nonlocal to modify outer scope variables:
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print("Counter call 1:", c())
print("Counter call 2:", c())
print("Counter call 3:", c())


# 11. First-Class Functions & Higher-Order Functions
print("\n--- Higher-Order Functions ---")
def apply_operation(func, values):
    return [func(x) for x in values]

squared = apply_operation(lambda x: x ** 2, [1, 2, 3, 4, 5])
print("Squared with lambda:", squared)


# 12. Function Attributes & Introspection
def documented_calc(x: int, y: int) -> int:
    """Returns the sum of two integers with metadata."""
    return x + y

documented_calc.call_count = 1  # Functions are objects; can have custom attributes!
print("\n--- Function Metadata ---")
print("Docstring:   ", documented_calc.__doc__)
print("Annotations: ", documented_calc.__annotations__)
print("Custom attr: ", documented_calc.call_count)