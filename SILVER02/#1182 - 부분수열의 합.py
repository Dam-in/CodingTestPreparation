#1182 부분수열의 합
## 내장함수를 이용한 조합
import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(1, N+1):
    d = list(combinations(data, i))
    for i in d:
        if S == sum(i):
            cnt += 1
print(cnt)

## DFS를 이용한 조합
def DFS(idx, list):
    if len(list) == r:
        answer.append(list[:])
        return

    for i in range(idx, N):
        DFS(i+1, list+[data[i]])


import sys
N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
answer = []
cnt = 0
for i in range(1, N+1):
    r = i
    DFS(0, [])
for i in answer:
    if S == sum(i):
        cnt += 1
print(cnt)

## DFS로 구현 - 다른 사람 코드 약간 참고함.
def function(cur, t):
    global cnt
    if N == cur:
        if t == S:
            cnt += 1
        return
    function(cur+1, t)
    function(cur+1, t+data[cur])


import sys
N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0
function(0, 0)
if S == 0:
    cnt -= 1
print(cnt)