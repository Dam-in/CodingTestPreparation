# 함수 - 15596번[정수 N개의 합]
def solve(a):
    ans = sum(a)
    return ans
a = []
while True:
    try:
        a.append(int(input()))
        x = solve(a)
        print(x)
    except EOFError:
        break


# 함수 - 4673번[셀프 넘버]
def f(n):
    a = 0
    for i in list(str(n)):
        a += int(i)
    return int(n) + a
a = []
for i in range(1, 10001):
    a.append(f(i))
for i in range(1, 10001):
    if i in a:
        pass
    else:
        print(i)


# 함수 - 1065번[한수]
def f(n):  # 해당 숫자보다 작거나 같은 한수의 개수 출력 함수
    count = 0
    for i in range(1, n+1):
        a = list(str(i))
        d = set()
        for j in range(1, len(a)):
            d.add(int(a[j]) - int(a[j-1]))
        if len(d) == 1 or len(d) == 0:
            count += 1
    return count
N = int(input())
print(f(N))
