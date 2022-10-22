def solve(k, n, lst):
    global minV, result

    if minV <= k:
        return

    if n == 1:
        if minV > k:
            minV = k
            result = lst[:]
        return

    if n % 3 == 0:
        solve(k+1, n//3, lst+[n//3])
    if n % 2 == 0:
        solve(k+1, n//2, lst+[n//2])
    solve(k+1, n-1, lst+[n-1])


n = int(input())
minV = 10000000
result = []
solve(0, n, [n])
print(minV)
print(*result)
