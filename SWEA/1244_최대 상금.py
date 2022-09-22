# def f(n, r):
#     global arrList
#     arrList.append(n)
#     result = []
#     ln = len(n)
#     while r != 0:
#         for a in arrList:
#             t = a[:]
#             for i in range(ln-1):
#                 for j in range(i+1, ln):
#                     t[i], t[j] = t[j], t[i]
#                     if t not in result:
#                         result.append(t)
#                     t = a[:]
#         r -= 1
#         arrList = result[:]
#         result = []
#
#
# T = int(input())
# for tc in range(1, T+1):
#     num, r = map(int, input().split())
#     n = []
#     for i in str(num):
#         n.append(i)
#     arrList = []
#     f(n, r)
#
#     maxV = 0
#     for i in arrList:
#         if maxV < int(''.join(i)):
#             maxV = int(''.join(i))
#     print(f'#{tc} {maxV}')

# 재귀
def solve(k, card):
    global maxV, arrList
    if k == N:
        if maxV < card:
            maxV = card
        return

    if card in arrList[k]:
        return
    else:
        arrList[k].append(card)

    #NC2
    card = list(str(card))
    K = len(card)
    for i in range(K-1):
        for j in range(i+1, K):
            card[i], card[j] = card[j], card[i]
            solve(k+1, int(''.join(card)))
            card[i], card[j] = card[j], card[i]


TC = int(input())
for tc in range(1, TC+1):
    CARD, N = map(int, input().split())
    maxV = 0
    arrList = [[] for _ in range(N)]
    solve(0, CARD)
    print(f'#{tc} {maxV}')
