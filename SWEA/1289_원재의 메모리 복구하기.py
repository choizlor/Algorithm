T = int(input())

for t in range(1, T + 1):
    n = input()
    lst = [int(i) for i in n]

    test = [0] * len(lst) # 초기화 list 값
    count = 0

    for i in range(len(lst)):
        if lst[i] == test[i]:
            continue
        else:
            test[i:] = [lst[i]] * (len(lst)-i)
            count += 1

    print(f'#{t} {count}')