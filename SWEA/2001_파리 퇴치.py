N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
maxV = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        sumV = 0
        for k in range(M):
            for l in range(M):
                sumV += lst[i+k][j+l]
        if sumV > maxV:
            maxV = sumV
print(f'답: {maxV}')