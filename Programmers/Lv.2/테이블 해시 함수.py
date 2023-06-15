def solution(data, col, row_begin, row_end):
    answer = 0
    # col-1번째 값으로 오름차순, 동일할 시 첫 번째 컬럼의 값을 기준으로 내림차순
    data = sorted(data, key=lambda x: [x[col - 1], -x[0]])

    for i in range(row_begin, row_end + 1):
        total = 0
        for j in data[i - 1]:
            total += (j % i)

        # mod 연산된 값의 합을 XOR연산
        answer ^= total

    return answer
