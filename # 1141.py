# 1141 접두사
import sys
N = int(sys.stdin.readline())
List = sorted([sys.stdin.readline().strip() for _ in range(N)], key=len)
count = 0
for i in range(N):
    word = List[i]
    flag = False
    for j in range(i + 1, N):
        try:
            if List[j].index(word) == 0:
                flag = True
                break
        except:
            continue
    if not flag:
        count += 1
print(count)

'''
테스트
5
hi
hk
h
h
zh

5
hi
hi
hk
h
zh

6
hi
hk
h
h
h
zh
'''
