T = int(input())
for t in range(1, T + 1):
    n = int(input())
    lst = [list(map(int, list(input()))) for _ in range(n)]

    value = n // 2 # 농장을 반으로 나눠서 생각
    sumV = 0

    for i in range(value + 1): # 가운데 줄 까지
        sumV += sum(lst[i][value - i:value + 1 + i])

    for j in range(value): # 그 밑은 거꾸로 가져와서 더하기
        sumV += sum(lst[n - 1 - j][value - j:value + 1 + j])

    print(f'#{t} {sumV}')