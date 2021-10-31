# 2193 이친수
import sys
import math
N = int(sys.stdin.readline())
if N <= 2:
    print(1)
    exit()
else:
    N -= 1
    result = 1
    result += sum(math.factorial(N-r) // (math.factorial(N-r-r) * math.factorial(r)) for r in range(1, N//2+1))
    # for r in range(1, N//2+1):
    #         result += math.factorial(N-r) // (math.factorial(N-r-r) * math.factorial(r))
    print(result)


### 동적 구현
'''
n = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
'''
