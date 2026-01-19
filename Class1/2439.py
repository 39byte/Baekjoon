N = int(input())
for i in range(N, 0, -1):
    print(" "*(i-1), end="")
    print("*"*(N-i+1))