N = list(map(int, input().split()))
total = 0
for i in range(len(N)):
    N[i] **= 2
    total += N[i]
print(total % 10)