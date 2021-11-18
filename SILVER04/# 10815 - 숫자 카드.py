#10815 숫자 카드
import sys
sys.stdin.readline()
nList = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
mList = list(map(int, sys.stdin.readline().split()))
for x in mList:
    if x in nList:
        print(1, end=' ')
    else:
        print(0, end=' ')