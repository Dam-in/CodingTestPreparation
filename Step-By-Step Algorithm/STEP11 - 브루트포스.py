# 브루트 포스 - 2798번[블랙잭]
import sys
N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        for z in range(j-1, -1, N):
            if card[i] + card[j] + card[z] < M:
                print(card[i]+card[j]+card[z])
#### 오류가 생긴 코드 -> 미해결
for i in range(N-2):
    for j in range(i+1, N-1):
        for z in range(j+1, N):
            if card[i] + card[j] + card[z] > M:
                continue
            else:
                result = max(result, card[i]+card[j]+card[z])
print(result)



# 브루트 포스 - 2231번[분해합]
####### 내가 짠 코드 -> 시간 초과
def DecompositionSum(N):
    Sum = N
    for i in range(N - 1, -1, -1):
        x = int('1' + '0' * i)
        Sum += N // x
        N %= x
    return Sum
N = int(input())
for i in range(N):
    if N == DecompositionSum(i):
        print(i)
        exit()
print(0)
######## 인터넷 참고
def DecompositionSum(num):
    sum = num
    while True:
        if num <= 0:
            break
        sum += num % 10
        num = num // 10
    return sum
N = int(input())
result = 0
for i in range(N):
    x = DecompositionSum(i)
    if x == N:
        print(i)
        exit()
print(0)
# 29200KB / 72ms
num = int(input())
num_size = len(list(str(num)))
key = num - 9 * num_size
if key <= 0:
    key = 1
    ans = -1
for i in range(key, num+1):
    sum = i
    num_list = list(str(i))
    size = len(num_list)
    for j in range(size):
        sum += int(num_list[j])
    if sum == num:
        ans = i
        break
if ans != -1:
    print(ans)
else:
    print(0)



# 브루트 포스 - 7568번[덩치]
import sys
dic = {}
grade = 1
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    dic[x] = y
List = list()
for i in dic.keys():
    count = 1
    for j in dic.keys():
        if i < j and dic[i] < dic[j]:
            count += 1
    List.append(count)
for i in List:
    print(i, end=' ')


