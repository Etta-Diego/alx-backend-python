#!/usr/bin/env python3

"""
A type-annotated function define_variables that define
the following variables with their specified values:

a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton”
"""


from typing import Tuple

""" defining the variables """
a = 1
pi = 3.14
i_understand_annotations = True
school = "Holberton"


def define_variables(a: int, pi: float, i_understand_annotations:
                     bool, school: str) -> Tuple[int, float, bool, str]:
    """return the defined variables"""
    return a, pi, i_understand_annotations, school
