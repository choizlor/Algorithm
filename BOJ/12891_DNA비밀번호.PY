import sys
input = sys.stdin.readline

P, S = map(int, input().split())
arr = input()
A, C, G, T = map(int, input().split())
result = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
cnt = 0

for i in range(0, P-S+1):
    if i == 0:
        for j in arr[i:S]:
            result[j] += 1
    else:
        result[arr[i-1]] -= 1
        result[arr[S+i-1]] += 1

    if result['A'] >= A and result['C'] >= C and result['G'] >= G and result['T'] >= T:
        cnt += 1

print(cnt)