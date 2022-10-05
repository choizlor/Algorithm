n = int(input())
m = int(input())

G = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)

friend = []
friend += G[1]

for i in G[1]:
    friend += G[i]

if 1 in friend:
    print(len(set(friend))-1)
else:
    print(len(set(friend)))

