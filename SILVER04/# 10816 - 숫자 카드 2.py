#10816 숫자 카드 2
import sys
from collections import Counter
sys.stdin.readline()
nList = Counter(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
mList = list(map(int, sys.stdin.readline().split()))
for i in mList:
    if i in nList:
        print(nList[i], end=' ')
    else:
        print(0, end=' ')
