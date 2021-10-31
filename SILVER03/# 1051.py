# 1051 숫자 정사각형
import sys
N, M = map(int, sys.stdin.readline().split())
Rectangle = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
size = 1
for l in range(1, min(N, M)):
    for row in range(N-l):
        for col in range(M-l):
            if Rectangle[row][col] == Rectangle[row+l][col] == Rectangle[row][col+l] == Rectangle[row+l][col+l]:
                size = (l+1)**2
print(size)
