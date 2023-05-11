def solution(storey):
    answer = 0

    while storey:
        num = storey % 10   # 10으로 나눴을 때 나머지

        if num > 5:     # 5보다 크면
            answer += (10 - num)    # ex) 10 - 7 = 3
            storey += 10    # 숫자에 10을 더해줌
        elif num < 5:   # 5보다 작으면
            answer += num   # 그냥 더해줌
        else:   # 5면
            if (storey // 10) % 10 > 4:
                storey += 10    # 자릿 값이 바뀐 것이니까 +10
            answer += num
        storey //= 10   # 몫으로 다시 시작.

    return answer


solution(16)
solution(2554)
