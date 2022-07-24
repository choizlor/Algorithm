num = int(input())
for i in range(1, num+1):
    n = 0
    for j in range(len(str(i))): # 3, 6, 9가 num에 몇 개 들어가는지 세기
        if '3' in str(i)[j]:
            n += 1
        if '6' in str(i)[j]:
            n += 1
        if '9' in str(i)[j]:
            n += 1
    if n > 0:
        print('-' * n, end=' ')
    else:
        print(i, end = ' ')
