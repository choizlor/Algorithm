def solution(people, limit):
    answer = 0
    lst = sorted(people)
    a = 0
    b = len(people) - 1
    while a < b:
        if lst[a] + lst[b] <= limit:
            answer += 1
            a += 1
        b -= 1
    return len(lst) - answer
