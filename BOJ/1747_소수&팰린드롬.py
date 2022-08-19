a = [False, False] + [True] * (1004000-1)
primes = []
for i in range(2, 1004000+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, 1004000+1, i):
            a[j] = False

n = int(input())
for i in primes:
    if i >= n:
        lst = list(str(i))
        if lst[0:len(lst)//2] == lst[::-1][:len(lst)//2]:
            print(i)
            break