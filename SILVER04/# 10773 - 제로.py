#10773 제로
import sys
stack = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x:
        stack.append(x)
    else:
        stack.pop()
print(sum(stack))



# 29980KB/96ms
'''
from sys import stdin
stdin.readline()
l = []
for i in map(int, stdin):
    l.append(i) if i else l.pop()
print(sum(l))
'''