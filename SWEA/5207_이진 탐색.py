def binary_s(n, S, key):
    global flag, cnt
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if S[mid] == key:
            cnt += 1
            return

        elif S[mid] > key:  # 왼쪽
            right = mid - 1
            if flag <= 0:
                flag = 1
            else:
                return

        elif S[mid] < key:   # 오른쪽
            left = mid + 1
            if flag >= 0:
                flag = -1
            else:
                return
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    A = sorted(A)
    for key in B:
        flag = 0
        binary_s(N, A, key)

    print(f'#{tc} {cnt}')


