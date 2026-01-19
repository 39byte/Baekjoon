total = []
for i in range(5):
    a, b = map(int, input().split())
    total.append(a + b)
for i in total:
    print(i)

while True:
    try: 
        a, b = map(int, input().split())
        print(a+b)
    except: break