# ==============================================================================
# Chapter 11: Typing, Modern Exceptions, Modules & Scopes in Python
# ==============================================================================
# Topics Covered:
# - Modern Type Annotations (Union |, Optional, Literal, Final, Self)
# - Generic Classes & TypeVar
# - Structural Subtyping with Protocol
# - TypedDict for Structured Dictionaries
# - Exception Hierarchy, Custom Exceptions & Exception Chaining (raise from)
# - Python 3.11+ ExceptionGroup & except* syntax
# - The Python Import System & Module Introspection (importlib, sys.modules)
# - Scope & Namespaces (The LEGB Rule: Local, Enclosing, Global, Built-in)

import sys
import importlib
from typing import (
    TypeVar, Generic, Protocol, TypedDict,
    Literal, Final, Callable, Optional, Union
)


# ------------------------------------------------------------------------------
# 1. Modern Type Annotations (PEP 484, PEP 604)
# ------------------------------------------------------------------------------
print("=== 1. Modern Type System ===")

# Final: Cannot be reassigned or overridden
DATABASE_TIMEOUT: Final[int] = 30

# Literal: Value must be one of specific literal constants
Mode = Literal["r", "w", "a"]

def open_file_safely(filename: str, mode: Mode) -> str:
    return f"Opening '{filename}' in '{mode}' mode"

print(open_file_safely("data.txt", "r"))

# Self (Python 3.11+) & Fluent Method Chaining
from typing import Self

class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, fields: str) -> Self:
        self.query += f"SELECT {fields} "
        return self

    def from_table(self, table: str) -> Self:
        self.query += f"FROM {table}"
        return self

qb = QueryBuilder().select("*").from_table("users")
print("Constructed Query via Self-chaining:", qb.query)


# ------------------------------------------------------------------------------
# 2. Generics & TypeVar
# ------------------------------------------------------------------------------
print("\n=== 2. Generics with TypeVar ===")

T = TypeVar("T")  # Represents any arbitrary type

class Stack(Generic[T]):
    """Generic stack container preserving item types."""
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None

str_stack: Stack[str] = Stack()
str_stack.push("First")
str_stack.push("Second")
print("Popped from generic stack:", str_stack.pop())


# ------------------------------------------------------------------------------
# 3. Structural Subtyping with Protocol (Static Duck Typing)
# ------------------------------------------------------------------------------
print("\n=== 3. Structural Subtyping (Protocol) ===")

class Renderable(Protocol):
    """Any class with a render() method satisfies Renderable without inheriting!"""
    def render(self) -> str:
        ...

class Button:
    def render(self) -> str:
        return "<button>Click Me</button>"

class Link:
    def render(self) -> str:
        return "<a href='#'>Link</a>"

def display_component(component: Renderable):
    print("Rendered:", component.render())

display_component(Button())
display_component(Link())


# ------------------------------------------------------------------------------
# 4. TypedDict
# ------------------------------------------------------------------------------
print("\n=== 4. TypedDict ===")

class UserProfile(TypedDict):
    id: int
    name: str
    is_active: bool

user: UserProfile = {"id": 101, "name": "Sarah", "is_active": True}
print(f"TypedDict user: {user['name']} (Active: {user['is_active']})")


# ------------------------------------------------------------------------------
# 5. Exception Chaining & Custom Exceptions
# ------------------------------------------------------------------------------
print("\n=== 5. Exception Chaining (raise from) ===")

class DataProcessingError(Exception):
    """Custom domain-specific application exception."""
    pass

def load_and_parse(raw_value: str) -> int:
    try:
        return int(raw_value)
    except ValueError as original_error:
        # 'raise ... from' explicitly chains the original cause (__cause__)
        raise DataProcessingError(f"Failed to parse '{raw_value}' into integer") from original_error

try:
    load_and_parse("not_a_number")
except DataProcessingError as err:
    print(f"Handled Custom Error: {err}")
    print(f"Original Underlying Cause: {repr(err.__cause__)}")


# ------------------------------------------------------------------------------
# 6. ExceptionGroup & except* (Python 3.11+)
# ------------------------------------------------------------------------------
print("\n=== 6. ExceptionGroup & except* ===")
# Allows raising and handling multiple independent exceptions concurrently.

try:
    raise ExceptionGroup(
        "Multiple task failures occurred concurrently",
        [
            ValueError("Invalid parameter"),
            KeyError("Missing configuration key"),
            ValueError("Value out of acceptable bounds"),
        ]
    )
except* ValueError as eg_val:
    print(f"Caught group of ValueErrors ({len(eg_val.exceptions)} exceptions)")
except* KeyError as eg_key:
    print(f"Caught group of KeyErrors ({len(eg_key.exceptions)} exceptions)")


# ------------------------------------------------------------------------------
# 7. Scope & The LEGB Rule
# ------------------------------------------------------------------------------
print("\n=== 7. The LEGB Scope Rule ===")
# Python searches variables in order:
# L: Local (inside current function)
# E: Enclosing (inside enclosing functions/closures)
# G: Global (module-level)
# B: Built-in (predefined in Python like 'len', 'range', 'int')

global_var = "Global"

def outer_scope():
    enclosing_var = "Enclosing"

    def inner_scope():
        local_var = "Local"
        print(f"Accessing: {local_var} -> {enclosing_var} -> {global_var}")
    inner_scope()

outer_scope()


# ------------------------------------------------------------------------------
# 8. Dynamic Imports & sys.modules
# ------------------------------------------------------------------------------
print("\n=== 8. Dynamic Imports & Module Machinery ===")

# Dynamic import at runtime
math_module = importlib.import_module("math")
print("Dynamically imported math.sqrt(16):", math_module.sqrt(16))

# sys.modules is Python's in-memory cache of all loaded modules
print(f"Total modules currently loaded in sys.modules: {len(sys.modules)}")
print("'math' is in sys.modules:", "math" in sys.modules)
