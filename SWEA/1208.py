for t in range(10):

    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        lst.sort()
        lst[-1] -= 1 # 최댓값 -1
        lst[0] += 1 # 최솟값 +1

    lst.sort() # for 문을 빠져나와서 sort하기
    result = lst[-1] - lst[0]

    print(f'#{t+1} {result}')