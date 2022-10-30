import copy

N = int(input())
check = list(map(int, list(input())))
result = list(map(int, list(input())))

lst1 = copy.deepcopy(check)
lst2 = copy.deepcopy(check)

for j in range(2):
    if j == 0:
        check = lst1
    else:
        check = lst2

    cnt = 0
    for i in range(N):
        if i == 0 and j == 0 and check != result:
            check[i] = 1 - check[i]
            check[i+1] = 1 - check[i+1]
            cnt += 1

        elif i == N-1 and check[i-1] != result[i-1]:
            check[i-1] = 1 - check[i-1]
            check[i] = 1 - check[i]
            cnt += 1

        elif 1 <= i <= N-2 and check[i-1] != result[i-1]:
            check[i-1] = 1 - check[i-1]
            check[i] = 1 - check[i]
            check[i + 1] = 1 - check[i + 1]
            cnt += 1

    if check == result:
        print(cnt)
        break

if check != result:
    print(-1)

'''
7
1101000
1111111
'''