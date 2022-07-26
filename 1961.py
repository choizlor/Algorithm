def rotate(a, b):
    for i in range(n):
        for j in range(n):
            b[j][n-1-i] = a[i][j]
def lst():
    blank_lst = []
    for _ in range(n):
        blank_lst.append([0] * n)
    return blank_lst

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

d_90 = lst()
d_180 = lst()
d_270 = lst()

rotate(data, d_90)
rotate(d_90, d_180)
rotate(d_180, d_270)

for i in range(n):
    print(''.join(map(str, d_90[i])), end=' ')
    print(''.join(map(str, d_180[i])), end=' ')
    print(''.join(map(str, d_270[i])), end=' ')
    print()

