N = input()
for i in range(len(N)):
    if str.islower(N[i]) == True:
        # if i == 0:
        #     N = str.upper(N[i]) + N[i+1:]
        #     continue
        N = N[:i] + str.upper(N[i]) + N[i+1:]
    else:
        # if i == 0:
        #     N = str.lower(N[i]) + N[i+1:]
        #     continue 
        N = N[:i] + str.lower(N[i]) + N[i+1:]
print(N)

# N = 'hello'
# print(str.islower(N[2]))