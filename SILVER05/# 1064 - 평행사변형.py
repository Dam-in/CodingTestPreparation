# 1064 평행사변형
import sys
x1, y1, x2, y2, x3, y3 = list(map(int, sys.stdin.readline().split()))
# 평행사변형이 안 만들어지는 경우
# 세 점으로 구한 세 개의 기울기가 똑같을 때 -> 일직선
if abs(x1 - x2) != 0 and abs(x1 - x3) != 0 and abs(x2 - x3) != 0:
    dx = abs(y1 - y2) / abs(x1 - x2)
    dy = abs(y1 - y3) / abs(x1 - x3)
    dz = abs(y2 - y3) / abs(x2 - x3)
    if dx == dy or dx == dz or dy == dz:
        print(-1.0)
        exit()
# 기울기가 수평선, 수직선인 경우
if x1 == x2 == x3 or y1 == y2 == y3:
    print(-1.0)
    exit()
# 평행사변형이 만들어지는 경우
x = abs(((x2-x1)**2 + (y2-y1)**2)**0.5)
y = abs(((x3-x1)**2 + (y3-y1)**2)**0.5)
z = abs(((x2-x3)**2 + (y2-y3)**2)**0.5)
List = [x*2+y*2, x*2+z*2, y*2+z*2]
print(max(List)-min(List))



# 참고
'''
if (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2) and (x2 - x1) * (y2 - y3) == (x2 - x3) * (y2 - y1):
    print(-1)
else:
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    list = []
    for i in range(3):
        list.append(((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5 + ((x[i] - x[i - 2]) ** 2 + (y[i] - y[i - 2]) ** 2) ** 0.5)
    print((max(list) - min(list)) * 2)
'''
