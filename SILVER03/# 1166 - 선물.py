'''
오류! 풀다가 말았음
'''

# 1166 선물
import sys
N, L, W, H = map(float, sys.stdin.readline().split())
L, W, H = sorted([L, W, H])
i = 1
A = L
while True:
    n = (L // A) * (W // A) * (H // A)
    if n == N:
        print(A)
        break
    elif n > N:
        A -= L/(2*i)
    else:
        A += L/(2*i)
    i += 1



'''
1. 제일 작은 수를 A로 정한다. 
2. 아래의 계산을 한다.
    가로 x 세로 x 높이 개수 == N인지 체크
3. A를 제일 작은 L의 절반으로 바꾼다. (A = L/2)
4. 2번의 계산을 한다.
5. 맞으면 출력 후 반복문 빠져나온다.
6. 틀린 경우, 그 개수가 N보다 크면 A = A + L/(2*2)로 A를 갱신한다.
7. 그 개수가 N보다 작으면 A = A - L/(2*2)로 A를 갱신한다.
'''
