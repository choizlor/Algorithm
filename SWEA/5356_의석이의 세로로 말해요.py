# 의석이의 세로로 말해요

tc = int(input())
for t in range(1, tc+1):
    lst = [input() for _ in range(5)]
    result = ''
    maxV = 0

    for i in range(5):
        if maxV < len(lst[i]):
            maxV = len(lst[i])

    for i in range(maxV):
        for j in range(5):
            
            if len(lst[j]) < maxV:
                
                if i >= len(lst[j]):
                    continue
                else:
                    result += lst[j][i]
                    
            else:
                result += lst[j][i]
                
    print(f'#{t} {result}')