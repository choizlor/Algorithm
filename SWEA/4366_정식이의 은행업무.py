# def find():
#     for i in range(N):
#         for j in range(M):
#             binL = list(binS)
#             triL = list(triS)
#             binL[i] = str((int(binL[i] + 1)) % 2)
#             for k in range(1, 3):
#                 triL[j] = str((int(triL[j] + k)) % 3)
#             binV = int(''.join(binL), 2)
#             triV = int(''.join(triL), 3)
#             if binV == triV:
#                 return binV
#     return -1

def find():
    for i in range(N):
        t_binS = binS[:]
        t_binS[i] = str((int(binS[i]) + 1) % 2)
        for j in range(M):
            t_triS = triS[:]
            for k in range(1, 3):
                t_triS[j] = str((int(triS[j]) + k) % 3)

                binV = int(''.join(t_binS), 2)
                triV = int(''.join(t_triS), 3)
                if binV == triV:
                    return binV
    return -1


T = int(input())
for tc in range(1,T+1):
    binS = list(input())
    triS = list(input())
    N = len(binS)
    M = len(triS)
    print(f'#{tc} {find()}')

