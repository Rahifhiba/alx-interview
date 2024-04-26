#!/usr/bin/python3
"""pascal triangles"""
import math


def pascal_triangle(n):
    """doc"""
    if n<= 0:
        return []
    pascal = lambda n, col: math.factorial(n) / (
        math.factorial(col) * math.factorial(n - col)
    )
    lst_final = []
    for row in range(n + 1):
        lst = []
        for col in range(row + 1):
            lst.append(int(pascal(row, col)))
        lst_final.append(lst)
    return lst_final
