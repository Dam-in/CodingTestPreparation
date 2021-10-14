# 1463 1로 만들기
# 37448KB / 660ms
'''
import sys
N = int(sys.stdin.readline())
DP = [False for _ in range(N+1)]
DP[0], DP[1] = 0, 0
for x in range(2, N+1):
    DP[x] = DP[x-1] + 1
    if x % 3 == 0:
        DP[x] = min(DP[x//3] + 1, DP[x])
    if x % 2 == 0:
        DP[x] = min(DP[x//2] + 1, DP[x])
print(DP[N])
'''


# 37448KB / 876ms
'''
import sys
N = int(sys.stdin.readline())
DP = [False for _ in range(N+1)]
DP[1] = 0
for x in range(2, N+1):
    a, b, c = x, x, x
    if x % 3 == 0:
        a = DP[x//3]
    if x % 2 == 0:
        b = DP[x//2]
    c = DP[x-1]
    DP[x] = min(a, b, c) + 1
print(DP[N])
'''


# 딕셔너리로 구현 -> 29200KB, 64ms
import sys
N = int(sys.stdin.readline())
cache = {1: 0, 2: 1}

def dp(n):
    if n in cache:
        return cache[n]
    cache[n] = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    return cache[n]

print(dp(N))



# 1995부터 제귀호출이 너무 많이 일어나서 런타임 에러 -> 아마 재귀 1000번 넘었나봄
'''
def func(x):
    if DP[x] is False:
        a, b, c = x, x, x
        if x % 3 == 0:
            if DP[x//3] is False:
                a = func(x//3)
            else:
                a = DP[x//3]
        if x % 2 == 0:
            if DP[x//2] is False:
                b = func(x // 2)
            else:
                b = DP[x//2]
        if DP[x-1] is False:
            c = func(x-1)
        else:
            c = DP[x-1]
        DP[x] = min(a, b, c) + 1
    return DP[x]


import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
DP = [False for _ in range(N+1)]
DP[1] = 0
func(N)
print(DP[N])
'''



# 29200KB, 76ms
'''
def cal_to1(x):
    L =[]
    for i in x:
        L.append(i-1)
        if i%2 ==0:
            L.append(i/2)
        if i%3 ==0:
            L.append(i/3)
    return list(set(L))


N = int(input())
cnt = 0
res =[N]

while True:
    if N == 1:
        break
    res = cal_to1(res)
    cnt += 1
    if min(res) == 1:
        break

print(cnt)
'''