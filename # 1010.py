# 1010 다리 놓기
import sys
for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    # 조합 MCN을 하면 된다.
    result = 1
    if N >= M//2:   # 6C4는 6C2랑 같으니까, 계산 빠르게 하려고
        N = M-N
    for i in range(M, M-N, -1):
        result *= i
    for j in range(1, N+1):
        result /= j
    print(int(result))