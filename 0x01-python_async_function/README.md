0x01. Python - Async
This directory contains Python scripts focused on asynchronous programming using asyncio in Python 3.7 on Ubuntu 18.04 LTS.

Resources
Read or watch:

Async IO in Python: A Complete Walkthrough
asyncio - Asynchronous I/O
random.uniform
Learning Objectives
By the end of this project, you will understand:

async and await syntax
How to execute an async program with asyncio
How to run concurrent coroutines
How to create asyncio tasks
How to use the random module for asynchronous operations
Requirements
A README.md file, at the root of the folder of the project, is mandatory
Allowed editors: vi, vim, emacs
All files are interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All files should end with a new line
All files must be executable
The first line of all files should be exactly #!/usr/bin/env python3
Code should use the pycodestyle style (version 2.5.x)
All functions and coroutines must be type-annotated
All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
Tasks Overview
The basics of async: Implement an asynchronous coroutine wait_random that waits for a random delay.
Let's execute multiple coroutines at the same time with async: Implement wait_n to run wait_random multiple times concurrently.
Measure the runtime: Measure the execution time of wait_n and calculate average time per coroutine execution.
Tasks: Implement non-async functions using asyncio's Task to manage coroutines.
Files
0-basic_async_syntax.py: Implementation of wait_random.
1-concurrent_coroutines.py: Implementation of wait_n.
2-measure_runtime.py: Measure the runtime of wait_n.
3-tasks.py: Implementation of task_wait_random.
4-tasks.py: Implementation of task_wait_n.
