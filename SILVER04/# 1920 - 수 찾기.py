# 1920 수 찾기
import sys
N = int(sys.stdin.readline())
A = set(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for num in B:
    if num in A:
        print(1)
    else:
        print(0)


'''def func(num):
    l, r = 0, N-1
    while l<=r:
        m = (r+l)//2
        if A[m] == num:
            return True
        if num < A[m]:
            r = m-1
        elif num > A[m]:
            l = m+1


import sys
N = int(sys.stdin.readline())
A = sorted(set(list(map(int, sys.stdin.readline().split()))))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if func(B[i]):
        print(1)
    else:
        print(0)'''


'''
import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
for num in B:
    l, m, r = 0, N // 2, N - 1
    flag = True
    while l <= r:
        if A[m] == num:
            B[B.index(num)] = 1
            flag = False
            break
        elif A[m] > num:
            r = m - 1
            m = (l + r) // 2
        else:
            l = m + 1
            m = (l + r) // 2
    if flag:
        B[B.index(num)] = 0
for i in B:
    print(i)
'''

