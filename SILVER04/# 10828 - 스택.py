#10828 스택
from sys import stdin
stack = []
next(stdin)
for line in stdin:
    command = line.split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


# 72ms
'''
import sys
order = list(sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline())))
stack = []
for odr in order:
    if 'push' in odr:
        Push, X = odr.split(' ')
        stack.append(X)
    elif 'pop' == odr:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' == odr:
        print(len(stack))
    elif 'empty' == odr:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
'''

# 76ms
'''
def push(pushX):
    Push, X = pushX.split(' ')
    stack.append(X)
def pop():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]
def size():
    print(len(stack))
def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

import sys
N = int(sys.stdin.readline())
order = list(sys.stdin.readline().strip() for _ in range(N))
stack = []
for odr in order:
    if 'push' in odr:
        push(odr)
    elif 'pop' == odr:
        pop()
    elif 'size' == odr:
        size()
    elif 'empty' == odr:
        empty()
    else:
        top()
'''