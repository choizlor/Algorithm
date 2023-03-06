def solution(s):
    lst = list(s)
    st = []
    for i in lst:
        if (i == '('):
            st.append(i);
        else:
            if st == []:
                return False;
            else:
                st.pop();
    if(st != []):
        return False;
    else:
        return True;

