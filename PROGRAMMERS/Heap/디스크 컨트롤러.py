def solution(jobs):
    answer, point, heap = 0, 0, []
    heap = sorted(jobs, key=lambda x: x[1])
    heap = sorted(heap, key=lambda x: x[0])
    print(heap)
    while len(heap) > 0:
        a, b = heap.pop(0)
        if point < a:
            point += a-point+b
            answer += b
        else:
            point += b
            answer += point-a
        print(answer)
    return answer//3


j = [[0, 3], [1, 9], [2, 6]]    # 9
j1 = [[0, 2], [4, 7], [9, 11]]  # 7
j2 = [[0, 5], [1, 7], [8, 2]]   # 5+11+2 = 18
j3 = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # 72
j4 = [[1, 2], [4, 3], [8, 5]]   # 3
j5 = [[1, 3], [2, 5], [8, 6]]   # 5

[[0, 3], [1, 9], [2, 6]]    9
[[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]    13
[[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]    13
[[0, 3], [0, 1], [4, 7]]    4
[[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]    13
[[0, 1], [0, 1], [1, 0]]    1
[[0, 5], [1, 2], [5, 5]]    6
[[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]    13
[[0, 1], [1, 2], [500, 6]]      3
[[0, 10], [4, 10], [5, 11], [15, 2]]    15
[[0, 10]]   10
[[1, 10], [3, 3], [10, 3]]      9
[[0, 10], [2, 3], [9, 3]]   9
[[0, 3], [4, 3], [10, 3]]   3
[[0, 10], [2, 10], [25, 10], [25, 2]]   10
[[0, 3], [1, 9], [2, 6], [4, 3]]    9
[[0, 4], [0, 3], [0, 2], [0, 1]]    5
[[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]   72

print(solution(j))