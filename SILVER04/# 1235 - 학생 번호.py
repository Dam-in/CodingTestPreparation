# 1235 학생번호
import sys
N = int(sys.stdin.readline())
num = [sys.stdin.readline().strip() for _ in range(N)]
l = len(num[0])
for i in range(l-1, -1, -1):
    s = set()
    for x in num:
        a = x[i:]
        s.add(a)
    if len(s) == N:
        print(len(a))
        break
