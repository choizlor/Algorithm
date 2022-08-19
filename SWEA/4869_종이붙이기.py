def paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return paper(n-10) + 2 * paper(n-20)


tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    print(f'#{t} {paper(n)}')