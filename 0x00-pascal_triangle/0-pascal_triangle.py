#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """doc"""
    lst = []
    if n <= 0:
        return lst
    for i in range(0, n):
        res = [int(x) for x in str(11**i)]
        lst.append(res)
    return lst
