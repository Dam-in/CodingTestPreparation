#15651 N과 M(3)
'''def DFS():
    if len(List) == M:
        print(' '.join(map(str, List)))
        return
    for i in range(1, N+1):
        List.append(i)
        DFS()
        del List[-1]

import sys
N, M = map(int, sys.stdin.readline().split())
List = []
DFS()'''


# 순열로 구현

import itertools
import sys
N, M = map(int, sys.stdin.readline().split())
List = list(map(str, range(1, N+1)))
print('\n'.join(list(map(" ".join, itertools.product(List, repeat=M)))))
# 입력이 N=4, M=2인 경우
# List = '1', '2', '3', '4'
# product(A, B) == (x, y) for x in A for y in B
# product(A, repeat=4) == product(A, A, A, A)



# 백트래킹
'''
def backtracking(List, cnt):
    if cnt == M:
        print(' '.join(map(str, List)))
        return
    for num in nums:
        backtracking(List+[num], cnt+1)


import sys
N, M = map(int, sys.stdin.readline().split())
for i in range(1, N+1):
    nums = list(i for i in range(1, N+1))
    backtracking([i], 1)
'''
