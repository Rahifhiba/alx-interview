#!/usr/bin/python3
"""check if all lockbox can be unlocked"""


def canUnlockAll(boxes):
    """lockbox"""
    opened = [0]
    for i in opened:
        for j in boxes[i]:
            if j not in opened and j < len(boxes):
                opened.append(j)
    return len(opened) == len(boxes)
