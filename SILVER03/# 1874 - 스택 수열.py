# 1874 스택 수열
import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
max = 0
result = []
for i in data:
    if max < i:
        for x in range(max+1, i):
            stack.append(x)
            result.append('+')
        max = i
        result.append('+')
        result.append('-')
    else:
        if i == stack[-1]:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            exit()
for i in result:
    print(i)
