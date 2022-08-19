T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [i for i in range(1, 13)]
    
    cnt = 0

    for i in range(1<<12):
        lst = []
        sumV = 0
        
        for j in range(12):
            if i & (1<<j):
                lst.append(arr[j])
                sumV += arr[j]
                
        if len(lst) == n and sumV == m:
            cnt += 1
            
    print(f'#{t} {cnt}')