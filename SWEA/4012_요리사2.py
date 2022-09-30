# def combi(k, s):
#     global minV
#     if k == N//2:
#         t = abs(calc(aList) - calc(bList))
#         if minV > t:
#             minV = t
#         return
#
#     for i in range(s, N-r+k):
#         aList[k] = i
#         combi(k+1, i+1)

def rec(k, aList, bList):
    if k==N:
        if len(aList) == len(bList):
            print(aList, bList)

        return

    rec(k+1, aList+[k], bList)
    rec(k+1, aList, bList+[k])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ing = [list(map(int, input().split())) for _ in range(N)]
    rec(0,[],[])