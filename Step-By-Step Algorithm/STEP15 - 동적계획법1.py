# 동적 계획법 1 - 1003번[피보나치 함수]
import sys
for _ in range(int(sys.stdin.readline())):
    count0 = 1
    count1 = 0
    temp = 0
    for _ in range(int(sys.stdin.readline())):
        temp = count1
        count1 += count0
        count0 = temp
    print(count0, count1)



# 동적 계획법 1 - 9184번[신나는 함수 실행]
import sys
DP = [[[0]*21 for _ in range(21)] for _ in range(21)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if DP[a][b][c]:
        return DP[a][b][c]
    if a < b < c:
        DP[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return DP[a][b][c]
    DP[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return DP[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

print(DP)
