#11653 소인수분해
import sys
N = int(sys.stdin.readline())
i = 2
r = int(N**0.5)
while i <= r:
    while not N % i:
        print(i)
        N //= i
    i += 1
if N > 1:
    print(N)


# 첫 코드 29200KB/1632ms
'''
import sys
N = int(sys.stdin.readline())
i = 2
while N != 1:
    if N % i == 0:
        N = N/i
        print(i)
    else:
        i += 1
'''