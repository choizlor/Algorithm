def solution(n):
    ans = 0
    while n > 0:
        if n % 2 != 0:
            ans += 1
        n //= 2

    return ans


solution(5)
solution(6)
solution(5000)