def f(k, midSum):
    global cnt

    if k == n:
        cnt += 1
        return

    if midSum > n:
        return

    f(k+1, midSum+1)
    f(k+2, midSum+2)
    f(k+3, midSum+3)


T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    f(0, 0)
    print(cnt)