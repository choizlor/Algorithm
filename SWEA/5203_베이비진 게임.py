def check(lst):
    lst.sort()
    for i in range(len(lst)):
        if lst.count(lst[i]) == 3:
            return True

    lst = list(set(lst))
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1]-1 and lst[i+1] == lst[i+2]-1:
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0
    for k in range(12):
        if k % 2 == 0:
            p1.append(card[k])
        else:
            p2.append(card[k])

    for i in range(3, 7):
        if check(p1[:i]):
            winner = 1
            break
        if check(p2[:i]):
            winner = 2
            break

    print(f'#{tc} {winner}')

