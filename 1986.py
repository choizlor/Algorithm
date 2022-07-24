T = int(input())
for t in range(1, T + 1):
    num = int(input())
    sumV = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            sumV -= i
        else:
            sumV += i
    print(f'#{t} {sumV}')