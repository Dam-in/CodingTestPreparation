# 1244 스위치 켜고 끄기
def male(state, num):
    global N
    for i in range(1, N+1):
        if i % num == 0:
            state[i] = (state[i]+1)%2


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
            state[num-i] = (state[num-i]+1)%2
            state[num+i] = (state[num+i]+1)%2


import sys
N = int(sys.stdin.readline())
state = list(map(int, sys.stdin.readline().split(' ')))
state.insert(0, 0)
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
8
0 1 0 1 0 0 0 1
2
1 3
2 3
 < 0 1 1 1 0 1 0 1 >
-> 1 0 0 0 1 1 0 1 

10
1 1 1 1 1 0 1 0 0 1
4
1 4
2 6
1 3
2 3
-> 1 1 1 0 0 0 0 1 1 1 

5
0 0 0 1 0
1
2 1
-> 1 0 0 1 0

25
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1
1 1
-> 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
1 0 1 0 1 
'''
