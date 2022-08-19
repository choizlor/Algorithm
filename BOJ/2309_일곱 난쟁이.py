arr = []
result = []

for _ in range(9):
    arr.append(int(input()))

for i in range(1<<9):
    lst = []
    sumV = 0

    for j in range(9):
        if i & (1<<j):
            lst.append(arr[j])
            sumV += arr[j]

    if len(lst) == 7 and sumV == 100:
        result = lst

for i in sorted(result):
    print(i)