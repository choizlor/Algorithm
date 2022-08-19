#백준 6588
a = [False,False] + [True]*(1000000-1)
primes = []
for i in range(2, 1000000+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, 1000000+1, i):
            a[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    # 합 구하기
    test = True
    for i in primes:
        for j in primes:
            if i + j == n:
                test = False
                print(f'{n} = {i} + {j}')
                break
        if test == False:
            break