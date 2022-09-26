s = list(input())
st = []
result = []
for i in s:
    if i == '(':
        st.append(s)
    elif i == ')':
        st.pop()
    else:
        result.append(i)
print(result)