#!/usr/bin/env python3
"""a type-annotated function"""


def sum_list(input_list: list[float]) -> float:
    """return sum of list element"""
    sum: float = 0
    for i in range(len(input_list)):
        sum = sum + input_list[i]
    return sum
