# 그리디 알고리즘 - 11047번[동전 O]
import sys
N, K = map(int, sys.stdin.readline().split())
List = []
count = 0
for _ in range(N):
    List.append(int(sys.stdin.readline()))
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if List[i] > K:
        continue
    count += K//List[i]
    K %= List[i]
print(count)



# 그리디 알고리즘 - 1931번[회의실 배정]
import sys
List = []
N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    List.append([x, y])
List = sorted(List, key=lambda a: a[0])
List = sorted(List, key=lambda a: a[1])
count = 1
finish = List[0][1]
for i in range(1, N):
    if List[i][0] >= finish:
        count += 1
        finish = List[i][1]
print(count)
