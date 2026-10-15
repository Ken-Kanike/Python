# ==============================================================================
# Chapter 9: Decorators & Context Managers in Python
# ==============================================================================
# Topics Covered:
# - Function Decorator Mechanics
# - Preserving Metadata with functools.wraps
# - Decorators with Arguments (Decorator Factories)
# - Multiple Stacked Decorators & Execution Order
# - Class Decorators & Stateful Decorators
# - Callable Classes as Decorators
# - Context Managers: The Context Management Protocol (__enter__, __exit__)
# - Handling Exceptions inside __exit__
# - The contextlib Standard Library:
#   - @contextmanager generator decorator
#   - contextlib.suppress
#   - contextlib.closing
#   - contextlib.ExitStack for dynamic resource management

import functools
import time
import contextlib


# ------------------------------------------------------------------------------
# 1. Basic Function Decorator & functools.wraps
# ------------------------------------------------------------------------------
print("=== 1. Basic Function Decorator ===")

def timer_decorator(func):
    """Measures execution time of a function."""
    @functools.wraps(func)  # Critical: Copies __name__, __doc__, and __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"[{func.__name__}] executed in {duration * 1000:.3f} ms")
        return result
    return wrapper

@timer_decorator
def compute_sum(n: int) -> int:
    """Computes sum of numbers up to n."""
    return sum(range(n))

val = compute_sum(100_000)
print(f"Result: {val}, Function name preserved: {compute_sum.__name__}")
print(f"Docstring preserved: {compute_sum.__doc__}")


# ------------------------------------------------------------------------------
# 2. Decorators with Arguments (Decorator Factory)
# ------------------------------------------------------------------------------
print("\n=== 2. Decorators with Arguments ===")

def repeat(num_times: int):
    """Decorator factory accepting configuration arguments."""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name: str):
    return f"Hello, {name}!"

print("Repeated 3 times:", greet("Alice"))


# ------------------------------------------------------------------------------
# 3. Multiple Decorators & Execution Order
# ------------------------------------------------------------------------------
print("\n=== 3. Multiple Stacked Decorators ===")
# Decorators are evaluated bottom-up when applied:
# @dec1
# @dec2
# def func(): ...
# is equivalent to func = dec1(dec2(func))

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def format_text(text: str) -> str:
    return text

print("Stacked formatting:", format_text("Python Decorators"))


# ------------------------------------------------------------------------------
# 4. Stateful Decorator using a Callable Class
# ------------------------------------------------------------------------------
print("\n=== 4. Callable Class Decorator (Call Counter) ===")

class CountCalls:
    """Class decorator tracking how many times a function has been invoked."""
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call #{self.num_calls} to '{self.func.__name__}'")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    return "Hi there!"

say_hello()
say_hello()
print(f"Total calls recorded: {say_hello.num_calls}")


# ------------------------------------------------------------------------------
# 5. Class Decorators (Decorating Classes Themselves)
# ------------------------------------------------------------------------------
print("\n=== 5. Class Decorator ===")

def add_greeting(cls):
    """Adds a standard greeting method to any class."""
    cls.welcome = lambda self: f"Welcome to {cls.__name__}!"
    return cls

@add_greeting
class Dashboard:
    pass

dash = Dashboard()
print("Method added via class decorator:", dash.welcome())


# ------------------------------------------------------------------------------
# 6. Context Management Protocol (__enter__ and __exit__)
# ------------------------------------------------------------------------------
print("\n=== 6. Context Management Protocol ===")

class ManagedResource:
    """Demonstrates __enter__ and __exit__ with exception suppression."""
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"[{self.name}] Resource acquired.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[{self.name}] Resource released.")
        if exc_type is not None:
            print(f"[{self.name}] Caught exception: {exc_val}")
            # Returning True SUPPRESSES the exception so it doesn't propagate!
            return True

with ManagedResource("DatabaseConnection"):
    print("Performing queries safely...")
    raise RuntimeError("Simulated query timeout!")  # Suppressed by __exit__

print("Execution continued cleanly after suppressed error!")


# ------------------------------------------------------------------------------
# 7. contextlib: @contextmanager Generator Decorator
# ------------------------------------------------------------------------------
print("\n=== 7. contextlib Utilities ===")

@contextlib.contextmanager
def temporary_flag(obj, attr_name, temp_value):
    """Context manager temporarily overriding an attribute and restoring it."""
    old_value = getattr(obj, attr_name)
    setattr(obj, attr_name, temp_value)
    try:
        yield obj
    finally:
        setattr(obj, attr_name, old_value)

class AppConfig:
    debug_mode = False

cfg = AppConfig()
print("Initial debug_mode:", cfg.debug_mode)

with temporary_flag(cfg, "debug_mode", True):
    print("Inside context debug_mode:", cfg.debug_mode)

print("Restored debug_mode:", cfg.debug_mode)


# ------------------------------------------------------------------------------
# 8. contextlib.suppress and contextlib.ExitStack
# ------------------------------------------------------------------------------
print("\n=== 8. contextlib.suppress & ExitStack ===")

# contextlib.suppress: Cleaner than empty try-except blocks
import os

with contextlib.suppress(FileNotFoundError):
    os.remove("non_existent_temporary_file.xyz")
    print("This will not be printed if file doesn't exist.")

print("contextlib.suppress successfully bypassed FileNotFoundError!")

# contextlib.ExitStack: Dynamically manages an arbitrary number of contexts
with contextlib.ExitStack() as stack:
    # Acquire resources conditionally or in loops
    res1 = stack.enter_context(ManagedResource("DynamicResource1"))
    res2 = stack.enter_context(ManagedResource("DynamicResource2"))
    print("Working with multiple dynamically managed resources...")
    # Both resources are guaranteed to close cleanly upon leaving the block
