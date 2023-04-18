def solution(n, lost, reserve):
    dp = [1] * (n + 2)

    for i in lost:
        dp[i] -= 1

    for i in reserve:
        dp[i] += 1

    answer = 0
    for i in range(1, n + 1):
        if dp[i] >= 1:
            answer += 1
        else:
            if dp[i-1] == 2:
                dp[i-1] -= 1
                answer += 1
                dp[i] += 1
            elif dp[i+1] == 2:
                dp[i+1] -= 1
                answer += 1
                dp[i] += 1
    
    return answer