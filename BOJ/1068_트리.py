N = int(input())
lst = list(map(int, input().split()))
R = int(input())

q = []
q.append(R)
lst[R] = -2
while q:
    d = q.pop(0)
    for i in range(N):
        if d == lst[i]:
            q.append(i)
            lst[i] = -2

cnt = 0
for i in range(N):
    if lst[i] == -2:
        continue
    if i not in lst:
        cnt += 1

print(cnt)

'''
12
1 4 3 -1 3 1 2 0 6 6 6 1
2
'''