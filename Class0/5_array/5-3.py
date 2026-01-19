st = []
for i in range(28):
    st.append(int(input()))
for i in range(1, 31):
    if st.count(i) == 0: 
        print(i)