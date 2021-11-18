# 1026 보물
import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
# print(sum(A[i] * B[i] for i in range(N))) ---> 밑의 코드를 이렇게 한 줄로 구현할 수 있음
result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)