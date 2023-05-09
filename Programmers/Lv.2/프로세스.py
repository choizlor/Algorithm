def solution(priorities, location):
    queue = [(idx, p) for idx, p in enumerate(priorities)]
    answer = 0
    while True:
        tmp = queue.pop(0)
        if any(tmp[1] < q[1] for q in queue):   # 하나라도 조건에 맞으면 True
            queue.append(tmp)
        else:
            answer += 1
            if tmp[0] == location:
                return answer