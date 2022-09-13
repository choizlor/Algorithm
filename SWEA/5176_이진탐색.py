def binary(n):
    global num
    if n <= N:
        binary(n*2)
        tree[n] = num
        num += 1
        binary(n*2 + 1)

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    binary(1)
    print(f'#{t} {tree[1]} {tree[N//2]}')
