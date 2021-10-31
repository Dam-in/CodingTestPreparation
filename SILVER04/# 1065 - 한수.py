# 1065 한수
def hansu(x):
    count = 0
    for i in range(1, x+1):
        List = list(str(i))
        Set = set()
        for j in range(1, len(List)):
            Set.add(int(List[j])-int(List[j-1]))    # 공차 찾아 넣는 거
        if len(Set) == 1 or len(Set) == 0:
            count += 1
    return count


import sys
N = int(sys.stdin.readline())
print(hansu(N))



# 참고
'''
import sys
def solve(n):
    if n < 100:
        return n
    else:
        count = 99
        for i in range(100, n + 1):
            if i // 100 - i // 10 % 10 == i // 10 % 10 - i % 10:
                count += 1
        return count


n = int(sys.stdin.readline().rstrip())
print(solve(n))
'''