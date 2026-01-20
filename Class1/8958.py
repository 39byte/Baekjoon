T = int(input())
for i in range(T):
    L = []
    L = list(input().replace("X", " ").split())
    total = 0
    for j in L:
        for k in range(1, len(j)+1):
            total += k
    print(total)