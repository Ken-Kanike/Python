# ==============================================================================
# Chapter 8: Iterators, Generators & Comprehensions in Python
# ==============================================================================
# Topics Covered:
# - Iterable vs Iterator (The Iterator Protocol)
# - Building Custom Iterators (__iter__, __next__)
# - iter() with Sentinel Functions
# - Iterator Exhaustion
# - Generators and the 'yield' Keyword
# - Generator Expressions & Lazy Evaluation
# - Delegating Generators with 'yield from'
# - Advanced Generator Methods: send(), throw(), close()
# - Generator Pipelines (Processing Infinite or Massive Streams)
# - Comprehensions: List, Set, Dictionary, Nested Comprehensions & Scopes


# ------------------------------------------------------------------------------
# 1. Iterable vs Iterator Protocol
# ------------------------------------------------------------------------------
print("=== 1. Iterable vs Iterator Protocol ===")
# - Iterable: An object that has an __iter__() method returning an iterator (e.g. list, tuple, str).
# - Iterator: An object with a __next__() method that returns elements one by one,
#   raising StopIteration when exhausted.

numbers = [10, 20, 30]
iterator = iter(numbers)  # Equivalent to numbers.__iter__()

print("Element 1:", next(iterator))  # 10
print("Element 2:", next(iterator))  # 20
print("Element 3:", next(iterator))  # 30
# next(iterator) now would raise StopIteration!


# ------------------------------------------------------------------------------
# 2. Building a Custom Iterator
# ------------------------------------------------------------------------------
print("\n=== 2. Custom Countdown Iterator ===")

class Countdown:
    """Custom iterator counting down from start to 1."""
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for count in Countdown(3):
    print(f"Countdown: {count}")


# ------------------------------------------------------------------------------
# 3. Sentinel-Based Iteration with iter()
# ------------------------------------------------------------------------------
print("\n=== 3. Sentinel Iteration ===")
# iter(callable, sentinel) repeatedly calls 'callable' until it returns 'sentinel'.
import random

def roll_die() -> int:
    return random.randint(1, 6)

# Roll until a 6 is rolled (sentinel is 6)
random.seed(123)
rolls = list(iter(roll_die, 6))
print("Dice rolls before hitting 6:", rolls)


# ------------------------------------------------------------------------------
# 4. Generators: Functions that yield
# ------------------------------------------------------------------------------
print("\n=== 4. Generator Functions & Lazy Evaluation ===")

def fibonacci_generator(limit: int):
    """Generates Fibonacci numbers up to limit using lazy evaluation."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

fib_gen = fibonacci_generator(7)
print("Fibonacci generator object:", fib_gen)
print("Fibonacci values:", list(fib_gen))


# ------------------------------------------------------------------------------
# 5. Generator Delegation: yield from
# ------------------------------------------------------------------------------
print("\n=== 5. Delegating with 'yield from' ===")

def chain_sequences(*iterables):
    """Flattens multiple iterables using 'yield from'."""
    for seq in iterables:
        yield from seq

result = list(chain_sequences([1, 2], ("a", "b"), range(3)))
print("Chained sequences via yield from:", result)


# ------------------------------------------------------------------------------
# 6. Advanced Generator Methods: send(), throw(), close()
# ------------------------------------------------------------------------------
print("\n=== 6. Generator Methods (send, throw, close) ===")

def running_averager():
    """Coroutine-style generator that receives values via send()."""
    total = 0.0
    count = 0
    average = None
    while True:
        # yield returns 'average' to caller and receives new value from send()
        val = yield average
        if val is None:
            break
        total += val
        count += 1
        average = total / count

avg = running_averager()
next(avg)  # Prime the generator (advance to first yield)

print("Average after 10:", avg.send(10))
print("Average after 20:", avg.send(20))
print("Average after 30:", avg.send(30))
avg.close()  # Closes generator; further send() raises StopIteration


# ------------------------------------------------------------------------------
# 7. Generator Pipelines
# ------------------------------------------------------------------------------
print("\n=== 7. Generator Pipelines (Data Stream Processing) ===")
# Pipelines compose lazy generators without consuming memory for intermediate lists.

def number_stream(n: int):
    """Generates integers from 1 to n."""
    for i in range(1, n + 1):
        yield i

def filter_evens(stream):
    """Filters out odd numbers."""
    for x in stream:
        if x % 2 == 0:
            yield x

def square_numbers(stream):
    """Squares every number in the stream."""
    for x in stream:
        yield x ** 2

# Pipeline assembly:
pipeline = square_numbers(filter_evens(number_stream(10)))
print("Pipeline result (even numbers squared up to 10):", list(pipeline))


# ------------------------------------------------------------------------------
# 8. Comprehensions (List, Set, Dict & Scope Behavior)
# ------------------------------------------------------------------------------
print("\n=== 8. Comprehensions & Scopes ===")

# List Comprehension with condition
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print("List Comprehension:      ", squares)

# Set Comprehension (Automatic deduplication)
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_lengths = {len(w) for w in words}
print("Set Comprehension:       ", unique_lengths)

# Dictionary Comprehension
price_map = {"laptop": 1200, "mouse": 25, "keyboard": 75}
discounted_prices = {item: price * 0.9 for item, price in price_map.items()}
print("Dict Comprehension:      ", discounted_prices)

# Nested Comprehensions (e.g. Flattening a 2D matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened 2D matrix:     ", flattened)

# Scope isolation in comprehensions:
# In Python 3, comprehension loop variables do NOT leak into the outer scope.
x = "outer"
[x for x in range(5)]
print("Loop variable 'x' preserved in outer scope:", x)  # Still 'outer'
