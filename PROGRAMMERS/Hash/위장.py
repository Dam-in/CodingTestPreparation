from collections import Counter

def solution(clothes):
    data = Counter([clothes[i][1] for i in range(len(clothes))]).values()
    answer = 1
    for x in data:
        answer *= (x+1)
    print(answer-1)


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])




'''
from itertools import combinations
from functools import reduce


def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


def solution(clothes):
    data, cnt = [], []
    for a, b in clothes:
        if b in data:
            cnt[data.index(b)] += 1
        else:
            data.append(b)
            cnt.append(1)
    answer = sum(cnt)
    for i in range(2, len(cnt)+1):
        for x in combinations(cnt, i):
            answer += multiply(x)
    print(answer)


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
'''


# Counter를 이용한 구현
'''
from itertools import combinations
from functools import reduce
from collections import Counter

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


def solution(clothes):
    data = Counter([clothes[i][1] for i in range(len(clothes))]).values()
    answer = sum(data)
    for i in range(2, len(data) + 1):
        for x in combinations(data, i):
            answer += multiply(x)
    print(answer)


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
'''


# 잘 짠 코드
'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''