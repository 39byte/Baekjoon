T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    total = ''

    for j in range(len(S)):
        total += S[j] * int(R)
    print(total)