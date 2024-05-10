#!/usr/bin/python3
""" 0. Minimum Operations
copyall -> paste -> paste -> copyall -> paste *2
"""


def minOperations(n):
    """method that calculates the fewest number of
    operations needed to result in exactly n H"""
    num_op = []
    hs = "h"
    while len(hs) < n:
        if n <= 0:
            return 0
        num_op.append("ca")
        le_hs = len(hs)
        if n % 2 == 0:
            num_op.append("p")
            hs += len(hs) * "h"
            num_op.append("ca")
            num_op.append("p")
            hs += len(hs) * "h"
        else:
            num_op.append("p")
            hs += le_hs * "h"
            num_op.append("p")
            hs += le_hs * "h"
    return len(num_op)
