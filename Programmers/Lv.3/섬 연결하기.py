def prim(start, n, tree):
    visited_set = set() # 현재까지 방문한 정점들의 집합
    visited_set.add(start)
    distance = 0

    # n-1개의 간선을 선택할 때까지 반복
    for _ in range(n-1):
        # min_dist: 현재 방문한 정점에서 갈 수 있는 간선의 최단 거리
        # next_node: 현재 방문한 정점에서 최단 거리로 갈 수 있는 정점
        min_dist, next_node = 100000000, -1

        # 현재까지 방문한 모든 정점에 대하여
        for node in visited_set:
            # 해당 정점과 연결되어 있고 아직 방문하지 않은 모든 정점 중
            # 소요 비용이 가장 작은 정점을 찾는다.
            for j in range(n):
                if j not in visited_set and 0 < tree[node][j] < min_dist:
                    min_dist = tree[node][j]
                    next_node = j

        distance += min_dist
        visited_set.add(next_node)

    return distance

def solution(n, costs):
    tree = [[0] * n for _ in range(n)]

    for i in range(len(costs)):
        x, y, value = costs[i][0], costs[i][1], costs[i][2]
        tree[x][y] = value
        tree[y][x] = value

    return prim(0, n, tree)
