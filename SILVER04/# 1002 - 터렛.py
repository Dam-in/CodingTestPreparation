# 1002 터렛
import sys
for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2 + (y1-y2)**2) ** .5
    add = r1 + r2
    sub = max(r1-r2, r2-r1)
    if d == 0 and r1 == r2:
        print(-1)
    elif sub < d < add:
        print(2)
    elif d == add or d == sub:
        print(1)
    else:
        print(0)



# 함수로 구현
'''
import sys
def func(x1, y1, r1, x2, y2, r2):
    d = ((x1-x2)**2 + (y1-y2)**2) ** .5
    if r1 > r2:
        tmp = r1
        r1 = r2
        r2 = tmp
    if d == 0 and r1 == r2:
        return -1
    elif d == r1+r2 or d == r2-r1:
        return 1
    elif d < r2 - r1 or d > r1 + r2:
        return 0
    else:
        return 2

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    print(func(x1, y1, r1, x2, y2, r2))
'''
