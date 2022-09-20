def ctob(num):
    result = ''
    num = num * 2
    while num != 1:
        if num > 1:
            result += '1'
            num -= 1
        else:
            result += '0'
        num = num * 2
    if len(result) >= 12:
        return 'overflow'
    else:
        return result+'1'


T = int(input())
for tc in range(1, T+1):
    num = float(input())
    print(f'#{tc} {ctob(num)}')

