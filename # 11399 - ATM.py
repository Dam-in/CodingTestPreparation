# 11399 ATM
import sys
N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))
result = 0
for i in range(1, N+1):
    result += sum(P[:i])
print(result)


# 위의 코드를 퀵정렬을 이용한 구현
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left_side, equal, right_side = [], [], []
    for x in arr:
        if x < pivot:
            left_side.append(x)
        elif x > pivot:
            right_side.append(x)
        else:
            equal.append(x)
    return quick_sort(left_side) + equal + quick_sort(right_side)


import sys
N = int(sys.stdin.readline())
P = quick_sort(list(map(int, sys.stdin.readline().split())))
result = 0
for i in range(1, N+1):
    result += sum(P[:i])
print(result)
'''


# DP를 이용한 구현
'''
import sys
N = int(sys.stdin.readline())

DP = [0, 1, 2]

for i in range(3, N + 1):
  DP.append(DP[i - 2] + DP[i - 1])
print(DP[N] % 10007)
'''