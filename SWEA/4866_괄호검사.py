tc = int(input())
for t in range(1, tc+1):
    st = []
    lst = input()
    result = 1

    for s in lst:
        if s == '{' or s == '(':
            st.append(s)

        elif s == '}' or s == ')':
            if len(st) == 0:
                result = 0
                break
            elif s == '}' and st.pop() == '(':
                result = 0
                break
            elif s == ')' and st.pop() == '{':
                result = 0
                break

    if len(st):
        result = 0

    print(f'#{t} {result}')
