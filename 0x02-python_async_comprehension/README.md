# 0x02. Python - Async Comprehension

## Project Overview

This project explores **asynchronous programming** in Python, specifically focusing on **async comprehensions** and **generators**. Here, you will learn how to create asynchronous functions that yield values one at a time, use async comprehensions for clean code, and measure execution time for concurrent tasks. By the end, you will be familiar with Python async programming, especially useful for I/O-bound tasks like network requests and file operations.

---

## Learning Objectives

- **Asynchronous Generators**: Creating async generators that yield values one at a time with pauses.
- **Async Comprehensions**: Writing efficient async code with comprehensions.
- **Type-Hinting Generators**: Adding type hints to asynchronous functions.
- **Concurrency with `asyncio.gather`**: Running multiple async tasks in parallel and measuring their execution time.

## Project Structure

This directory, `0x02-python_async_comprehension`, includes the following tasks:

1. **Async Generator** (`0-async_generator.py`):
   - Write an async generator function, `async_generator`, that yields 10 random float values between 0 and 10 with a 1-second pause between each yield.

2. **Async Comprehension** (`1-async_comprehension.py`):
   - Use an async comprehension to gather 10 values from `async_generator` and return them as a list.

3. **Run Time for Parallel Comprehensions** (`2-measure_runtime.py`):
   - Measure the execution time of running the `async_comprehension` function four times in parallel. Use `asyncio.gather` to execute the tasks concurrently and return the total runtime.

---

## Requirements

- **Environment**: Ubuntu 18.04 LTS, Python 3.7
- **Coding Standards**: Follow `pycodestyle` (v2.5.x) for consistent style.
- **Documentation**: Each module and function must include a docstring explaining its purpose.
- **Type Annotations**: Use type annotations for all functions and coroutines.
- **Executable Files**: Start each file with `#!/usr/bin/env python3`.
- **README.md**: This file is mandatory at the root of the project folder.

---

## Task Breakdown

### Task 0: Async Generator

- **Objective**: Write a coroutine, `async_generator`, that loops 10 times. Each loop:
  - Pauses for 1 second.
  - Yields a random float between 0 and 10.
  
- **Key Points**: 
  - Use `await` with `asyncio.sleep` to pause for exactly 1 second.
  - The `random.uniform(0, 10)` function generates a random float within the specified range.

### Task 1: Async Comprehensions

- **Objective**: Write `async_comprehension`, a coroutine that:
  - Uses an async comprehension to collect 10 values from `async_generator`.
  - Returns the values as a list.
  
- **Key Points**: 
  - Async comprehensions allow for concise, single-line code when handling async generators.
  - Since `async_generator` pauses between each yield, this process will take around 10 seconds.

### Task 2: Measure Runtime

- **Objective**: Write a coroutine, `measure_runtime`, that:
  - Runs `async_comprehension` four times in parallel.
  - Measures and returns the total runtime.
  
- **Explanation**: Although each call to `async_comprehension` takes about 10 seconds, running them in parallel reduces the overall runtime to around 10 seconds instead of 40. This is achieved using `asyncio.gather`, which enables concurrency.

---

## Usage

To test each file:

1. **Run Task 0**: 
   ```bash
   python3 0-main.py


2.  **Run Task 1**:
   ```bash
   python3 1-main.py

3.  **Run Task 2**:
   ```bash
   python3 2-main.py




### Resources
For a deeper understanding of async comprehensions and generators in Python, refer to:

- PEP 530 – Asynchronous Comprehensions
- Python: Asynchronous Comprehensions/Generators
- Type Hints for Generators
