p = sorted(list(input()))
odd = []
even = []
result = ['' for _ in range(len(p))]
for i in range(0, len(p), 2):
    odd.append(p[i])
for i in range(1, len(p), 2):
    even.append(p[i])

for i in range(len(even)):
    for j in range(len(odd)):
        if even[i] == odd[j]:
            result[i] = even[i]
            result[len(p)-1-i] = odd[j]
            odd[j] = 0
            break

for i in odd:
    if i != 0:
        result[len(p)//2] = i

if '' in result:
    print("I'm Sorry Hansoo")
else:
    print(''.join(result))