import heapq

def solution(operations):
    heap = []
    for operation in operations:
        c, n = operation.split()
        if c == 'I':
            heapq.heappush(heap, int(n))
        else:
            if len(heap) != 0:
                if int(n) == -1:
                    heapq.heappop(heap)
                else:
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
    if len(heap) == 0:
        return [0, 0]
    else:
        return heapq.nlargest(1, heap) + [heapq.heappop(heap)]



o = ["I 16","D 1"]                  # [0, 0]
o1 = ["I 7","I 5","I -5","D -1"]    # [7, 5]
o2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    # [333, -45]

print(solution(o2))