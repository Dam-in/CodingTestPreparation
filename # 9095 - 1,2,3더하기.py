# 9095 1,2,3 더하기
import sys
DP = [0, 1, 2, 4]
for i in range(4, 12):
    DP.append(DP[i - 1] + DP[i - 2] + DP[i - 3])
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(DP[n])
