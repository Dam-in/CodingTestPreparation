import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        if a < K:
            b = heapq.heappop(heap)
            heapq.heappush(heap, a + (b*2))
            answer += 1
        else:
            if min(heap) < K:
                answer = -1
    if len(heap) == 1:
        if heap[0] < K:
            answer = -1
    return answer


s = [1, 2, 3, 10, 12]       # 2
k = 7



print(solution(s, k))