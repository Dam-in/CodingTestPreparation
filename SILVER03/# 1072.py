# 1072 게임
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = Y*100//X
l, r = 1, 1000000000
if Z >= 99:
    print(-1)
else:
    while l <= r:
        m = (l + r)//2  # 1부터 게임 횟수 X의 중간값
        z = (Y+m) * 100 // (X+m)    # 중간값 만큼 했을 때 승률
        if z > Z:
            r = m - 1
        else:
            l = m + 1
    print(r+1)



'''
처음에는 반복문으로 x, y를 1씩 증가시켜 Z를 갱신하고 초기 Z값이 변하면 반복문을 빠져나오게 하고자 했다.
그러나 그렇게 구현하니 시간초과가 나왔다.
'''



### 첫번째 아이디어 - 시간 초과
'''
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = int(Y/X*100)
ori = Z
count = 0
if X == Y:
    print(-1)
    exit()
while ori == Z:
    X += 1
    Y += 1
    Z = int(Y/X*100)
    count += 1
print(count)
'''
