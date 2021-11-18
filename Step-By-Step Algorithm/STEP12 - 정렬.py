# 정렬 - 2750번[수 정렬하기]
N = int(input())
x = []
for i in range(N):
    x.append(int(input()))
x.sort()
for i in x:
    print(i)


# 정렬 - 2751번[수 정렬하기 2]
### pypy3로 풀면 맞고 python은 시간초과
N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
for i in sorted(list):
    print(i)
######### 참조
from sys import stdin
n = int(stdin.readline())
N = [int(stdin.readline()) for i in range(n)]
N.sort()
[print(N[i]) for i in range(n)]


# 정렬 - 10989번[수 정렬하기 3]
from sys import stdin
list = [0] * 10001
for i in range(int(stdin.readline())):
    list[int(stdin.readline())] += 1
for i in range(len(list)):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)


# 정렬 - 2108번[통계학]
from sys import stdin
from collections import Counter
N = int(stdin.readline())
List = []
for _ in range(N):
    List.append(int(stdin.readline()))
List.sort()
ListCounter = Counter(List).most_common()
print(round(sum(List)/N))
print(List[N//2])
print(ListCounter)
if len(ListCounter) > 1:
    if ListCounter[0][1] == ListCounter[1][1]:
        print(ListCounter[1][0])
    else:
        print(ListCounter[0][0])
else:
    print(ListCounter[0][0])
print(List[-1]-List[0])
####### 인터넷 참조
import sys
sum = 0
numCount = [None] * 8001
Max = float('-inf')
Min = float('inf')
N = int(sys.stdin.readline().strip())
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    sum += num
    idx = num + 4000
    if numCount[idx] is None:
        numCount[idx] = 1
    else:
        numCount[idx] += 1
    if Min > num:
        Min = num
    if Max < num:
        Max = num
print(round(sum/N))
centerIdx = N//2
curIdx = -1
for num, i in enumerate(numCount[Min + 4000:Max + 4001], Min):
    if i is None:
        continue
    if curIdx <= centerIdx <= curIdx + i:
        print(num)
        break
    curIdx += i
val = max(v for v in numCount if v is not None)
vals = sorted(i - 4000 for i, v in enumerate(numCount) if v == val)
if len(vals) == 1:
    print(vals[0])
else:
    print(vals[1])
print(Max - Min)


# 정렬 - 1427번[소트인사이드]
List = list(input())
List.sort()
List.reverse()
for i in List:
    print(i, end='')


# 정렬 - 11650번[좌표 정렬하기]
import sys
List = []
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    List.append((x, y))
List.sort()
for i in range(len(List)):
    print(f'{List[i][0]} {List[i][1]}')


# 정렬 - 11651번[좌표 정렬하기 2]
import sys
List = []
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    List.append((y, x))
List.sort()
for i in range(len(List)):
    print(f'{List[i][1]} {List[i][0]}')


# 정렬 - 1181번[단어 정렬]
import sys
List = []
for _ in range(int(sys.stdin.readline())):
    List.append(sys.stdin.readline().rstrip())
List = list(set(List))
List.sort()
List.sort(key=len)
for i in List:
    print(i)


# 정렬 - 10814번[나이순 정렬]
import sys
List = []
for _ in range(int(sys.stdin.readline())):
    age, name = map(str, sys.stdin.readline().split())
    List.append((int(age), name))
print(List)
List.sort(key=lambda x: x[0])
for i in List:
    print(f'{i[0]} {i[1]}')


# 정렬 18870번[좌표 압축]
import sys
int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
newList = sorted(set(List))
dic = {x: idx for idx, x in enumerate(newList)}
for i in List:
    print(dic[i], end=' ')
