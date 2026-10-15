# ==============================================================================
# Chapter 10: Deep Python: Dunders, Descriptors, __slots__ & Metaclasses
# ==============================================================================
# Topics Covered:
# - Python Object Model (Identity, id(), is vs ==, __dict__, __class__, type())
# - Dunder Methods (Object Lifecycle, Sequence/Container, Numeric Protocols)
# - Descriptors Protocol (__get__, __set__, __delete__)
# - Data Descriptors vs Non-Data Descriptors & Precedence
# - How Functions/Methods Actually Work in Python
# - Attribute Access Machinery (__getattribute__, __getattr__, __setattr__)
# - __slots__ for Memory Optimization
# - Metaclasses: Classes as Objects, Dynamic Class Creation, __init_subclass__

import sys


# ------------------------------------------------------------------------------
# 1. Python Object Model: Everything is an Object
# ------------------------------------------------------------------------------
print("=== 1. Python Object Model ===")

a = 1000
b = 1000
# 'is' tests object identity (memory address in RAM), '==' tests value equality
print(f"a == b (value equal):    {a == b}")
print(f"a is b (same instance?): {a is b}")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")

# Everything has a class and a type:
print("type(a):        ", type(a))
print("type(type):     ", type(type))  # type is an instance of type itself!
print("isinstance(5, object):", isinstance(5, object))


# ------------------------------------------------------------------------------
# 2. Object Lifecycle: __new__ vs __init__
# ------------------------------------------------------------------------------
print("\n=== 2. Object Lifecycle: __new__ vs __init__ ===")
# __new__: Allocates the object in memory and returns it (acts as actual creator).
# __init__: Initializes attributes on the already-created instance.

class Singleton:
    """Enforces a single instance using __new__."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the single instance in memory via __new__")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: int):
        self.value = value

s1 = Singleton(10)
s2 = Singleton(20)
print(f"s1 is s2: {s1 is s2} (Both point to the same memory object, value: {s1.value})")


# ------------------------------------------------------------------------------
# 3. Container & Sequence Dunders (__getitem__, __setitem__, __len__)
# ------------------------------------------------------------------------------
print("\n=== 3. Custom Container Protocol ===")

class CustomList:
    """A custom container implementing sequence protocols."""
    def __init__(self, elements=None):
        self._data = list(elements) if elements else []

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __contains__(self, item) -> bool:
        return item in self._data

    def __repr__(self) -> str:
        return f"CustomList({self._data})"

cl = CustomList([10, 20, 30, 40])
print("Custom container:", cl)
print("cl[1]:          ", cl[1])
print("len(cl):        ", len(cl))
print("30 in cl:       ", 30 in cl)
cl[1] = 99
print("After cl[1]=99: ", cl)


# ------------------------------------------------------------------------------
# 4. Descriptors: Data vs Non-Data Descriptors
# ------------------------------------------------------------------------------
print("\n=== 4. Descriptors Protocol ===")
# A descriptor is an attribute object that controls access via __get__, __set__, or __delete__.
# - Data Descriptor: Implements __set__ and/or __delete__. Has precedence over instance __dict__.
# - Non-Data Descriptor: Implements only __get__ (e.g. regular methods).

class PositiveNumber:
    """A data descriptor validating that assigned values are positive numbers."""
    def __set_name__(self, owner, name):
        # Automatically called in Python 3.6+ to know the attribute name on the class
        self.private_name = f"_{name}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.private_name, 0.0)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Value for '{self.private_name[1:]}' must be a positive number! Got: {value}")
        setattr(instance, self.private_name, value)

class Product:
    price = PositiveNumber()   # Descriptor instance
    weight = PositiveNumber()  # Descriptor instance

    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

prod = Product("Coffee Beans", 15.50, 500)
print(f"Product: {prod.name}, Price: ${prod.price}, Weight: {prod.weight}g")
try:
    prod.price = -10  # Raises ValueError thanks to the descriptor!
except ValueError as e:
    print("Descriptor caught invalid assignment:", e)


# ------------------------------------------------------------------------------
# 5. Attribute Access Machinery (__getattr__ vs __getattribute__)
# ------------------------------------------------------------------------------
print("\n=== 5. Attribute Access Machinery ===")
# __getattribute__: Called unconditionally for EVERY attribute access.
# __getattr__: Fallback called ONLY when an attribute is NOT found in __dict__ or class.

class DynamicFallback:
    def __init__(self):
        self.known_attr = "I exist in instance __dict__"

    def __getattr__(self, name):
        """Fallback for undefined attributes."""
        return f"Dynamically handled attribute: '{name}'"

obj = DynamicFallback()
print(obj.known_attr)
print(obj.non_existent_field)  # Triggers __getattr__ fallback seamlessly


# ------------------------------------------------------------------------------
# 6. Memory Optimization with __slots__
# ------------------------------------------------------------------------------
print("\n=== 6. Memory Optimization with __slots__ ===")
# Normal Python instances carry a __dict__ for dynamic attributes, which adds memory overhead.
# __slots__ reserves fixed space for specified attributes and eliminates the __dict__.

class StandardPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ('x', 'y')  # No __dict__ created!

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

p_std = StandardPoint(1.0, 2.0)
p_slot = SlottedPoint(1.0, 2.0)

print("StandardPoint has __dict__:", hasattr(p_std, '__dict__'))
print("SlottedPoint has __dict__: ", hasattr(p_slot, '__dict__'))
print(f"StandardPoint memory: {sys.getsizeof(p_std)} bytes + dict({sys.getsizeof(p_std.__dict__)} bytes)")
print(f"SlottedPoint memory:  {sys.getsizeof(p_slot)} bytes (Massive memory saving at scale!)")


# ------------------------------------------------------------------------------
# 7. Metaclasses & __init_subclass__
# ------------------------------------------------------------------------------
print("\n=== 7. Metaclasses: The Classes of Classes ===")
# In Python, classes are themselves instances of metaclasses. The default metaclass is 'type'.

# Dynamic class creation using type(name, bases, dict):
DynamicPerson = type("DynamicPerson", (object,), {
    "species": "Homo sapiens",
    "say_hi": lambda self: f"Hello from {self.species}"
})
dp = DynamicPerson()
print(f"Dynamically created class: {DynamicPerson.__name__}, Call: {dp.say_hi()}")


# Custom Metaclass: Enforces that all class attribute names must be lowercase
class StrictMeta(type):
    def __new__(mcs, name, bases, namespace):
        for attr_name in namespace:
            if not attr_name.startswith("__") and not attr_name.islower():
                raise TypeError(f"Attribute '{attr_name}' in class '{name}' must be lowercase!")
        return super().__new__(mcs, name, bases, namespace)

class ValidClass(metaclass=StrictMeta):
    valid_attribute = "ok"

print("Class ValidClass created successfully under StrictMeta.")


# Modern Alternative: __init_subclass__ (PEP 487)
# Cleaner and preferred over complex metaclasses for plugin registration
class PluginBase:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registry.append(cls)
        print(f"Auto-registered plugin subclass: {cls.__name__}")

class ImagePlugin(PluginBase):
    pass

class AudioPlugin(PluginBase):
    pass

print("PluginBase registry:", [p.__name__ for p in PluginBase.registry])
