def f(n, r):
    global arrList
    arrList.append(n)
    result = []
    ln = len(n)
    while r != 0:
        for a in arrList:
            t = a[:]
            for i in range(ln-1):
                for j in range(i+1, ln):
                    t[i], t[j] = t[j], t[i]
                    if t not in result:
                        result.append(t)
                    t = a[:]
        r -= 1
        arrList = result[:]
        result = []


T = int(input())
for tc in range(1, T+1):
    num, r = map(int, input().split())
    n = []
    for i in str(num):
        n.append(i)
    arrList = []
    f(n, r)

    maxV = 0
    for i in arrList:
        if maxV < int(''.join(i)):
            maxV = int(''.join(i))
    print(f'#{tc} {maxV}')

# # 재귀
# def solve(k):
#     if k==K:
#         최대값인지 확인
#         return
#     for 교환횟수:
#         교환
#         solve(k+1)
#         교환
#
# # 반복문
# for k<K:
#     for a in arrList[k]:
#         교환해서 arrList[K] append

