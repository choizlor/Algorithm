N = int(input())
check = list(map(int, list(input())))
result = list(map(int, list(input())))
cnt = 0

for i in range(N):
        if check[i] != result[i]:
            if i == 0:
                check[i] = 1 - check[i]
                check[i+1] = 1 - check[i+1]
            elif i == N-1:
                check[i-1] = 1 - check[i-1]
                check[i] = 1 - check[i]
            else:
                check[i-1] = 1 - check[i-1]
                check[i] = 1 - check[i]
                check[i + 1] = 1 - check[i + 1]
            for x in range(i, i+3):
                check[x] = 1 - check[x]
