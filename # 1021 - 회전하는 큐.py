# 1021 회전하는 큐
import sys
N, M = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))
data = [i for i in range(1, N+1)]
result = 0
for i in range(M):
    l = len(data)
    idx = data.index(location[i])
    if idx < l - idx:       # 2번 연산
        while True:
            if data[0] == location[i]:
                del data[0]
                break
            else:
                data.append(data[0])
                del data[0]
                result += 1
    else:                   # 3번 연산
        while True:
            if data[0] == location[i]:
                del data[0]
                break
            else:
                data.insert(0, data[-1])
                del data[-1]
                result += 1
print(result)
