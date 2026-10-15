# 🐍 Python Learning At One Spot — Core to Advanced

> A comprehensive, hands-on Python repository covering the complete journey from **day-one fundamentals** to **advanced CPython internals, async concurrency, and production projects**.

[![Live Interactive Web Playground](https://img.shields.io/badge/Live%20Demo-Interactive%20Web%20Playground-3776AB?style=for-the-badge&logo=python&logoColor=ffd43b)](https://ken-kanike.github.io/Python/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Site-brightgreen?style=for-the-badge&logo=github)](https://ken-kanike.github.io/Python/)

🌐 **Live Interactive Playground:** [**https://ken-kanike.github.io/Python/**](https://ken-kanike.github.io/Python/)  
*Run, edit, and experiment with 100+ Python files directly in your browser with zero setup (powered by Pyodide WebAssembly).*

---

## 📚 Curriculum Roadmap

```
Python Learning at One Spot
├── 🟢 1. Fundamentals & Core Chapters (0 to 6)
│   ├── 1helloWorld.py          → Execution model, dynamic typing, __name__ == '__main__'
│   ├── 2Operators.py           → Arithmetic, identity, bitwise, walrus :=, precedence
│   ├── chapter1.py             → Variables, casting, data types, comments
│   ├── chapter2.py             → Strings, formatting, slicing, methods
│   ├── chapter3.py             → Lists, Tuples, Sets, Dictionaries
│   ├── chapter4.py             → Control flow, loops, functions, lambdas
│   ├── chapter5.py             → OOP foundations, inheritance, methods
│   └── chapter6.py             → Basic file handling, mathematical scripts
│
├── 🟣 2. Deep Dive & Advanced Chapters (7 to 14)
│   ├── chapter7_oop_advanced.py             → @classmethod, @property, ABCs, MRO & C3, Mixins
│   ├── chapter8_iterators_generators.py     → Iterator protocol, yield from, pipelines, comprehensions
│   ├── chapter9_decorators_context_managers.py → Wraps, factories, class decorators, contextlib
│   ├── chapter10_dunders_descriptors_metaclasses.py → Descriptors, __slots__, __new__, Metaclasses
│   ├── chapter11_typing_exceptions_modules.py  → Generics, Protocol, ExceptionGroups, LEGB scope
│   ├── chapter12_stdlib_functional_itertools.py → lru_cache, itertools, copying, regex, serialization
│   ├── chapter13_concurrency_multiprocessing_async.py → Threads, Locks, Multiprocessing, AsyncIO
│   └── chapter14_internals_ast_bytecode_performance.py → AST, bytecode dis, introspection, memory/GC
│
├── 🔵 3. Data Science & Core Libraries
│   ├── NumpyDemo/              → ndarray, broadcasting, vectorization, linear algebra
│   ├── PandasDemo/             → Series, DataFrame, loc/iloc, GroupBy, missing data
│   ├── MatplotlibDemo/         → Subplots, time-series line & scatter visualizations
│   ├── File Handling/          → Binary streams, pathlib, StringIO, CSV, JSON
│   ├── PyMySQL/                → MySQL database connectivity & Tkinter CRUD UI
│   └── MyMathPackage/          → Custom reusable arithmetic modular package
│
├── 🟡 4. Lab Practicals & College Question Banks
│   ├── Practcals/              → Lab experiments 1 to 16 fully solved
│   ├── manual pr/              → MSBTE curriculum lab practical manuals
│   ├── Ct1Qb/                  → Class Test 1 solved question bank
│   └── Ct2Qb/                  → Class Test 2 solved question bank
│
└── 🟠 5. Mini Projects & Bots
    ├── PythonProjects/
    │   ├── 1_QRcode/           → Dynamic QR code generation with PIL
    │   ├── 2_NumberInfo/       → Web scraping and number trace utilities
    │   ├── 3_Whatssapp/        → WhatsApp automation script
    │   ├── 4_FaceDetection/    → OpenCV live webcam Haar Cascade face tracking
    │   ├── 5_tkinter_gui/      → Animated GUI attendance & background video system
    │   └── 6_AiApiFetching/    → Google Gemini AI interactive client
    ├── TrackFlexBot/           → Groq LLM Telegram assistant bot
    └── E_MP/                   → Interactive CLI Todo List microproject
```

---

## 🧭 Complete 38-Topic Topic Map Index

| # | Topic | Implemented In |
|---|---|---|
| **1** | Python Object Model (Identity, `id()`, `is` vs `==`, Interning) | [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) & [2Operators.py](2Operators.py) |
| **2** | Advanced Functions (`*args`, `**kwargs`, Positional-only `/`, Keyword-only `*`, Closures) | [YtoCodes/functions.py](YtoCodes/functions.py) |
| **3** | Decorators (`functools.wraps`, factories, class decorators, stateful) | [chapter9_decorators_context_managers.py](chapter9_decorators_context_managers.py) |
| **4** | Iterators (Iterable vs Iterator protocol, sentinel `iter()`) | [chapter8_iterators_generators.py](chapter8_iterators_generators.py) |
| **5** | Generators (`yield`, `yield from`, `send()`, `throw()`, `close()`, pipelines) | [chapter8_iterators_generators.py](chapter8_iterators_generators.py) |
| **6** | Comprehensions (List, Set, Dict, Nested, Scope isolation) | [chapter8_iterators_generators.py](chapter8_iterators_generators.py) |
| **7** | Context Managers (`__enter__`, `__exit__`, `contextlib`, `ExitStack`) | [chapter9_decorators_context_managers.py](chapter9_decorators_context_managers.py) |
| **8** | Advanced OOP (Class/Static methods, Properties, MRO, C3, Mixins) | [chapter7_oop_advanced.py](chapter7_oop_advanced.py) |
| **9** | Dunder Methods (`__repr__`, `__len__`, `__getitem__`, `__add__`, etc.) | [chapter7_oop_advanced.py](chapter7_oop_advanced.py) & [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) |
| **10** | Descriptors (`__get__`, `__set__`, Data vs Non-Data descriptors) | [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) |
| **11** | Attribute Access (`__getattr__`, `__getattribute__`, instance/class dict) | [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) |
| **12** | `__slots__` (Memory savings, removing `__dict__`) | [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) |
| **13** | Metaclasses (Classes as objects, dynamic `type()`, `__init_subclass__`) | [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) |
| **14** | Abstract Base Classes (`abc.ABC`, `@abstractmethod`) | [chapter7_oop_advanced.py](chapter7_oop_advanced.py) |
| **15** | Type System (`typing`, `Union`, `Literal`, `Final`, `Protocol`, `Self`, `TypedDict`) | [chapter11_typing_exceptions_modules.py](chapter11_typing_exceptions_modules.py) |
| **16** | Exception System (Chaining `raise from`, `ExceptionGroup`, `except*`) | [chapter11_typing_exceptions_modules.py](chapter11_typing_exceptions_modules.py) |
| **17** | Modules & Imports (`sys.modules`, `importlib`, dynamic imports) | [chapter11_typing_exceptions_modules.py](chapter11_typing_exceptions_modules.py) & [checkLibrary.py](checkLibrary.py) |
| **18** | Scope & Namespaces (LEGB rule, `global`, `nonlocal`, `globals()`) | [chapter11_typing_exceptions_modules.py](chapter11_typing_exceptions_modules.py) |
| **19** | Functional Python (`map`, `filter`, `reduce`, `operator`) | [chapter12_stdlib_functional_itertools.py](chapter12_stdlib_functional_itertools.py) |
| **20** | `functools` (`lru_cache`, `partial`, `singledispatch`) | [chapter12_stdlib_functional_itertools.py](chapter12_stdlib_functional_itertools.py) |
| **21** | `itertools` (`chain`, `groupby`, `islice`, `pairwise`, `combinations`) | [chapter12_stdlib_functional_itertools.py](chapter12_stdlib_functional_itertools.py) |
| **22** | Advanced Data Model (Hashing, equality, container protocols) | [chapter7_oop_advanced.py](chapter7_oop_advanced.py) & [chapter10_dunders_descriptors_metaclasses.py](chapter10_dunders_descriptors_metaclasses.py) |
| **23** | Memory Management (`sys.getsizeof`, `tracemalloc`, `gc` cycle collection) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **24** | Copying (Shallow vs Deep copy with `copy` module) | [chapter12_stdlib_functional_itertools.py](chapter12_stdlib_functional_itertools.py) |
| **25** | Serialization (`json` vs `pickle`, security considerations) | [chapter12_stdlib_functional_itertools.py](chapter12_stdlib_functional_itertools.py) |
| **26** | File & I/O System (`pathlib`, binary I/O, `io.StringIO`, `io.BytesIO`) | [File Handling/handling1.py](File%20Handling/handling1.py) |
| **27** | Regular Expressions (Named groups, Lookaheads, Lookbehinds) | [chapter12_stdlib_functional_itertools.py](chapter12_stdlib_functional_itertools.py) |
| **28** | Concurrency: Threading (`threading.Thread`, `Lock`, `Queue`) | [chapter13_concurrency_multiprocessing_async.py](chapter13_concurrency_multiprocessing_async.py) |
| **29** | Multiprocessing (`Process`, `Pool`, CPU-bound workloads, GIL bypass) | [chapter13_concurrency_multiprocessing_async.py](chapter13_concurrency_multiprocessing_async.py) |
| **30** | Async Python (`async`, `await`, `asyncio.run`, `gather`, async iterators) | [chapter13_concurrency_multiprocessing_async.py](chapter13_concurrency_multiprocessing_async.py) |
| **31** | Introspection (`inspect` signatures, frames, `dir()`, `hasattr()`) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **32** | AST (`ast.parse`, `ast.dump`, `ast.NodeVisitor`) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **33** | Bytecode & Code Objects (`dis.dis`, `__code__`, `co_varnames`) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **34** | Compilation & Execution (`compile()`, `eval()`, `exec()`) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **35** | Standard Library Tools (`collections`, `enum`, `dataclasses`, `pathlib`) | Across Chapters 7, 11, 12, 14 |
| **36** | Performance & Optimization (`timeit`, `cProfile`, algorithmic choices) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **37** | CPython Runtime (GIL, reference counts, cyclic collector) | [chapter14_internals_ast_bytecode_performance.py](chapter14_internals_ast_bytecode_performance.py) |
| **38** | Native Boundary & Extensions (`ctypes`, `sys` modules) | [chapter11_typing_exceptions_modules.py](chapter11_typing_exceptions_modules.py) |

---

## ⚡ Quickstart & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ken-Kanike/Python.git
cd Python
```

### 2. Configure Environment Variables (Optional for AI & Bot Projects)
To run the AI assistants in `chatBot.py`, `TrackFlexBot/`, and `PythonProjects/6_AiApiFetching/`:
```bash
# Copy the example environment file
cp .env.example .env
```
Fill in your API keys in `.env`:
- `GROQ_API_KEY`: Obtain from [console.groq.com](https://console.groq.com)
- `GEMINI_API_KEY`: Obtain from [aistudio.google.com](https://aistudio.google.com)
- `TELEGRAM_BOT_TOKEN`: Obtain from [@BotFather](https://t.me/BotFather)

### 3. Run Any Chapter or Script
Every script is completely self-contained and runnable:
```bash
# Run Core Fundamentals
python 1helloWorld.py
python 2Operators.py

# Run Advanced Topic Chapters
python chapter7_oop_advanced.py
python chapter8_iterators_generators.py
python chapter9_decorators_context_managers.py
python chapter10_dunders_descriptors_metaclasses.py
python chapter11_typing_exceptions_modules.py
python chapter12_stdlib_functional_itertools.py
python chapter13_concurrency_multiprocessing_async.py
python chapter14_internals_ast_bytecode_performance.py

# Run Library Demos
python NumpyDemo/test.py
python PandasDemo/test.py
python MatplotlibDemo/test.py
```

---

## 🛡️ License & Contributions
This project is open-source. Feel free to explore, learn, fork, and contribute!
