# 1057 토너먼트
import sys
N, J, H = map(int, sys.stdin.readline().split())
round = 0
while J != H:
    J -= J//2
    H -= H//2
    round += 1
print(round)

'''
8-4-2-1-1
9-5-3-2-1
'''

'''
처음에는 지민의 번호와 한수의 번호를 x=2부터 2,4,8,16순으로 반복문 돌면서
같은 구간에 있을 경우 round 횟수를 출력하고 반복문을 빠져나온다.
다른 구간에 있을 경우 round 횟수를 증가시키고 x를 2배로 갱신한다.
로 구현하고자 했지만, 구현하지 못했다. 
'''



# 초기 설계 - 오류
'''
import sys
N, J, H = map(int, sys.stdin.readline().split())
round = 0
x = 2
while True:
    if H % x == 0 and J//x == (H//x)-1:
        print(round)
        break
    elif J%x == 0 and H//x - J//x < 1.0:
        print(round)
        break
    else:
        round += 1
        x *= 2
print(round)
'''