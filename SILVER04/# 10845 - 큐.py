# 10845 큐
from sys import stdin

queue = []
for _ in range(int(stdin.readline())):
    command = stdin.readline().split()
    if command[0] == 'push':
        queue.insert(0, command[1])
    elif command[0] == 'pop':
        if len(queue):
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    else:
        if len(queue):
            print(queue[0])
        else:
            print(-1)


# 1등 코드 - 29056KB/60ms
'''
import sys
t = int(input())
q = []
res = []
L = sys.stdin.read().splitlines()
for idx in range(t):
    a, *b = L[idx].split()
    if "push" in a:
        q.append(b[0])
    elif a == "front":
        res.append(q[0] if q else "-1")
    elif a == "back":
        res.append(q[-1] if q else "-1")
    elif a == "size":
        res.append(str(len(q)))
    elif a == "empty":
        res.append('0' if q else "1")
    elif a == "pop":
        res.append(q.pop(0) if q else "-1")
print("\n".join(res))
'''
