for t in range(1,11):
    N = int(input())
    lst = list(input().split())
    M = int(input())
    test = list(input().split())

    for i in range(len(test)):
        if test[i] == 'I':
            a = int(test[i + 1])
            b = int(test[i + 2])
            for j in range(b):
                lst.insert(a+j, test[i+j+3])

    result = ' '.join(lst[:10])
    print(f'#{t} {result}')