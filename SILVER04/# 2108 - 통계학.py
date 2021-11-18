#2108 통계학
import sys
from collections import Counter
N = int(sys.stdin.readline())
data = sorted([int(sys.stdin.readline()) for _ in range(N)])
# 산술 평균
print(round(sum(data)/N))
# 중앙값
print(data[N//2])
# 최빈값
dataCount = Counter(data).most_common()
if len(data) > 1 and dataCount[0][1] == dataCount[1][1]:
    print(dataCount[1][0])
else:
    print(dataCount[0][0])
# 범위
print(data[-1]-data[0])
