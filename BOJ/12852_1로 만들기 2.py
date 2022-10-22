def solve(k, n, lst):
    global minV,

    if n == 1:
        if minV > k:
            minV = k
        return

    if n % 3 == 0:
        solve(k+1, n//3, lst+[n//3])
    elif n % 2 == 0:
        solve(k+1, n//2, lst+[n//2])
    solve(k+1, n-1, lst+[n-1])


n = int(input())
minV = 100000
lst_a = [n]
solve(0, n, lst)
print(lst)
print(minV)