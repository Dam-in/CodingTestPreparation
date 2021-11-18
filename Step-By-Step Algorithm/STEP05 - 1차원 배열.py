# 1차원 배열 - 10818번[최대,최소]
N = int(input())
list_str = []
list_str = input().split()
list_int = list(map(int, list_str))
print(min(list_int), max(list_int))


# 1차원 배열 - 2562번[최댓값]
list_str = []
for i in range(0, 9):
    list_str.append(input())
list_int = list(map(int, list_str))
print(max(list_int))
print(list_int.index(max(list_int))+1)


# 1차원 배열 - 2577번[숫자의 개수]
A = int(input())
B = int(input())
C = int(input())
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N = str(A*B*C)
for i in range(0,len(N)):
    if N[i]=='0':
        count[0] += 1
    elif N[i]=='1':
        count[1] += 1
    elif N[i]=='2':
        count[2] += 1
    elif N[i]=='3':
        count[3] += 1
    elif N[i]=='4':
        count[4] += 1
    elif N[i]=='5':
        count[5] += 1
    elif N[i]=='6':
        count[6] += 1
    elif N[i]=='7':
        count[7] += 1
    elif N[i]=='8':
        count[8] += 1
    elif N[i]=='9':
        count[9] += 1
for i in range(0, 10):
    print(count[i])


# 1차원 배열 - 3052번[나머지]
list_int = []
for i in range(0, 10):
    list_int.append(int(input()))
for i in range(0, 10):
    list_int[i] = list_int[i] % 42
set_int = set(list_int)
print(len(set_int))


# 1차원 배열 - 1546번[평균]
N = int(input())
record_str = []
record_str = input().split()
record_int = list(map(int, record_str))
Max = max(record_int)
i = record_int.index(Max)
for j in range(0, N):
    record_int[j] = record_int[j]/Max*100
print(sum(record_int)/N)


# 1차원 배열 - 8958번[OX퀴즈]
T = int(input())

for i in range(T):
    x = input()
    score = 0
    sumScore = 0
    for j in x:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)


# 1차원 배열 - 4344번[평균은 넘겠지]
C = int(input())
score = []
up = []
for i in range(0, C):
    score.append(input().split())
for i in range(0, C):
    x = list(map(int, score[i]))
    mean = (sum(x) - x[0]) / x[0]
    for j in range(1, len(x)):
        if x[j] > mean:
            up.append(x[j])
    print("{:.3f}%".format(len(up) / x[0] * 100))
    del up[:]
