def omok():
    global result
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for di, dj in [[1,0],[0,1],[1,1],[1,-1]]:
                    ni = i + di
                    nj = j + dj
                    cnt = 1

                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                        ni += di
                        nj += dj
                        cnt += 1

                    if cnt >= 5:
                        result = 'YES'


tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 'NO'

    omok()
    print(f'#{t} {result}')