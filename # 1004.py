# 1004 어린 왕자
import sys
for _ in range(int(sys.stdin.readline())):   # 입력 받은 수만큼 반복
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    count = 0

    for i in range(n):  # 원의 개수만큼 반복
        cx, cy, r = map(int, sys.stdin.readline().split())
        aDistance = ((x1 - cx)**2 + (y1 - cy)**2)**0.5    # 출발점과 i번째 원 사이 거리(aDistance)
        bDistance = ((x2 - cx)**2 + (y2 - cy)**2)**0.5    # 도착점과 i번째 원 사이 거리(bDistance)
        if aDistance < r and bDistance < r:     # 두 점 모두 한 원 안에 있는 경우
            continue
        elif aDistance < r or bDistance < r:    # 각각의 거리과 원의 반지름 크기 비교
            count += 1
    print(count)




'''
초기 설계 : 두 점과 각 원들의 거리(xdistance, ydistance)를 구하고 각각의 d와 r중 d가 클 때만 카운트 해준다. 두 점 모두
'''