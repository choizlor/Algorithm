for _ in range(1, 11):
    n = int(input())
    lst = [input() for _ in range(100)]
 
    for i in range(100):
        lst.append([])
        for j in range(100):
            lst[100 + i] += lst[j][i]
 
    maxV = 0
 
    for i in lst:
        for j in range(99):
            for k in range(99-j):
                check = i[j:100-k]
                if check == check[::-1]:
                    if maxV < len(check):
                        maxV = len(check)
                        break
  
    print(f'#{n} {maxV}')