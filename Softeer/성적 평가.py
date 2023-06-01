import sys
input = sys.stdin.readline


def solve(tmp):
    dic = {}
    answer = []
    stmp = sorted(tmp, reverse=True)
    for idx, t in enumerate(stmp):
        if t not in dic:
            dic[t] = idx + 1
    for t in tmp:
        answer.append(dic[t])
    return answer


N = int(input())
grade = []
total = [0] * N
for i in range(3):
    tmp = list(map(int, input().split()))
    for idx in range(N):
        total[idx] += tmp[idx]
    print(*solve(tmp))

print(*solve(total))
