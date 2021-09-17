# 1037 약수
import sys
int(sys.stdin.readline())
divisor = list(map(int, sys.stdin.readline().split()))
print(max(divisor)*min(divisor))



# 최대 최소 함수 직접 구현
import sys
int(sys.stdin.readline())
divisor = list(map(int, sys.stdin.readline().split()))
min = divisor[0]
max = divisor[0]
for i in divisor:
    if min > i:
        min = i
    if max < i:
        max = i
print(max*min)



# 처음에 구현한 코드
import sys
int(sys.stdin.readline())
divisor = list(map(int, sys.stdin.readline().split()))
N = 3
while True:
    flag = False
    N += 1
    if N in divisor:    # 약수 리스트에 있으면 패스
        continue
    for i in divisor:
        if N % i != 0:
            flag = True
            break
    if flag:
        continue
    print(N)
    break