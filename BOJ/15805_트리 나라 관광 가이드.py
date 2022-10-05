N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
result = [-1] * (M+1)

for i in range(N-1):
    if result[lst[i+1]] == -1:
        result[lst[i+1]] = lst[i]

result[lst[0]] = -1
print(M+1)
print(*result)
