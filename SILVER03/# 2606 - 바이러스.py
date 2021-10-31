# 2606 바이러스
import sys

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
# 인접 행렬로 그래프 만들기
adj = [[0 for _ in range(node + 1)] for _ in range(node + 1)]
for _ in range(edge):
    x, y = map(int, sys.stdin.readline().split())
    adj[x][y] = y
    adj[y][x] = x


# BFS로 그래프 탐색 알고리즘
def BFS(graph, s):
    visit = []
    queue = [s]
    while queue:
        node = queue.pop(0)
        if node == 0:
            continue
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit


print(len(BFS(adj, 1)) - 1)
