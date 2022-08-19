# 쇠막대기 자르기

tc = int(input())
for t in range(1, tc + 1):
    lst = input().replace('()', '#')
    result = 0
    pipe = 0

    for i in lst:
        if i == '(':
            pipe += 1

        elif i == '#':
            result += pipe

        else:
            pipe -= 1
            result += 1

    print(f'#{t} {result}')