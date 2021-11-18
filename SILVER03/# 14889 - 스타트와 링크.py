#14889 스타트와 링크
# 초기설계 - 시간초과
import sys
from itertools import combinations
N = int(sys.stdin.readline())
person = list(i for i in range(N))
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Min = N
for startTeam in combinations(person, N//2):
    linkTeam = []
    start, link = 0, 0
    for i in person:
        if i not in startTeam:
            linkTeam.append(i)
    for x, y in combinations(startTeam, 2):
        start += S[x][y]+S[y][x]
    for x, y in combinations(linkTeam, 2):
        link += S[x][y]+S[y][x]
    Min = min(Min, abs(start-link))
print(Min)



# 조합으로 시간초과없이 구현한 코드
'''
from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = list(i for i in range(N))
startTeam = []
for team in list(combinations(members, N//2)):
    startTeam.append(team)
Min = 10000
for i in range(len(startTeam)//2):
    team = startTeam[i]
    start = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            start += S[member][k]
    team = startTeam[-i-1]
    link = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            link += S[member][k]
    Min = min(Min, abs(start-link))
print(Min)
'''


# DFS - 왜 나만 안 돼 ? 코드 다 똑같은데 ? 나만 왜 시간 초과 ? ?
'''
def DFS(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if visited[i]: continue
        visited[i] = 1
        DFS(i+1, cnt+1)
        visited[i] = 0


import sys
sys.setrecursionlimit(100001)   # 재귀의 깊이를 지정해 주어야 에러가 안 뜬다.
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [list(map(int, input().split()))]
visited = [0 for _ in range(n)]
ans = int(1e9)
DFS(0, 0)
print(ans)
'''


# 백트래킹
'''
from copy import deepcopy
import sys
input = sys.stdin.readline
def dif(temp1):
    global result
    temp2 = []
    for i in range(n):
        if i in temp1:
            continue
        temp2.append(i)
    temp1_n = 0
    temp2_n = 0
    for i in range((n // 2) - 1):
        for j in range(i + 1, n // 2):
            a, b = temp1[i], temp1[j]
            c, d = temp2[i], temp2[j]
            temp1_n += s[a][b] + s[b][a]
            temp2_n += s[c][d] + s[d][c]
    result = min(result, abs(temp1_n - temp2_n))
def dfs(temp):
    t = deepcopy(temp)
    if len(t) == n // 2:
        dif(t)
        return
    for i in range(t[-1] + 1, n):
        t.append(i)
        dfs(t)
        t.pop()
n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
result = 1000000000
temp = [0]
dfs(temp)
print(result)
'''