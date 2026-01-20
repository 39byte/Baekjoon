L1 = [] # 검증 이전
L2 = [] # 검증 이후
for i in range(10):
    L1.append(int(input())%42)
for i in L1:
    if i not in L2:
        L2.append(i)
print(len(L2))