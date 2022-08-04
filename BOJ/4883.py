# 백준 4883

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

sumV = lst[0][1] + lst[n-1][1] # 가장 위에 값이랑 밑에 값 미리 더해주기
y = 1 # 초기 y값
minV = 0
for i in range(1, n - 1): # 맨 위랑 맨 아래 제외한 나머지 최소거리값 구하기
    if y == 0 or y == 1: # y가 0 or 1일때 min 값 임의 지정
        minV = lst[i][0]
    else: # y가 2일때 min값 임의 지정
        minV = lst[i][1]
    for j in range(3): # 한 줄에 세 개인 값 중 최소값
        if y == 0:
            if j < 2:
                if lst[i][j] <= minV:
                    minV = lst[i][j]
                    z = j
        elif y == 1:
            if lst[i][j] <= minV:
                minV = lst[i][j]
                z = j
        else:
            if j > 0:
                if lst[i][j] <= minV:
                    minV = lst[i][j]
                    z = j
    y = z # y 위치 받아오기
    sumV += minV

print(sumV)
