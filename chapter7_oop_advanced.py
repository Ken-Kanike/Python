# ==============================================================================
# Chapter 7: Advanced Object-Oriented Programming (OOP) in Python
# ==============================================================================
# Topics Covered:
# - Class vs Instance Attributes
# - Instance Methods vs @classmethod vs @staticmethod
# - Properties (@property, getters, setters, deleters)
# - Abstract Base Classes (abc, ABC, @abstractmethod)
# - Multiple Inheritance, Method Resolution Order (MRO) & C3 Linearization
# - Cooperative Inheritance with super()
# - Mixin Design Pattern & Composition vs Inheritance
# - Essential Dunder (Magic) Methods for OOP

from abc import ABC, abstractmethod


# ------------------------------------------------------------------------------
# 1. Class vs Instance Attributes
# ------------------------------------------------------------------------------
print("=== 1. Class vs Instance Attributes ===")

class BankAccount:
    bank_name = "Global Python Bank"  # Class attribute (shared across all instances)
    interest_rate = 0.04              # 4% interest
    total_accounts = 0

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner            # Instance attribute (unique to each instance)
        self.balance = balance
        BankAccount.total_accounts += 1

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

print(f"{acc1.owner} at {acc1.bank_name}, Balance: ${acc1.balance}")
print(f"Total accounts opened: {BankAccount.total_accounts}")


# ------------------------------------------------------------------------------
# 2. Instance Methods, Class Methods (@classmethod), and Static Methods (@staticmethod)
# ------------------------------------------------------------------------------
print("\n=== 2. Method Types ===")

class DateFormatter:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    # Instance method: Operates on a specific instance (has 'self')
    def format_iso(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    # Class method: Operates on the class itself (has 'cls'), acts as alternative constructor
    @classmethod
    def from_string(cls, date_str: str):
        """Creates a DateFormatter instance from 'YYYY-MM-DD'."""
        year, month, day = map(int, date_str.split("-"))
        return cls(day, month, year)

    # Static method: Utility function without access to instance or class state
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

d1 = DateFormatter(15, 8, 2024)
d2 = DateFormatter.from_string("2026-10-08")

print("Instance method: ", d1.format_iso())
print("From classmethod: ", d2.format_iso())
print("Static method:    Is 2024 a leap year?", DateFormatter.is_leap_year(2024))


# ------------------------------------------------------------------------------
# 3. Properties (@property, Getter, Setter, Deleter)
# ------------------------------------------------------------------------------
print("\n=== 3. Properties & Encapsulation ===")

class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = celsius  # Protected attribute by convention

    @property
    def celsius(self) -> float:
        """Getter for celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        """Setter with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero (-273.15°C) is impossible!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Computed property on-the-fly."""
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5 / 9

temp = Temperature(25)
print(f"25°C in Fahrenheit: {temp.fahrenheit}°F")
temp.fahrenheit = 212
print(f"212°F set -> Celsius: {temp.celsius}°C")


# ------------------------------------------------------------------------------
# 4. Abstract Base Classes (ABC)
# ------------------------------------------------------------------------------
print("\n=== 4. Abstract Base Classes ===")

class Shape(ABC):
    """Abstract Base Class enforcing an interface on subclasses."""

    @abstractmethod
    def area(self) -> float:
        """Subclasses must implement area()."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Subclasses must implement perimeter()."""
        pass

    # Concrete method in an ABC
    def describe(self) -> str:
        return f"{self.__class__.__name__} with area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

c = Circle(5)
print(c.describe(), f", perimeter={c.perimeter():.2f}")


# ------------------------------------------------------------------------------
# 5. Multiple Inheritance, MRO & C3 Linearization
# ------------------------------------------------------------------------------
print("\n=== 5. Multiple Inheritance & Method Resolution Order (MRO) ===")

# In Python, multiple inheritance is resolved using the C3 Linearization algorithm.
class BaseA:
    def action(self):
        print("BaseA action")

class BaseB:
    def action(self):
        print("BaseB action")

class Derived(BaseA, BaseB):
    pass

d = Derived()
d.action()  # Calls BaseA.action because BaseA comes first in MRO
print("MRO of Derived:", [cls.__name__ for cls in Derived.__mro__])


# Cooperative Multiple Inheritance with super()
class Animal:
    def __init__(self, name: str, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Swimmer(Animal):
    def __init__(self, swim_speed: int = 10, **kwargs):
        self.swim_speed = swim_speed
        super().__init__(**kwargs)

class Flyer(Animal):
    def __init__(self, fly_altitude: int = 500, **kwargs):
        self.fly_altitude = fly_altitude
        super().__init__(**kwargs)

class Duck(Swimmer, Flyer):
    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, **kwargs)

duck = Duck(name="Donald", swim_speed=15, fly_altitude=300)
print(f"Duck '{duck.name}': speed={duck.swim_speed}, altitude={duck.fly_altitude}")
print("Duck MRO:", [cls.__name__ for cls in Duck.__mro__])


# ------------------------------------------------------------------------------
# 6. Mixin Design Pattern
# ------------------------------------------------------------------------------
print("\n=== 6. Mixin Pattern ===")

import json

class JSONSerializableMixin:
    """A mixin providing JSON export to any class without altering its inheritance tree."""
    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

class User(JSONSerializableMixin):
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

user = User("code_master", "user@example.com")
print("User via Mixin JSON:", user.to_json())


# ------------------------------------------------------------------------------
# 7. Core Dunder Methods for Objects (__repr__, __str__, __eq__, __hash__)
# ------------------------------------------------------------------------------
print("\n=== 7. Dunder Methods for Data Objects ===")

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # __str__: User-friendly string representation (used by print(), str())
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # __repr__: Unambiguous developer representation (used in repl, debugging)
    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    # __eq__: Custom equality logic
    def __eq__(self, other) -> bool:
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    # __hash__: Enables usage as dictionary keys and set elements (if immutable)
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    # Operator overloading: __add__, __sub__, __mul__
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2
print(f"Vector Addition: {v1} + {v2} = {v3}")
print("Vector repr:    ", repr(v3))
print("Equality check:  v1 == Vector2D(3, 4)?", v1 == Vector2D(3, 4))
print("Can be in a set: ", {v1, v2, v3})
