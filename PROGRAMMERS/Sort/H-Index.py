def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

c = [3, 0, 6, 1, 5]     # 3


print(solution(c))