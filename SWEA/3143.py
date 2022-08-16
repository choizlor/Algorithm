# 가장 빠른 문자열 타이핑

tc = int(input())
for t in range(1, tc + 1):
 
    strA, strB = input().split()
    cnt = 0
    i = 0
 
    while i < len(strA):
        result = 0
 
        if strB[0] == strA[i] and i + len(strB) <= len(strA):
            for j in range(1, len(strB)):
                if strB[j] == strA[i+j]:
                    result = 1
                else:
                    result = 0
                    break
 
        if result == 1:
            i += len(strB)
        else:
            i += 1
 
        cnt += 1
 
    print(f'#{t} {cnt}')