#10866 덱
import sys
Deque = []
for _ in range(int(sys.stdin.readline())):
    a, *b = sys.stdin.readline().split()
    if a == 'push_front':
        Deque.insert(0, b[0])
    elif a == 'push_back':
        Deque.append(b[0])
    elif a == 'pop_front':
        if len(Deque):
            print(Deque[0])
            del Deque[0]
        else:
            print(-1)
    elif a == 'pop_back':
        if len(Deque):
            print(Deque[-1])
            del Deque[-1]
        else:
            print(-1)
    elif a == 'size':
        print(len(Deque))
    elif a == 'empty':
        if len(Deque):
            print(0)
        else:
            print(1)
    elif a == 'front':
        if len(Deque):
            print(Deque[0])
        else:
            print(-1)
    else:
        if len(Deque):
            print(Deque[-1])
        else:
            print(-1)