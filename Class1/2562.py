import copy

L = []
for i in range(9):
    L.append(int(input()))

index = 1; max = 0; max_index = 0
for i in L:
    if i > max:
        max = i; max_index = copy.copy(index)
    index += 1
print(max)
print(max_index)