#1676 팩토리얼 0의 개수
import sys
import math
N = math.factorial(int(sys.stdin.readline()))
cnt = 0
for i in reversed(str(N)):
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)


# 2등 코드
'''
import sys
N = int(sys.stdin.readline())
print(N//5 + N//25 + N//125)
'''