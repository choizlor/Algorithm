def solution(k, tangerine):
    answer = 0
    dic = {}

    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    tan = sorted(dic.values(), key=lambda x: x)

    while k > 0:
        k -= tan.pop()
        answer += 1

    return answer


solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
solution(2, [1, 1, 1, 1, 2, 2, 2, 3])
