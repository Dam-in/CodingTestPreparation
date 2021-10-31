# 14501 퇴사
import sys
N = int(sys.stdin.readline())
result=[];T=[];P=[]
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
    result.append(True)
for _ in range(N):
    Max = max(P)
    idx = P.index(Max)
    if N > idx + T[idx]:

print(result)
print(T)
print(P)



'''
밸류에서 최대값을 찾고
그 키만큼 키+1 인덱스부터 밸류-1만큼 뒤의 인덱스까지의 P(밸류값들)을 합한 것보다 해당 키의 P값이 큰 경우 그대로 놔두고
작은 경우 그 키의 밸류값을 0로 바꾼다.
그리고 다음 최대값을 찾고 반복한다. N만큼
그리고 나머지 남은 밸류 값들을 합한다.
'''
