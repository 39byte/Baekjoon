S = input()
ref = "abcdefghijklmnopqrstuvwxyz"
L = []

for i in range(len(ref)):
    if ref[i] in S: # 만일 안에 존재하면 서칭 시작
        L.append(S.find(ref[i]))
    else: L.append(-1)
for i in L:
    print(i, end=" ")