N = input()
for i in range(len(N)):
    if str.islower(N[i]) == True:
        N = N[:i] + str.upper(N[i]) + N[i+1:]
    else:
        N = N[:i] + str.lower(N[i]) + N[i+1:]
print(N)

# N = 'hello'
# print(str.islower(N[2]))