# ALX Backend - Python Variable Annotations

This directory, `0x00-python_variable_annotations`, contains tasks that explore advanced Python features, focusing on type annotations, which improve code readability, robustness, and type checking.

## Learning Objectives

By the end of this project, you will be able to:
- Understand and use type annotations in Python 3.
- Specify function signatures and variable types through type hints.
- Apply duck typing principles.
- Use `mypy` for code validation.

## Resources

Here are the main resources that may help you in the project:
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Requirements

- Code editor: `vi`, `vim`, or `emacs`
- Files should be interpreted on **Ubuntu 18.04 LTS** using **Python 3.7**
- Follow **pycodestyle** (version 2.5) style
- All files must be executable and end with a newline
- Document all modules, classes, and functions meaningfully

## Task List

1. **Basic Annotations - Add**
   - Define `add(a: float, b: float) -> float`: Adds two floats.

2. **Basic Annotations - Concat**
   - Define `concat(str1: str, str2: str) -> str`: Concatenates two strings.

3. **Basic Annotations - Floor**
   - Define `floor(n: float) -> int`: Returns the floor of a float.

4. **Basic Annotations - To String**
   - Define `to_str(n: float) -> str`: Converts a float to a string.

5. **Define Variables**
   - Annotate variables: integer `a = 1`, float `pi = 3.14`, boolean `i_understand_annotations = True`, and string `school = "Holberton"`.

6. **Complex Types - List of Floats**
   - Define `sum_list(input_list: List[float]) -> float`: Returns the sum of a list of floats.

7. **Complex Types - Mixed List**
   - Define `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`: Sums integers and floats in a list.

8. **Complex Types - String and Int/Float to Tuple**
   - Define `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`: Returns a tuple with the string and square of the int/float.

9. **Complex Types - Functions**
   - Define `make_multiplier(multiplier: float) -> Callable[[float], float]`: Returns a multiplier function.

10. **Duck Typing - Element Length**
    - Annotate `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]`: Returns length of each element in a sequence.

11. **Duck Typing - First Element of a Sequence** (Advanced)
    - Annotate `safe_first_element(lst: Sequence[Any]) -> Union[Any, None]`: Returns the first element or None.

12. **More Involved Type Annotations** (Advanced)
    - Annotate `safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]`: Retrieves a dictionary value safely.

13. **Type Checking** (Advanced)
    - Use `mypy` to validate and refine function `zoom_array`.

## Usage

To test these functions:
```bash
python3 <task>-main.py

