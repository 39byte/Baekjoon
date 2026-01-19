while True:
    N = input()
    try:
        N = int(N)
    except ValueError:
        try:
            print(f"{N[0]}{N[-1]}")
        except: break