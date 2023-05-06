def solution(x, y, n):
    answer = 0
    dp = set() # 같은 숫자는 들어오지 않게!
    dp.add(x)

    while dp:
        if y in dp:
            return answer
        else:
            dp_y = set()
            for i in dp:
                if i + n <= y:
                    dp_y.add(i + n)
                if i * 2 <= y:
                    dp_y.add(i * 2)
                if i * 3 <= y:
                    dp_y.add(i * 3)
            dp = dp_y
            answer += 1
    
    return -1
