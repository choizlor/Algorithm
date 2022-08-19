tc = int(input())

for t in range(1, tc+1):
    N, M, K = map(int, input().split())
    guest = sorted(list(map(int, input().split())))

    res = 'Possible'

    for i in range(len(guest)):
        if guest[i] // M * K >= i + 1:
            continue
        else:
            res = 'Impossible'
            break

    print(f'#{t} {res}')