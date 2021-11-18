# 1904 01타일
import sys
N = int(sys.stdin.readline())
DP = [1, 2]
for i in range(2, N):
    DP.append((DP[i-1]+DP[i-2])%15746)
print(DP[N-1])
# 68680/420
# 202036/164 - pypy3


### 29200/268
'''
import sys
N = int(sys.stdin.readline())
if N < 3:
    print(N)
else:
    x, y = 1, 2
    for i in range(2, N):
        x, y = y, (x+y)%15746
    print(y)
'''

#### 29200/160
'''
import sys
def go():
    N = int(sys.stdin.readline())
    if N < 3:
        print(N)
        return
    x, y = 1, 2
    for i in range(2, N):
        x, y = y, (x+y)%15746
    print(y)
    
if __name__ == "__main__":
    go()
'''

# 1등 코드
'''
def tile(t):
    if t in mem:
        return mem[t]
    else:
        if t%2 == 0:    # t가 짝수이면
            a = tile(t//2-1)%mod
            b = tile(t//2)%mod
            f = ((2*a+b)*b)%mod
        else:           # t가 홀수이면
            f = (tile((t+1)//2)%mod)**2 + (tile((t-1)//2)%mod)**2
        mem[t] = f%mod
        return f%mod


mem={0:0,1:1}
mod=15746
print(tile(int(input())+1))
'''