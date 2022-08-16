# 글자수

tc = int(input())
for t in range(1, tc + 1):
    str1 = [i for i in input()]
    str2 = [j for j in input()]

    test = {}
    maxV = 0

    for i in str2:
        test[i] = 0
    for j in str2:
        test[j] += 1

    for i in str1:
        if int(test.get(i)) > maxV:
            maxV = int(test.get(i))

    print(f'#{t} {maxV}')