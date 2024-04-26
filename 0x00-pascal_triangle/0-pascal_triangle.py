#!/usr/bin/python3
"""pascal triangles"""


def fac(n):
    """factorial"""
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def pascal(n, col):
    """pascal func"""
    return fac(n) / (fac(col) * fac(n - col))


def pascal_triangle(n):
    """doc"""
    if n <= 0:
        return []
    lst_final = []
    for row in range(n):
        lst = []
        for col in range(row + 1):
            lst.append(int(pascal(row, col)))
        lst_final.append(lst)
    return lst_final
