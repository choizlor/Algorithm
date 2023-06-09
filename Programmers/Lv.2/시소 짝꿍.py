def solution(weights):
    answer = 0
    dic = {}

    for w in weights:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    for i in dic:
        if dic[i] > 1:
            answer += (dic[i] * (dic[i] - 1)) / 2
        if i * 2 in dic:
            answer += dic[i] * dic[i * 2]
        if i * 2 / 3 in dic:
            answer += dic[i] * dic[i * 2 / 3]
        if i * 3 / 4 in dic:
            answer += dic[i] * dic[i * 3 / 4]

    return answer
