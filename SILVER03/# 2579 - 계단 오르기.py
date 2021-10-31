# 2579 계단 오르기
import sys
n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]
DP = list()
if n < 3:
    print(sum(stair))
    exit()
DP.append(stair[0])
DP.append(stair[0]+stair[1])
DP.append(max(stair[0]+stair[2], stair[1]+stair[2]))
for i in range(3, n):
    DP.append(max(DP[i-2]+stair[i], DP[i-3]+stair[i]+stair[i-1]))
print(DP[-1])

