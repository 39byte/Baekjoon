N = list(map(int, input().split()))

st = ''
if N[0] == 1:
    st = 'ascending'
    for i in range(1, 9):
        if N[i-1] != i:
            st = 'mixed'
            break
elif N[0] == 8:
    st = 'descending'
    index = 0
    for i in range(8, 0, -1):
        if N[index] != i:
            st = 'mixed'
            break
        index += 1
else: st = 'mixed'

print(st)