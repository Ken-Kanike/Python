# ==============================================================================
# Chapter 12: Standard Library Mastery: Functional, itertools & Serialization
# ==============================================================================
# Topics Covered:
# - Functional Programming: map(), filter(), reduce(), zip(), sorted(key=...)
# - The operator Module: itemgetter, attrgetter
# - The functools Module: lru_cache, partial, singledispatch, total_ordering
# - The itertools Module: chain, groupby, islice, pairwise, permutations, combinations
# - Object Copying: Shallow Copy vs Deep Copy (copy module)
# - Serialization: JSON vs pickle (and security caveats)
# - Regular Expressions (re module): Named Groups, Lookahead, Lookbehind

import copy
import json
import pickle
import re
import operator
import functools
import itertools


# ------------------------------------------------------------------------------
# 1. Functional Python & the operator Module
# ------------------------------------------------------------------------------
print("=== 1. Functional Programming & operator ===")

numbers = [1, 2, 3, 4, 5]

# map and filter
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("map (doubled):", doubled)
print("filter (evens):", evens)

# functools.reduce
sum_total = functools.reduce(lambda acc, x: acc + x, numbers)
print("reduce (sum):  ", sum_total)

# operator.itemgetter & operator.attrgetter
records = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]
sorted_by_score = sorted(records, key=operator.itemgetter(1), reverse=True)
print("Sorted by score using itemgetter:", sorted_by_score)


# ------------------------------------------------------------------------------
# 2. functools: lru_cache, partial, and singledispatch
# ------------------------------------------------------------------------------
print("\n=== 2. functools Utilities ===")

# lru_cache (Memoization)
@functools.lru_cache(maxsize=128)
def expensive_fib(n: int) -> int:
    if n < 2:
        return n
    return expensive_fib(n - 1) + expensive_fib(n - 2)

print("Fibonacci(35) via lru_cache:", expensive_fib(35))
print("Cache info:                  ", expensive_fib.cache_info())

# functools.partial: Freezes a portion of a function's arguments
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)
print("Square of 7 via partial:", square(7))
print("Cube of 3 via partial:  ", cube(3))

# functools.singledispatch: Function Overloading based on argument type
@functools.singledispatch
def serialize(val):
    return f"Default string: {str(val)}"

@serialize.register(int)
def _(val: int):
    return f"Integer number: {val:,}"

@serialize.register(list)
def _(val: list):
    return f"List with {len(val)} items: [{', '.join(map(str, val))}]"

print("singledispatch (int): ", serialize(1_000_000))
print("singledispatch (list):", serialize([1, 2, 3]))
print("singledispatch (str): ", serialize("plain text"))


# ------------------------------------------------------------------------------
# 3. itertools: Infinite, Terminating, and Combinatoric Iterators
# ------------------------------------------------------------------------------
print("\n=== 3. itertools Module ===")

# chain: Chains multiple iterables together seamlessly
combined = list(itertools.chain([1, 2], ["a", "b"], [10, 20]))
print("chain():", combined)

# pairwise (Python 3.10+): Successive overlapping pairs
items = ["A", "B", "C", "D"]
print("pairwise():", list(itertools.pairwise(items)))

# groupby: Groups consecutive items by key (requires data to be sorted by key)
data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot"), ("veg", "broccoli")]
grouped = {k: list(v) for k, v in itertools.groupby(data, key=lambda x: x[0])}
print("groupby():", grouped)

# Combinations & Permutations
print("Combinations of ('A', 'B', 'C') size 2: ", list(itertools.combinations(["A", "B", "C"], 2)))
print("Permutations of ('A', 'B') size 2:      ", list(itertools.permutations(["A", "B"], 2)))


# ------------------------------------------------------------------------------
# 4. Object Copying: Shallow Copy vs Deep Copy
# ------------------------------------------------------------------------------
print("\n=== 4. Shallow Copy vs Deep Copy ===")

original = [[1, 2, 3], [4, 5, 6]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify nested element in original
original[0][0] = 999

print("Original after modification: ", original)
print("Shallow copy (nested changed):", shallow)  # Reflects the change!
print("Deep copy (completely immune):", deep)     # Completely independent!


# ------------------------------------------------------------------------------
# 5. Serialization: JSON vs pickle
# ------------------------------------------------------------------------------
print("\n=== 5. Serialization (JSON vs pickle) ===")

user_data = {"id": 1, "name": "Elena", "roles": ["Admin", "User"]}

# JSON: Human-readable, language-agnostic, safe
json_str = json.dumps(user_data)
print("JSON serialized string:  ", json_str)
print("JSON deserialized object:", json.loads(json_str))

# pickle: Python-specific, supports complex arbitrary Python objects
# SECURITY WARNING: Never unpickle untrusted data (can execute arbitrary code)!
pickled_bytes = pickle.dumps(user_data)
print("Pickled byte representation:", pickled_bytes)
print("Unpickled object:           ", pickle.loads(pickled_bytes))


# ------------------------------------------------------------------------------
# 6. Regular Expressions: Groups, Lookaheads & Lookbehinds
# ------------------------------------------------------------------------------
print("\n=== 6. Regular Expressions (re) ===")

text = "Invoice #1042: Total amount $250.00 on 2024-05-12."

# Named Capture Groups (?P<name>...)
pattern = r"(?P<currency>[$€£])(?P<amount>\d+\.\d{2})"
match = re.search(pattern, text)
if match:
    print(f"Currency: {match.group('currency')}, Amount: {match.group('amount')}")

# Positive Lookahead (?=...): Matches a pattern only if followed by another pattern
# Extracts word before 'amount' without including 'amount' in the match:
lookahead_match = re.search(r"\b\w+(?=\s+amount)", text)
if lookahead_match:
    print("Word before 'amount' via Lookahead:", lookahead_match.group())

# Positive Lookbehind (?<=...): Matches a pattern only if preceded by another pattern
# Extracts dollar amount digits preceded by '$':
lookbehind_match = re.search(r"(?<=\$)\d+\.\d{2}", text)
if lookbehind_match:
    print("Amount extracted via Lookbehind:   ", lookbehind_match.group())
