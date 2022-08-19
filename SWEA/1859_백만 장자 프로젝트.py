# 백만장자 프로젝트

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
 
    price = list(map(int, input().split()))
    price = price[::-1]
    maxV = price[0]
    result = 0
 
    for i in range(n):
        if maxV < price[i]:
            maxV = price[i]
        else:
            result += maxV - price[i]
 
    print(f'#{t} {result}')