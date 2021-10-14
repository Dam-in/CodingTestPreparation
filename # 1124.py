# 1124 언더프라임
import sys
A, B = map(int, sys.stdin.readline().split())
count = 0


def Prime(n):   # n의 소인수 개수를 리턴해주는 함수
    primeCount = 0
    for i in range(2, int(n**.5)+1):
        while n % i == 0:
            primeCount += 1
            n //= i
    if n > 1:
        primeCount += 1
    return primeCount


def sosu(n):    # n이 소수인지 아닌지 불린식으로 리턴하는 함수
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True


for x in range(A, B+1):
    if sosu(Prime(x)):
        count += 1
print(count)

