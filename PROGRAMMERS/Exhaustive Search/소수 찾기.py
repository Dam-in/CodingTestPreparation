from itertools import permutations
def sosu(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    list = []
    for x in range(1, len(numbers)+1):
        for y in permutations(numbers, x):
            list.append(int(''.join(y)))
    for i in set(list):
        if sosu(i):
            answer += 1
    return answer




n = '17'
n1 = '011'

print(solution(n))