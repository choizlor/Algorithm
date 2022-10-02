N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# bfs 돌리고, 치킨집까지의 거리 min/좌표 구하고, 그 minV 보다 크면 return 해버리기
# 좌표랑 최솟값 같이 들어있는 list를 보고 분석.