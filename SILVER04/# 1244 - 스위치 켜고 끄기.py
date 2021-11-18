# 1244 스위치 켜고 끄기
def male(state, num):
    global N
    for i in range(1, N+1):
        if i % num == 0:
            state[i] = switch[state[i]]


def female(state, num):
    global N
    x = 0
    for i in range(1, min(N-num+1, num)):
        a = num - i
        b = num + i
        x = i
        if state[a] != state[b]:
            x = i-1
            break
    state[num] = (state[num]+1)%2
    for i in range(x+1):
            state[num-i] = switch[state[num-i]]
            state[num+i] = switch[state[num+i]]


import sys
N = int(sys.stdin.readline())
state = list(map(int, sys.stdin.readline().split(' ')))
state.insert(0, 0)
switch = {0: 1, 1: 0}
for _ in range(int(sys.stdin.readline())):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1:
        male(state, num)
    if gender == 2:
        female(state, num)
for i in range(1, N+1):
    print(state[i], end=' ')
    if i % 20 == 0:
        print()


'''
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [0] + list(map(int, input().split()))
s_n = int(input())

switch = {0:1, 1:0}

for _ in range(s_n):
    g, num = map(int, input().split())
    if g == 1:
        for i in range(num, n+1, num):
            a[i] = switch[a[i]]
    else:
        a[num] = switch[a[num]]
        i = 1
        while (num - i >= 1) and (num + i <= n) and (a[num - i] == a[num + i]):
            a[num-i], a[num+i] = switch[a[num-i]], switch[a[num+i]]
            i+=1

for idx, el in enumerate(a[1:], start = 1):
    print(el, end=" ")
    if not idx % 20:
        print()
'''