T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    print(f"{N%H}{N//H+1:02d}")