#!/usr/bin/python3
boxes = [[1], [2], [3], [4], []]
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

def delist_list(lst):
    final = []
    for i in lst:
        for j in i:
            final.append(j)
    return final
def delist(lst):
    final = []
    for i in lst:
        final.append(i)
    return final

# print(delist(boxes)
# )
opened = delist(boxes[0])
# opened = [value for sublist in boxes[0]]
print("opened: first", opened)
for i in boxes:
    if boxes.index(i) in opened:
        opened.append(i)

print("opened final:", opened)