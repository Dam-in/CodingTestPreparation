# 1654 랜선 자르기
import sys
K, N = map(int, sys.stdin.readline().split())
List = list(int(sys.stdin.readline()) for _ in range(K))
l, r = 0, 10000000000
while l <= r:
    m = (l + r) // 2
    cnt = sum([x//m for x in List])
    if cnt >= N:
        l = m + 1
    else:
        r = m - 1
print(r)



'''
import sys
K, N = map(int, sys.stdin.readline().split())
List = list(int(sys.stdin.readline()) for _ in range(K))
l, r = 1, sum(List)//N
while l <= r:
    m = (l + r) // 2
    cnt = sum([x//m for x in List])
    if cnt < N:
        r = m - 1
    else:
        l = m + 1
        result = m
print(result)
'''