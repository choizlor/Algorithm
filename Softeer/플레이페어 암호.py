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
graph = [[0 for _ in range(5)] for _ in range(5)]
for i in range(25):
    graph[i // 5][i % 5] = lst[i]

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


print(check)
