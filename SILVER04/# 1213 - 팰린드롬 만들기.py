# 1213 팰린드롬 만들기
import sys
name = sorted(sys.stdin.readline().strip())
N = len(name)
palindrom = [0 for _ in range(N)]
dic = {}
for i in sorted(set(name)):
    dic[i] = 0
for i in name:
    dic[i] += 1

List = list()
for i in sorted(set(name)):
    if dic[i] % 2 != 0:
        List.append(i)
if len(List) > 1:
    print("I'm Sorry Hansoo")
    exit()
if len(List) == 1:
    palindrom[N//2] = List[0]
    name.remove(List[0])
for i in range(N//2):
    palindrom[i] = name[0]
    del name[0]
    palindrom[-(1+i)] = name[0]
    del name[0]
    if palindrom[i] != palindrom[-(1+i)]:
        print("I'm Sorry Hansoo")
        exit()
for i in palindrom:
    print(i, end='')



'''
셋함수와 딕셔너리로 개수를 생각해서 구현하려고 했었다.
그럴 필요없이 정렬하고 순서대로 순서에 맞춰서 넣으면 된다
'''


# AACVV 같은 경우에서 오류
'''
import sys
name = sorted(sys.stdin.readline().strip())
N = len(name)
palindrom = [0 for _ in range(N)]
for i in range(N//2):
    palindrom[i] = name[0]
    del name[0]
    palindrom[-(1+i)] = name[0]
    del name[0]
    if palindrom[i] != palindrom[-(1+i)]:
        print("I'm Sorry Hansoo")
        exit()
if N % 2 != 0:
    palindrom[N//2] = name[0]
for i in palindrom:
    print(i, end='')
'''

