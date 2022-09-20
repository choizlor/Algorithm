# def htoc(c):
#     pat = {
#         '0': '0000', '1': '0001', '2': '0010', '3': '0011',
#         '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#         'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
#     }
#     return pat[c]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, num = input().split()
#     result = ''
#     for c in num:
#         result += htoc(c)
#
#     print(f'#{tc} {result}')


def htob(arr):
    answer = ''
    for i in arr:
        if i.isdecimal():
            intC = int(i)
        else:
            intC = ord(i) - ord('A') + 10

        result = ''
        for i in range(4):
            result = str(intC % 2) + result
            intC //= 2
        answer += result

    return answer


for tc in range(1, int(input()) + 1):
    n, arr = input().split()
    print(f'#{tc} {htob(arr)}')