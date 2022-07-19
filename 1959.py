a = [6, 0, 5, 5, -1, 1, 6]
b = [-4, 1, 8, 7, -9, 3]

if len(a) > len(b):
    a, b = b, a

len_a = len(a)
len_b = len(b)

max_1 = 0
for i in range(len(b)-len((a))):
    a.append(0)

for i in range(len_b -len_a+1):
    len_1 = len(a)
    sum = 0
    for j in range(len_1):
        sum += a[j] * b[j]
    if sum > max_1:
        max_1 = sum
    for k in range(len_1-1, -1, -1):
        a[k] = a[k - 1]
        if k == 0:
            a[k] = 0

print(max_1)