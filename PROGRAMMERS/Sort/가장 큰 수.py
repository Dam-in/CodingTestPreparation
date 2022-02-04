def solution(numbers):
    answer = list(map(str, numbers))
    answer = sorted(answer, key=lambda x: x[len(x)-1], reverse=True)
    return ''.join(answer)


n = [6, 10, 2]              # "6210"
n1 = [3, 30, 34, 5, 9]      # "9534330"
n2 = [1, 10, 100, 1000]     # 1101001000
n3 = [0, 0, 0, 0]
n4 = [33, 30, 3]
n5 = [1, 2, 3, 4, 5]
n6 = [21, 212]
n7 = [30, 303]
n8 = [0, 0, 1, 1, 0, 0]
n9 = [1, 10001, 10101]


print(solution(n))
print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
print(solution(n5))
print(solution(n6))
print(solution(n7))
print(solution(n8))
print(solution(n9))