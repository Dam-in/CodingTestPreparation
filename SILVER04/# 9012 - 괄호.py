#9012 괄호
import sys
for _ in range(int(sys.stdin.readline())):
    stack = 0
    List = sys.stdin.readline().strip()
    flag = True
    for i in List:
        if i == '(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                flag = False
    if not flag or stack > 0:
        print('NO')
    else:
        print('YES')
