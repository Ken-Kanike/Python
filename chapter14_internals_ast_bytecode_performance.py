# ==============================================================================
# Chapter 14: Python Internals: AST, Bytecode, Introspection & Profiling
# ==============================================================================
# Topics Covered:
# - Runtime Introspection (inspect module, call stack inspection)
# - Abstract Syntax Trees (ast.parse, ast.NodeVisitor)
# - Python Bytecode & Code Objects (dis module, __code__, co_consts, co_varnames)
# - Dynamic Code Execution: compile(), eval(), exec()
# - Memory Profiling (sys.getsizeof, tracemalloc)
# - Benchmarking with timeit & cProfile
# - CPython Internals Overview (PyObject, Reference Counting, Cyclic GC)

import ast
import dis
import inspect
import sys
import timeit
import tracemalloc
import gc


# ------------------------------------------------------------------------------
# 1. Runtime Introspection (inspect Module)
# ------------------------------------------------------------------------------
print("=== 1. Runtime Introspection (inspect Module) ===")

def calculate_discount(price: float, rate: float = 0.1) -> float:
    """Calculates discounted price based on rate."""
    current_frame = inspect.currentframe()
    print(f"Inside function '{calculate_discount.__name__}' at line {current_frame.f_lineno}")
    return price * (1 - rate)

# Inspect function signature and docstrings
sig = inspect.signature(calculate_discount)
print("Function Signature: ", sig)
print("Parameter details:  ", {p.name: p.default for p in sig.parameters.values()})
calculate_discount(100.0)


# ------------------------------------------------------------------------------
# 2. Abstract Syntax Trees (ast Module)
# ------------------------------------------------------------------------------
print("\n=== 2. Abstract Syntax Trees (ast) ===")

source_code = "result = 10 + 20 * 2"
parsed_ast = ast.parse(source_code)
print("AST Dump:\n", ast.dump(parsed_ast, indent=2))

# AST Visitor pattern: Traverse syntax nodes
class VariableNameCollector(ast.NodeVisitor):
    def __init__(self):
        self.names = []

    def visit_Name(self, node):
        self.names.append(node.id)
        self.generic_visit(node)

collector = VariableNameCollector()
collector.visit(ast.parse("x = 5; y = x + 10; z = math.sqrt(y)"))
print("Variables discovered by AST Visitor:", collector.names)


# ------------------------------------------------------------------------------
# 3. Python Bytecode & Disassembly (dis Module)
# ------------------------------------------------------------------------------
print("\n=== 3. Python Bytecode Disassembly (dis) ===")

def sample_math(a, b):
    return (a + b) * 2

print("Disassembly of sample_math:")
dis.dis(sample_math)

# Inspecting Code Objects (__code__)
code_obj = sample_math.__code__
print("\n--- Code Object Attributes ---")
print("co_varnames (local variables):", code_obj.co_varnames)
print("co_consts   (constants in code):", code_obj.co_consts)
print("co_argcount (argument count):  ", code_obj.co_argcount)


# ------------------------------------------------------------------------------
# 4. Compilation & Dynamic Execution (compile, eval, exec)
# ------------------------------------------------------------------------------
print("\n=== 4. Dynamic Execution (compile, eval, exec) ===")

# eval: Evaluates a single Python expression and returns its value
val = eval("3 * 10 + 5")
print("eval('3 * 10 + 5'):", val)

# compile: Compiles string source code into a Python code object for fast repeated execution
compiled_code = compile("for i in range(3): print(f'Compiled loop step: {i}')", "<string>", "exec")
exec(compiled_code)


# ------------------------------------------------------------------------------
# 5. Memory Profiling (sys.getsizeof & tracemalloc)
# ------------------------------------------------------------------------------
print("\n=== 5. Memory Profiling ===")

# sys.getsizeof shows shallow memory allocation
print(f"Memory size of integer 42:          {sys.getsizeof(42)} bytes")
print(f"Memory size of empty list:          {sys.getsizeof([])} bytes")
print(f"Memory size of list with 100 items: {sys.getsizeof([0] * 100)} bytes")

# tracemalloc: Tracks memory allocations during runtime
tracemalloc.start()
large_dataset = [i ** 2 for i in range(50_000)]
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Current memory: {current_mem / (1024):.2f} KB | Peak memory: {peak_mem / (1024):.2f} KB")


# ------------------------------------------------------------------------------
# 6. Performance Benchmarking with timeit
# ------------------------------------------------------------------------------
print("\n=== 6. Performance Benchmarking (timeit) ===")

# Comparing list comprehension vs map()
time_comp = timeit.timeit("[x * 2 for x in range(1000)]", number=10_000)
time_map = timeit.timeit("list(map(lambda x: x * 2, range(1000)))", number=10_000)

print(f"List Comprehension (10k runs): {time_comp:.4f}s")
print(f"map with lambda    (10k runs): {time_map:.4f}s")


# ------------------------------------------------------------------------------
# 7. CPython Runtime, Reference Counting & Cyclic GC
# ------------------------------------------------------------------------------
print("\n=== 7. CPython Internals & Garbage Collection (gc) ===")
# In CPython, memory is freed primarily through reference counting.
# When refcount reaches 0, the memory is deallocated immediately.
# The cyclic Garbage Collector (gc module) handles circular reference cycles.

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

# Create circular reference: node_a -> node_b -> node_a
node_a = Node("A")
node_b = Node("B")
node_a.link = node_b
node_b.link = node_a

print("Reference count of node_a:", sys.getrefcount(node_a) - 1)  # -1 for getrefcount's own reference

# Delete external variables (cycle remains in memory)
del node_a
del node_b

# Force cyclic garbage collection run
unreachable_collected = gc.collect()
print(f"Cyclic GC collected {unreachable_collected} circular referenced objects.")
