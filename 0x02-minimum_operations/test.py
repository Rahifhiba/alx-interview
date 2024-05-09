#!/usr/bin/python3


# copy all > paste > paste > copy all > paste > paste ...
# c, p, p, c, p, p,  c , p , p, c, p, p
# 1, 2, 3,    6, 9,      18, 27,   54, 81

def minOperations(n):
    num_op = []
    hs = "h"
    while len(hs) != n:
        if n <= 0:
            return 0
        num_op.append("ca")
        le_hs = len(hs)
        if n % 2 == 0:
            num_op.append("p")
            hs += (len(hs) * "h")
            num_op.append("ca")
            num_op.append("p")
            hs += (len(hs) * "h")
        else :
            num_op.append("p")
            hs += (le_hs * "h")
            num_op.append("p")
            hs += (le_hs * "h")
    return len(num_op)

# hs = "h"
# print(len(hs))
n=5
print("Min # of operations to reach {} char: {}".format(5, minOperations(5)))
# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))