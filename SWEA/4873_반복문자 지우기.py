tc = int(input())

for t in range(1, tc+1):
    lst = input()
    st = []
    
    for i in lst:
        if len(st) > 0:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
        else:
            st.append(i)

    print(f'#{t} {len(st)}')