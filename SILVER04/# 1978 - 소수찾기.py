# 1978 소수찾기
def sosu(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


import sys
sys.stdin.readline()
List = list(map(int, sys.stdin.readline().split()))
count = 0
for i in List:
    if sosu(i):
        count += 1
print(count)


# 저번에 풀었던 코드 - 68ms
'''
import sys
N = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
count = 0
for i in List:
    if i == 1:
        count += 1
        continue
    if i == 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            count += 1
            break
print(N-count)
'''