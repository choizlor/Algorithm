N, M = map(int, input().split())
check = [list(map(int, list(input()))) for _ in range(N)]
result = [list(map(int, list(input()))) for _ in range(N)]
cnt = 0

# 어차피 첫 번째 줄이 틀리면 끝이기 때문에 이렇게 범위 설정함.
# 그리고, 3x3 행렬이므로 같은 곳을 또 바꾼다고 해서 의미가 없음.
for i in range(N-2):
    for j in range(M-2):
        # 밑에 for문으로 바꾼 후에 첫 줄의 다음 숫자 보기, 여기도 틀리면 다시 들어가는 것
        if check[i][j] != result[i][j]:
            for x in range(i, i+3):
                for y in range(j, j+3):
                    check[x][y] = 1 - check[x][y]
            cnt += 1

# 마지막 검사하기
a = 0
for i in range(N):
    for j in range(M):
        if check[i][j] != result[i][j]:
            a = 1

if a == 1:
    print(-1)
else:
    print(cnt)
