def solution(numbers):
    answer = [-1] * len(numbers)
    st = []

    for i in range(len(numbers)):
        # stack에 담겨있는 값이 새로 나온 값보다 작으면 그때 값 바꿔주기
        while st and numbers[st[-1]] < numbers[i]:
            answer[st.pop()] = numbers[i]
        st.append(i) # 값이 numbers[st[-1]]보다 작으면 stack에 담기

    return answer