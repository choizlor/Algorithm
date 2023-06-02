import sys

input = sys.stdin.readline

message = list(input().rstrip())
key = list(input().rstrip())
code = {}
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']

# 암호 표 만들기
for k in key:
    if k not in code:
        code[k] = 1
for a in alphabet:
    if a not in code:
        code[a] = 1
lst = list(code.keys())
maps = [[0 for _ in range(5)] for _ in range(5)]
for i in range(25):
    maps[i // 5][i % 5] = lst[i]
graph = {}
for idx in range(25):
    graph[lst[idx]] = (idx // 5, idx % 5)

# 메세지 정제
check = []
while True:
    if len(message) == 0:
        break
    elif len(message) == 1:
        check.append([message[0], 'X'])
        break

    if message[0] != message[1]:
        check.append([message[0], message[1]])
        message = message[2:]
    else:
        if message[0] == 'X' and message[1] == 'X':
            check.append([message[0], 'Q'])
            message = message[1:]
        else:
            check.append([message[0], 'X'])
            message = message[1:]

# 암호화
ans = []
for c in check:
    a, b = c
    a_idx = graph[a]
    b_idx = graph[b]

    # 오른쪽으로 한 칸 이동한 칸
    if a_idx[0] == b_idx[0]:
        if a_idx[1] == 4:
            ans.append(maps[a_idx[0]][0])
        elif a_idx[1] < 4:
            ans.append(maps[a_idx[0]][a_idx[1] + 1])
        if b_idx[1] == 4:
            ans.append(maps[b_idx[0]][0])
        elif b_idx[1] < 4:
            ans.append(maps[b_idx[0]][b_idx[1] + 1])

    # 아래쪽으로 한 칸 이동한 칸
    elif a_idx[1] == b_idx[1]:
        if a_idx[0] == 4:
            ans.append(maps[0][a_idx[1]])
        elif a_idx[0] < 4:
            ans.append(maps[a_idx[0] + 1][a_idx[1]])
        if b_idx[0] == 4:
            ans.append(maps[0][b_idx[1]])
        elif b_idx[0] < 4:
            ans.append(maps[b_idx[0] + 1][b_idx[1]])

    # 두 글자가 위치하는 칸의 열이 서로 교환
    else:
        ans.append(maps[a_idx[0]][b_idx[1]])
        ans.append(maps[b_idx[0]][a_idx[1]])

print(''.join(ans))