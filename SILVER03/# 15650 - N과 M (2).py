# 15650 N과 M(2)
import sys
N, M = map(int, sys.stdin.readline().split())
List = []
def DFS(start):
    if len(List) == M:
        print(' '.join(map(str, List)))
        return
    for i in range(start, N+1):
        if i not in List:
            List.append(i)
            DFS(i+1)
            del List[-1]
DFS(1)


