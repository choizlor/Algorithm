N = int(input())
grade = [int(input()) for _ in range(N)]
grade.sort()
check = [i for i in range(1, N+1)]
sumV = 0
for i in range(N):
    sumV += abs(grade[i] - check[i])
print(sumV)