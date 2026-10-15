# ==============================================================================
# Chapter 13: Concurrency, Multiprocessing & AsyncIO in Python
# ==============================================================================
# Topics Covered:
# - Concurrency Models: I/O Bound vs CPU Bound & The Global Interpreter Lock (GIL)
# - Threading (threading module, Race Conditions, Locks, Semaphores, Thread Queues)
# - Multiprocessing (multiprocessing, ProcessPoolExecutor, Bypassing the GIL)
# - Asynchronous Programming (asyncio, Coroutines, Event Loop, Tasks, gather)
# - Async Context Managers & Async Iterators

import time
import threading
import queue
import asyncio
from concurrent.futures import ThreadPoolExecutor


# ------------------------------------------------------------------------------
# 1. Threading for I/O Bound Tasks (threading Module)
# ------------------------------------------------------------------------------
print("=== 1. Threading & Synchronization Locks ===")

# Shared resource and lock to prevent race conditions
counter = 0
counter_lock = threading.Lock()

def safe_increment(n: int):
    global counter
    for _ in range(n):
        # Acquire lock before modifying shared memory
        with counter_lock:
            counter += 1

threads = [threading.Thread(target=safe_increment, args=(10_000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter value after 5 concurrent threads: {counter}")


# ------------------------------------------------------------------------------
# 2. Producer-Consumer Pattern using thread-safe queue.Queue
# ------------------------------------------------------------------------------
print("\n=== 2. Thread-Safe Queue (Producer-Consumer) ===")

task_queue = queue.Queue(maxsize=5)

def producer():
    for item in range(1, 4):
        task_queue.put(item)
        print(f"Produced task #{item}")

def consumer():
    while not task_queue.empty():
        item = task_queue.get()
        print(f"  Consumed task #{item}")
        task_queue.task_done()

prod_thread = threading.Thread(target=producer)
cons_thread = threading.Thread(target=consumer)
prod_thread.start()
prod_thread.join()
cons_thread.start()
cons_thread.join()


# ------------------------------------------------------------------------------
# 3. ThreadPoolExecutor for High-Throughput I/O
# ------------------------------------------------------------------------------
print("\n=== 3. ThreadPoolExecutor ===")

def mock_io_fetch(task_id: int) -> str:
    time.sleep(0.05)  # Simulate non-blocking network wait
    return f"Response from API #{task_id}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(mock_io_fetch, range(1, 4)))
    for res in results:
        print(" ", res)


# ------------------------------------------------------------------------------
# 4. Multiprocessing for CPU-Bound Parallelism
# ------------------------------------------------------------------------------
print("\n=== 4. Multiprocessing Concept (Bypassing the GIL) ===")
# Python's GIL allows only one native thread to execute bytecode at a time.
# For heavy CPU workloads (cryptography, image processing, math), multiprocessing
# creates separate OS processes with independent memory and independent GILs!

def cpu_heavy_computation(n: int) -> int:
    """CPU-bound task."""
    return sum(i * i for i in range(n))

# Note: On Windows, multiprocessing code must always be guarded inside __name__ == '__main__'
print("CPU task result: ", cpu_heavy_computation(50_000))


# ------------------------------------------------------------------------------
# 5. Modern AsyncIO (Cooperative Concurrency)
# ------------------------------------------------------------------------------
print("\n=== 5. AsyncIO (async / await) ===")
# Asyncio runs on a single thread using an event loop to cooperatively switch tasks.

async def async_fetch(site_name: str, delay: float) -> str:
    print(f"[{site_name}] Fetch started...")
    # asyncio.sleep yields control back to the event loop without blocking the thread
    await asyncio.sleep(delay)
    print(f"[{site_name}] Fetch completed!")
    return f"{site_name} Data"

async def main_async():
    # Running multiple coroutines concurrently using asyncio.gather
    print("Launching async coroutines concurrently...")
    start_time = time.perf_counter()
    
    results = await asyncio.gather(
        async_fetch("Server A", 0.1),
        async_fetch("Server B", 0.05),
        async_fetch("Server C", 0.08),
    )
    
    elapsed = time.perf_counter() - start_time
    print(f"All 3 async calls resolved in {elapsed:.3f}s total (Concurrent!):", results)

# Run the async event loop
asyncio.run(main_async())


# ------------------------------------------------------------------------------
# 6. Async Context Manager & Async Iterator
# ------------------------------------------------------------------------------
print("\n=== 6. Async Context Managers & Async Iterators ===")

class AsyncResource:
    """Implements the __aenter__ and __aexit__ protocol."""
    async def __aenter__(self):
        print("Acquiring async database connection...")
        await asyncio.sleep(0.01)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing async database connection...")
        await asyncio.sleep(0.01)

class AsyncNumberStream:
    """Implements the __aiter__ and __anext__ protocol."""
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(0.01)
        self.count += 1
        return self.count

async def test_async_advanced():
    async with AsyncResource():
        print("Inside async context block.")
        async for num in AsyncNumberStream(3):
            print(f"Async streaming item #{num}")

asyncio.run(test_async_advanced())
