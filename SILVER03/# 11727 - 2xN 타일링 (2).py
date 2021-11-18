# 11727 2xN 타일링 (2)
import sys

n = int(sys.stdin.readline())
DP = [0, 1, 3]
for i in range(3, 1001):
    DP.append((DP[i - 2] * 2) + DP[i - 1])
print(DP[n] % 10007)

# 1등 코드  29284KB/52ms
'''
n = int(input())
a = 1
b = 3
for _ in range(n - 1): a, b = b, 2 * a + b
print(a % 10007)
'''