N = int(input())

a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

sumV = 0
for i in range(N):
    sumV += min(a_lst) * max(b_lst)
    a_lst.pop(a_lst.index(min(a_lst)))
    b_lst.pop(b_lst.index(max(b_lst)))

print(sumV)