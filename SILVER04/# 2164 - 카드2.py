#2164 카드2
import sys
import math
N = int(sys.stdin.readline())
if N == 1:
    print(1)
    exit()
if math.log2(N) != int(math.log2(N)):
    M = (2**int(math.log2(N)))*2
else:
    M = N
List = [2*i for i in range(1, M//2+1)]
print(List[N%(M//2)-1])


# 1등 코드
'''
import sys
N = int(sys.stdin.readline())
n = 1
while True:
    if n*2 > N:
        break
    else:
        n *= 2
if N == n:
    print(n)
else:
    print(N - (n - (N-n)))
'''