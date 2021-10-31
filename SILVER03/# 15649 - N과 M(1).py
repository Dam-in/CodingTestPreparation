# 15649 N과 M(1)
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
            del List[-1]
DFS()

'''
N = 4, M = 2인 경우
List : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
'''