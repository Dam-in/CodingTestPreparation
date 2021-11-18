# 11726 2xn타일링
# 동적으로 구현










### math라이브러리로 피보함수 사용 -> 31312, 96
'''
import sys
import math
n = int(sys.stdin.readline())
Sum = 1  # nC0
for i in range(1, n//2+1):
    Sum += math.factorial(n-i) // (math.factorial(n-i-i) * math.factorial(i))
print(Sum % 10007)
'''


### 함수로 피보 구현 -> 29200, 216
'''
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

import sys
n = int(sys.stdin.readline())
Sum = 1  # nC0
for i in range(1, n//2+1):
    Sum += factorial(n-i) // (factorial(n-i-i) * factorial(i))
print(Sum % 10007)
'''


### 반복문으로 구현 -> 29200, 208
'''
import sys
n = int(sys.stdin.readline())
Sum = 1  # nC0
for i in range(1, n//2+1):
    a = 1
    for j in range(n-i, n-i-i, -1):
        a *= j
    for j in range(1, i+1):
        a //= j
    Sum += a
print(Sum % 10007)
'''