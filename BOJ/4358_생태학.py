import sys

trees = {}
while True:
    # sys.stdin.readline()을 쓰기 위해서는 rstrip이 필수
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

n = sum(trees.values())
trees = sorted(trees.items())

for key, value in trees:
    print('%s %.4f' %(key, value / n * 100))
