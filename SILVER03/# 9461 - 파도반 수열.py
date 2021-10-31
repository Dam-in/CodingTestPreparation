# 9461 파도반 수열
def dp(N):
    try:
        return DP[N]
    except:
        for x in range(8, N+1):
            try:
                DP[x] = DP[x-1] + DP[x-5]
            except:
                DP.append(DP[x-1] + DP[x-5])
        return DP[N]


import sys
DP = [0, 1, 1, 1, 2, 2, 3, 4]
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    print(dp(N))


# 1부터 100까지 저장하고 출력하기
'''
DP = [0, 1, 1, 1, 2, 2, 3, 4]
for n in range(8, 101):
    DP.append(DP[n-1] + DP[n-5])

import sys
for _ in range(int(sys.stdin.readline())):
    print(DP[int(sys.stdin.readline())])
'''
