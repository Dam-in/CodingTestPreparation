# 재귀 - 10872번[팩토리얼]
def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        x = N*factorial(N-1)
        return x
N = int(input())
print(factorial(N))


# 재귀 - 10870번[피보나치 수 5]
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(int(input())))


# 재귀 - 2447번[별 찍기 - 10]
######### 인터넷 도움
def star(n):
    if n == 3:
        return ['***', '* *', '***']
    x = star(n//3)
    y = [i*3 for i in x]
    z = [i + ' '*len(i) + i for i in x]
    return y+z+y
print(*star(int(input())), sep='\n')


# 재귀 - 11729번[하노이 탑 이동 순서]
########### 인터넷 도움
def TowerOfHanoi(n, x, y, z):
    if n == 1:
        print(x, z)
    else:
        TowerOfHanoi(n-1, x, z, y)
        print(x, z)
        TowerOfHanoi(n-1, y, x, z)
N = int(input())
K = 1
for i in range(N-1):
    K = K * 2 + 1
print(K)
TowerOfHanoi(N, 1, 2, 3)
