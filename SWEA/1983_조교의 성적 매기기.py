T = int(input())
for t in range(1, T + 1):
    result = ''
    s, num = map(int, input().split())
    test = []
    grade = [''] * s
    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    for i in range(s):
        m, f, a = map(int, input().split())
        score = m * 0.35 + f * 0.45 + a * 0.2
        test.append((i, score))
    sorted_test = sorted(test, key=lambda x: -x[1])

    for i in range(1, 11):
        for j in range(s // 10 * (i-1), s // 10 * i):
            grade[sorted_test[j][0]] = grades[i - 1]

    result = grade[num - 1]
    print(f'#{t} {result}')