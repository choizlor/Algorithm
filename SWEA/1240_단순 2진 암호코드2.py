pat_lst = {
        '0001101': 0, '0011001': 1, '0010011': 2,
        '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pat = ''
    for _ in range(N):
        row = input()
        if row != '0' * M:  # 유효한 줄만 체크
            pat = row.rstrip('0')[-56:] # 뒤에서부터 0 제거하고, 56개만 검사
            cnt = [0, 0]    # 홀수, 짝수 자리 검사 리스트
            for i in range(1, 9):
                cnt[i % 2 ^ 1] += pat_lst[pat[7 * (i - 1):7 * i]]   # 홀수일 때, 짝수일 때 나눠서 값 저장
    print(f'#{tc}', end=' ')
    if (cnt[0] * 3 + cnt[1]) % 10:
        print(0)
    else:
        print(sum(cnt))