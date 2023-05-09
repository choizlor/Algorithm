def solution(s):
    answer = 0

    lst = list(s)
    for k in range(0, len(lst)):
        st = []
        tmp = lst.pop(0)
        lst.append(tmp)
        st.append(lst[0])

        for i in lst[1:]:
            if i == ']':
                if st and st[-1] == '[':
                    st.pop()
            elif i == ')':
                if st and st[-1] == '(':
                    st.pop()
            elif i == '}':
                if st and st[-1] == '{':
                    st.pop()
            else:
                st.append(i)

        if not len(st):
            answer += 1

    return answer

solution("[](){}")
solution("}]()[{")
solution("[)(]")
solution("}}}")
