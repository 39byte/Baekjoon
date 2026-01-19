N = int(input())
L = list(map(int, input().split()))
max = -1000000; min = 1000000
for i in range(N):
    if L[i] > max: max = L[i]
    if L[i] < min: min = L[i]
print(min, max)