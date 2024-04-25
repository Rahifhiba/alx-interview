#!/usr/bin/python3
"""pascal triangle"""

def pascal_triangle(n):
    """doc"""
    lst = []
    lst_final = []
    if n <= 0:
        return lst
    for i in range(0, n):
        for j in str(11**i):
            lst.append(int(j))
        lst_final.append(lst)
    return lst_final