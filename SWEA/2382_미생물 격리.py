def move():
    for k in range(len(arr)):
        nx = arr[k][0] + d[arr[k][3]][0]
        ny = arr[k][1] + d[arr[k][3]][1]

        if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
            arr[k][2] //= 2
            arr[k][0] = nx
            arr[k][1] = ny
            if arr[k][3] == 1:  arr[k][3] = 2
            elif arr[k][3] == 2:  arr[k][3] = 1
            elif arr[k][3] == 3:  arr[k][3] = 4
            else:  arr[k][3] = 3

        else:
            arr[k][0] = nx
            arr[k][1] = ny


def s():
    arr.sort(key=lambda x: x[2])
    xyL = [[3,3]]
    for i in range(len(arr)):
        if [arr[i][0], arr[i][1]] not in xyL:
            xyL.append([arr[i][0], arr[i][1]])

    lst = [[0, 0] for _ in range(len(xyL))]
    for k in range(len(xyL)):
        for i in range(len(arr)):
            if xyL[k][0] == arr[i][0] and xyL[k][1] == arr[i][1]:
                lst[k][0] += arr[i][2]
                lst[k][1] = arr[i][3]

    for k in range(len(xyL)):
        xyL[k] += lst[k]

    return xyL


d = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[] for _ in range(K)]
    for k in range(K):
        arr[k] = list(map(int, input().split()))

    for _ in range(M):
        move()
        arr = s()

    sumV = 0
    for k in range(len(arr)):
        sumV += arr[k][2]
    print(f'#{tc} {sumV}')