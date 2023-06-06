from collections import deque

T = int(input())

for _ in range(T):
    p = list(input())
    n = int(input())
    arr = input()
    arr = arr.replace('[', '').replace(']', '')
    lst = []

    if arr:
        lst = deque(list(arr.split(',')))

    cnt = 0  # R 개수가 몇 개인지
    total = 0
    answer = ''

    for i in p:
        if i == 'R':
            cnt += 1
        else:
            if not lst:
                answer = 'error'
                break
            if cnt % 2 == 0:
                lst.popleft()
            else:
                lst.pop()

    if answer != 'error':
        if cnt % 2 == 1:
            lst.reverse()
        answer = '[' + ','.join(lst) + ']'
    print(answer)
