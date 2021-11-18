#11866 요세푸스 문제0
import sys
N, K = map(int, sys.stdin.readline().split())
List = [i for i in range(1, N+1)]
result = []
idx = K-1
while True:
    result.append(List[idx])
    del List[idx]
    idx += K-1
    if len(List) == 0:
        break
    if idx >= len(List):
        idx = idx % len(List)
print('<' + ', '.join(map(str, result)) + '>')