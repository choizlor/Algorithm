N, K = map(int, input().split())
board = []
chess = [[[] for _ in range(N)] for _ in range(N)]
horse = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x - 1, y - 1, d - 1])
    chess[x - 1][y - 1].append(i)

cnt = 0

# 벽 or 파란색 만났을 때 방향 바꾸는 함수
def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d


def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]

    # 벽 or 파란색 만났을 때 조건 처리
    if 0 > nx or nx >= N or 0 > ny or ny >= N or board[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= N or 0 > ny or ny >= N or board[nx][ny] == 2:
            return True

    horse_up = []
    # 쌓이면 같이 움직여야되니까 그 처리 먼저 해주기
    for h_idx, h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y] = chess[x][y][:h_idx]
            break

    # 움직인 칸이 빨간색일 때 거꾸로
    if board[nx][ny] == 1:
        horse_up = horse_up[-1::-1]

    # for 문 돌면서 새로운 칸에 값 넣어주기
    for h in horse_up:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)

    # 4 이상이면 게임 끝!
    if len(chess[nx][ny]) >= 4:
        return False
    return True


while True:
    what = False
    if cnt > 1000:
        print(-1)
        break
    for i in range(K):
        if solve(i) == False:
            what = True
            break
    cnt += 1
    if what:
        print(cnt)
        break
