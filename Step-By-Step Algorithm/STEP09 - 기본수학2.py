# 기본 수학 2 - 1978번[소수 찾기]
##### No 함수 구현
N = int(input())
List = list(map(int, input().split()))
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
##### 함수로 구현
N = int(input())
List = list(map(int, input().split()))
def sosu(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
count = 0
for i in List:
    if sosu(i):
        count += 1
print(count)


# 기본 수학 2 - 2581번[소수]
import sys

def sosu(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


List = []
for i in range(int(sys.stdin.readline()), int(sys.stdin.readline())+1):
    if sosu(i):
        List.append(i)
if len(List) == 0:
    print(-1)
    exit()
print(sum(List))
print(min(List))


# 기본 수학 2 - 11653번[소인수분해]
########### 내가 짠 코드
import sys
N = int(sys.stdin.readline())
i = 2
while N != 1:
    if N % i == 0:
        N = N/i
        print(i)
    else:
        i += 1
############ 시간이 훨씬 적게 걸린 코드
import sys
N = int(sys.stdin.readline().rstrip())
for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        print(i)
        N //= i
if N > 1:
    print(N)


# 기본 수학 2 - 1929번[소수 구하기]
######### 내가 구현 한 코드 -> 메모리는 가장 적게 사용 but 시간이 오래 걸려
import sys
def sosu(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True


M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if i == 2:
        print(2)
    if i % 2 != 0:
        if sosu(i):
            print(i)
######### 인터넷 참조 -> 메모리를 10000KB 정도 더 쓰지만, 시간은 20배 단축 코드
import sys
def prime(n):
    seive = [True] * (n+1)
    for i in range(2, int(n**.5)+1):
        if seive[i] == True:
            for j in range(i+i, n+1, i):
                seive[j] = False
    return [i for i in range(2, n+1) if seive[i] == True]
m, n = map(int, sys.stdin.readline().split())
primeList = prime(n)
for i in primeList:
    if i < m:
        continue
    print(i)


# 기본 수학 2 - 4948번[베르트랑 공준]
import sys
N = 123456 * 2 + 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False
def primeCount(n):
    count = 0
    for i in range(n+1, 2*n+1):
        if sieve[i]:
            count += 1
    print(count)
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    primeCount(n)


# 기본 수학 2 - 9020번[골드바흐의 추측]
import sys
def sosu(n):
    end = int(n**.5)+1
    for i in range(2, end):
        if n % i == 0:
            return False
    return True

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    for i in range(n//2, 1, -1):
        if sosu(i):
            if sosu(n-i):
                print(i, n-i)
                break


# 기본 수학 2 - 1085번[직사각형에서 탈출]
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, w-x, h-y))


# 기본 수학 2 - 3009번[네 번째 점]
X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for i in X:
    if X.count(i) == 1:
        x = i
for j in Y:
    if Y.count(j) == 1:
        y = j
print(x, y)


# 기본 수학 2 - 4153번[직각삼각형]
import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    a, b, c = sorted([a, b, c])
    if c*c == a*a + b*b:
        print('right')
    else:
        print('wrong')


# 기본 수학 2 - 3053번[택시 기하학]
import math
R = int(input())
print('%.6f' % (R*R*math.pi))
print('%.6f' % (R*R*2))


# 기본 수학 2 - 1002번[터렛]
import sys
for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**.5
    sub = max(r1 - r2, r2 - r1)
    if d == 0 and r1 == r2:
        print(-1)
    elif d == 0 and r1 != r2:
        print(0)
    elif d < r1 + r2 and d > sub:
        print(2)
    elif d == r1 + r2 or d == sub:
        print(1)
    else:
        print(0)
