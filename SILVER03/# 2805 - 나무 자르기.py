# 2805 나무 자르기
import sys
N, M = map(int, sys.stdin.readline().split(' '))
tree = list(map(int, sys.stdin.readline().split(' ')))
l=1;r=max(tree);result=0
def func(mid):
    sum = 0
    for i in tree:
        if i > mid:
            sum += i - mid
    return sum
while l<=r:
    mid = (l + r) // 2
    x = func(mid)
    if x >= M:
        l = mid + 1
        result = mid
    else:
        r = mid - 1
print(result)


# 다 함수에 넣고 구현한 거
'''
import sys
N, M = map(int, sys.stdin.readline().split(' '))
tree = list(map(int, sys.stdin.readline().split(' ')))
l=1;r=max(tree);result=0
def calc():
    global l, r, result
    while l <= r:
        mid = (l + r) // 2
        sum = 0
        for i in tree:
            if i > mid:
                sum += i - mid
        if sum >= M:
            l = mid + 1
            result = mid
        else:
            r = mid - 1
    return result

print(calc())
'''