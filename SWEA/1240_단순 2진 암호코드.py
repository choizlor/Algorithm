def btod(c):
    pat_lst = ['0001101', '0011001', '0010011', '0111101', '0100011',
               '0110001', '0101111', '0111011', '0110111', '0001011']
    pat = {
        '0001101': 0, '0011001': 1, '0010011': 2,
        '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8,
        '0001011': 9,
    }

    if c in pat_lst:    # 0~9와 다른 입력이 있을 때 처리
        return pat[c]
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = ''
    for _ in range(N):  # 0만 있는 줄은 없애고, 암호문 해석할 첫 줄만 가져오기
        num = input()
        lst = list(map(int, num))
        if max(lst) == 1:
            a = num

    cnt1 = 0    # 앞부분 0 개수
    cnt2 = 0    # 뒷부분 0 개수
    for i in range(len(a)-1, -1, -1):
        if a[i] == '1':
            break
        else:
            cnt2 += 1
    cnt1 = M - cnt2 - 56
    a = a[cnt1:M-cnt2]  # 56개의 암호문

    sumV = 0
    even = 0
    odd = 0
    for i in range(0, len(a), 7):   # 암호문 해석
        if i % 2 == 0:  # 홀수 자릿수 더하기
            odd += btod(a[i:i + 7])
        else:   # 짝수 자릿수 더하기
            even += btod(a[i:i + 7])

        if btod(a[i:i + 7]) == -1:
            sumV = 0
            break
        else:
            sumV += btod(a[i:i + 7])

    if (odd * 3 + even) % 10 == 0 or sumV == 0: # 마지막 검증
        print(f'#{tc} {sumV}')
    else:
        print(f'#{tc} 0')
