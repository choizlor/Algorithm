dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ddx = [-1, 1, 1, -1]
ddy = [-1, -1, 1, 1]


def solution(places):
    answer = []
    for n in range(5):
        check = False
        for x in range(5):
            for y in range(5):
                if places[n][x][y] == 'P':
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < 5 and 0 <= ny < 5 and places[n][nx][ny] == 'P':
                            check = True
                            answer.append(0)
                            break

                        if 0 <= nx < 5 and 0 <= ny < 5 and places[n][nx][ny] == 'O':
                            nxx = nx + dx[i]
                            nyy = ny + dy[i]
                            if 0 <= nxx < 5 and 0 <= nyy < 5 and places[n][nxx][nyy] == 'P':
                                check = True
                                answer.append(0)
                                break

                        # 대각선이 P일 때
                        ndx = x + ddx[i]
                        ndy = y + ddy[i]
                        if 0 <= ndx < 5 and 0 <= ndy < 5 and places[n][ndx][ndy] == 'P':
                            for k in range(2):
                                cx = x + dx[(k + i) % 4]
                                cy = y + dy[(k + i) % 4]
                                if 0 <= cx < 5 and 0 <= cy < 5 and places[n][cx][cy] == 'O':
                                    check = True
                                    answer.append(0)
                                    break
                        if check:
                            break
                if check:
                    break
            if check:
                break
        if not check:
            answer.append(1)

    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"]])
