import copy
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    line = N//H + 1
    if N%H == 0: 
        floor = copy.copy(H)
        line -= 1
    else: floor = N%H
    print(floor * 100 + line)