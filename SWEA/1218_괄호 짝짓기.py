N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
lst.insert(0, 0)

for i in range(1, N+1):
    lst[i] = lst[i-1]+lst[i]

for _ in range(M):
    a, b = map(int, input().split())
    print(lst[b]-lst[a-1])