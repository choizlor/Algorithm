def solution(cards):
    visited = [0] * len(cards)
    check = []
    idx = 0

    while sum(visited) != len(cards):
        for i in range(len(visited)):
            if visited[i] == 0:
                idx = i
                break

        total = 0
        while True:
            if not visited[idx]:
                visited[idx] = 1
                idx = cards[idx] - 1
                total += 1
            else:
                check.append(total)
                break

    if len(check) == 1:
        return 0
    else:
        check.sort(reverse=True)
        return check[0] * check[1]


solution([8, 6, 3, 7, 2, 5, 1, 4])
