N = input()
score = 0.0

if N[0] == "A": score += 4
elif N[0] == "B": score += 3
elif N[0] == "C": score += 2
elif N[0] == "D": score += 1

if score != 0.0:
    if N[1] == "+": score += 0.3
    elif N[1] == "0": score += 0.0
    elif N[1] == "-": score -= 0.3
    else: print(0.0)

print(score)