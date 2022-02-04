def solution(priorities, location):
    queue = [[idx, p] for idx, p in enumerate(priorities)]
    answer = 0
    while True:
        idx, p = queue.pop(0)
        if any(p < x[1] for x in queue):
            queue.append([idx, p])
        else:
            answer += 1
            if idx == location:
                return answer


p1 = [2, 1, 3, 2]           # 1
l1 = 2

p2 = [1, 1, 9, 1, 1, 1]     # 5
l2 = 0

print(solution(p1, l1))