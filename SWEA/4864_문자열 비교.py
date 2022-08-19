# 문자열 비교

tc = int(input())
for t in range(1, tc + 1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        result = 1
    else:
        result = 0

    print(f'#{t} {result}')