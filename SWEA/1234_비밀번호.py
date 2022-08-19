for t in range(1, 11):
    n, lst = input().split()
    st = []

    for i in lst:
        if len(st) > 0:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
        else:
            st.append(i)

    result = ''.join(st)
    print(f'#{t} {result}')