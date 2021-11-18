'''
# 백트레킹 : 해를 찾아가는 도중, 지금의 경로에 해가 없을 것 같으면, 그 경로를 더이상 가지 않고 되돌아가는 것
DFS 기반
'''


# 백트래킹 - 15649번[N과 M (1)]
############인터넷 참조
import sys
N, M = map(int, sys.stdin.readline().split())
List = []
def DFS():
    if len(List) == M:
        print(' '.join(map(str, List)))
        return
    for i in range(1, N+1):
        if i not in List:
            List.append(i)
            DFS()
            List.pop()
DFS()


# 백트래킹 - 15650번[N과 M (2)]
N, M = map(int, input().split())
List = []
def DFS(n):
    if len(List) == M:
        print(' '.join(map(str, List)))
        return
    for i in range(n, N+1):
        if i not in List:
            List.append(i)
            DFS(i+1)
            List.pop()
DFS(1)


