# 1018 체스판 다시 칠하기
import sys
N, M = map(int, input().split())
chessStdW = [[]]
chessStdB = [[]]
chess = []
colorW = 'W'
colorB = 'B'

# 체스판 만들기
for i in range(N):
    # 입력받은 문자로 체스판 만들기
    chess.append(list(sys.stdin.readline().strip()))
    # 표준 체스판 만들기
    chessStdW.append(list())
    chessStdB.append(list())
    for j in range(M):
        chessStdW[i].append(colorW)
        chessStdB[i].append(colorB)
        if colorW == 'W':
            colorW = 'B'
            colorB = 'W'
        else:
            colorW = 'W'
            colorB = 'B'
    if M % 2 == 0:
        if colorW == 'W':
            colorW = 'B'
            colorB = 'W'
        else:
            colorW = 'W'
            colorB = 'B'
del chessStdW[-1], chessStdB[-1]

a, b, c, d = 0, 8, 0, 8
result = N*M
while b != N+1:
    while d != M+1:
        countW, countB = 0, 0
        for i in range(a, b):  # 행 인덱스
            for j in range(c, d):  # 열 인덱스
                if chess[i][j] != chessStdW[i][j]:
                    countW += 1
                if chess[i][j] != chessStdB[i][j]:
                    countB += 1
        if result > countW:
            result = countW
        if result > countB:
            result = countB
        c += 1
        d += 1
    a += 1
    b += 1
    c, d = 0, 8
print(result)
