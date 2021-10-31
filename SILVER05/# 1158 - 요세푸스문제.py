# 1158 요세푸스 문제
'''
from collections import deque
N, K = map(int, input().split())
deq = deque([])
result = []
for i in range(N):
    deq.append(i+1)
while len(deq) != 0:
    for _ in range(K):
        x = deq.popleft()
        deq.append(x)
    result.append(deq.pop())
print('<' + ', '.join(map(str, result)) + '>')
'''



# 처음 구현한 코드 - 리스트로 구현 - 시간 초과
'''
N, K = map(int, input().split())
result = []
Queue = []
for i in range(1, N):
    Queue.append(i)
while len(Queue) != 0:
    for _ in range(K-1):
        a = Queue.pop()
        Queue.insert(0, a)
    result.append(Queue.pop())
print('<' + ', '.join(map(str, result)) + '>')
'''

# 큐를 사용하여 구현 - 시간 초과
'''
import queue
Q = queue.Queue()
N, K = map(int, input().split())
result = []
for i in range(1, N+1):
    Q.put(i)
while Q.qsize() != 0:
    for _ in range(K-1):
        x = Q.get()
        Q.put(x)
    result.append(Q.get())
print('<' + ', '.join(map(str, result)) + '>')
'''
