# 1049 기타줄
import sys
N, M = map(int, sys.stdin.readline().split())
result = 0
six, one = list(), list()
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    six.append(x)
    one.append(y)
a = min(six)
b = min(one)
while N > 0:
    if N >= 6:
        result += min(a, b*6)
        N -= 6
    else:
        result += min(a, b*N)
        N -= N
print(result)