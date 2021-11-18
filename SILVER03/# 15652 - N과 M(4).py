#15652 N과 M(4)
def DFS(start):
    if len(List) == M:
        print(' '.join(map(str, List)))
        return
    for i in range(start, N+1):
        List.append(i)
        DFS(i)
        del List[-1]


import sys
N, M = map(int, sys.stdin.readline().split())
List = []
DFS(1)


# 순열을 이용한 구현
'''
import sys
from itertools import combinations_with_replacement
N, M = map(int, sys.stdin.readline().split())
print('\n'.join(map(' '.join, combinations_with_replacement(map(str, range(1, N+1)), M))))
'''