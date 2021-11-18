#1966 프린터 큐
import sys
for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    W = list(map(int, sys.stdin.readline().split()))
    w = [0 for i in range(N)]
    w[M] = 1
    cnt = 0
    while True:
        if W[0] == max(W):
            cnt += 1
            if w[0] == 1:
                print(cnt)
                break
            else:
                del W[0]
                del w[0]
        else:
            W.append(W[0])
            del W[0]
            w.append(w[0])
            del w[0]


# 3등 코드 (공개된 것 중 1등)
'''
from sys import stdin as st
def nQ(a,b,c):
    ks=iter(sorted(list(set(b)),reverse=True))
    oQ,curI,lastI,frstI=0,0,-1,0
    while True:
        if frstI==curI:
            curK=next(ks)
            curI=(lastI+1)%c
            frstI=curI
        if b[curI]==curK:
            oQ+=1
            lastI=curI
            if curI==a:
                return oQ
        curI+=1
        curI%=c
caseN=int(st.readline())
for i in range(caseN):
    N, Loc=map(int,st.readline().split())
    que=list(map(int,st.readline().split()))
    print(nQ(Loc,que,N))
'''