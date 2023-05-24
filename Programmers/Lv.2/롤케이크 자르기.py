def solution(topping):
    answer = 0
    
    # topping을 미리 dictionary에 쌓기
    dic = {}
    for t in topping:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    
    bro_set = set()
    
    # topping을 돌면서 비교하는 것, 먼저 왼쪽에서 다 먹는다는 느낌 ~
    for t in topping:
        dic[t] -= 1
        bro_set.add(t)
        if dic[t] == 0:
            del dic[t]
        if len(dic) == len(bro_set):
            answer += 1
    
    return answer