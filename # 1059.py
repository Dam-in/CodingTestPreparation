# 1059 좋은 구간
def func():
    L = int(input())
    S = sorted(map(int, input().split()))
    n = int(input())

    prev = 0
    for i in S:
        if i == n:
            return 0

        if i > n:
            A = prev + 1
            B = i - 1
            break
        prev = i
    return (n-A)*(B-n) + (n-A) + (B-n)
print(func())


### No 함수
L = int(input())
S = sorted(map(int, input().split()))
n = int(input())
if n in S:
    print(0)
else:
    i = 0
    while n > S[i]:
        i += 1
        if i == len(S):
            i -= 1
            break
    if i == 0:
        print(n * (S[0] - n) - 1)
    else:
        print((n - S[i - 1]) * (S[i] - n) - 1)


### 처음에 구현한 코드 -> 런타임에러
import sys
L = int(sys.stdin.readline())
S = sorted(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

if n in S:
    print(0)
else:
    for i in S:
        if n < i:
            B = i-1
            break
        A = i+1
    print((n-A)*(B-n) + (n-A) + (B-n))