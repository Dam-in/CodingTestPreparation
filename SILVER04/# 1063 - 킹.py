# 1063 킹
import sys
king, doll, N = sys.stdin.readline().split()
move = list(sys.stdin.readline().strip() for _ in range(int(N)))
for m in move:
    if 'R' == m:        # 오른쪽
        if ('H' in king) or ('G' in king and 'H' in doll and king[1] == doll[1]):
            continue
        else:
            if king[1] == doll[1] and ord(doll[0]) - ord(king[0]) == 1:
                doll = chr(ord(doll[0])+1) + doll[1]
            king = chr(ord(king[0])+1) + king[1]
    elif 'L' == m:      # 왼쪽
        if ('A' in king) or ('B' in king and 'A' in doll and king[1] == doll[1]):
            continue
        else:
            if king[1] == doll[1] and ord(king[0]) - ord(doll[0]) == 1:
                doll = chr(ord(doll[0])-1) + doll[1]
            king = chr(ord(king[0])-1) + king[1]
    elif 'B' == m:      # 아래
        if ('1' in king) or ('2' in king and '1' in doll and king[0] == doll[0]):
            continue
        else:
            if king[0] == doll[0] and ord(king[1]) - ord(doll[1]) == 1:
                doll = doll[0] + chr(ord(doll[1])-1)
            king = king[0] + chr(ord(king[1])-1)
    elif 'T' == m:      # 위
        if ('8' in king) or ('7' in king and '8' in doll and king[0] == doll[0]):
            continue
        else:
            if (king[0] == doll[0]) and (ord(doll[1]) - ord(king[1]) == 1):
                doll = doll[0] + chr(ord(doll[1])+1)
            king = king[0] + chr(ord(king[1])+1)
    elif 'RT' == m:     # 대각선(오른쪽 위)
        if 'H' in king or '8' in king or (king[0] == 'G' and doll[0] == 'H' and ord(doll[1])-ord(king[1]) == 1) or (king[1] == '7' and doll[1] == '8' and ord(doll[0]) - ord(king[0])==1):
            continue
        else:
            if (ord(doll[0])-ord(king[0])==1) and (ord(doll[1])-ord(king[1])==1):
                doll = chr(ord(doll[0])+1) + chr(ord(doll[1])+1)
            king = chr(ord(king[0])+1) + chr(ord(king[1])+1)
    elif 'LT' == m:     # 대각선(왼쪽 위)
        if 'A' in king or '8' in king or (king[0] == 'B' and doll[0] == 'A' and ord(doll[1])-ord(king[1]) == 1) or (king[1] == '7' and doll[1] == '8' and ord(king[0]) - ord(doll[0])==1):
            continue
        else:
            if (ord(king[0])-ord(doll[0])==1) and (ord(doll[1])-ord(king[1])==1):
                doll = chr(ord(doll[0])-1) + chr(ord(doll[1])+1)
            king = chr(ord(king[0])-1) + chr(ord(king[1])+1)
    elif 'RB' == m:     # 대각선(오른쪽 아래)
        if 'H' in king or '1' in king or (king[0] == 'G' and doll[0] == 'H' and ord(king[1])-ord(doll[1])==1) or (king[1] == '2' and doll[1] == '1' and ord(king[0])-ord(doll[0])==1):
            continue
        else:
            if (ord(doll[0])-ord(king[0])==1) and (ord(king[1])-ord(doll[1])==1):
                doll = chr(ord(doll[0])+1) + chr(ord(doll[1])-1)
            king = chr(ord(king[0])+1) + chr(ord(king[1])-1)
    elif 'LB' == m:     # 대각선(왼쪽 아래)
        if 'A' in king or '1' in king or (king[0] == 'B' and doll[0] == 'A' and ord(king[1])-ord(doll[1])==1) or (king[1] == '2' and doll[1] == '1' and ord(king[0])-ord(doll[0])==1):
            continue
        else:
            if (ord(king[0])-ord(doll[0])==1) and (ord(king[1])-ord(doll[1])==1):
                doll = chr(ord(doll[0])-1) + chr(ord(doll[1])-1)
            king = chr(ord(king[0])-1) + chr(ord(king[1])-1)
print(king)
print(doll)


'''
E5 F6 3
RT
R
T

G7
G8
------------
D1 B3 3
LT
LT
LT

B3
A4
------------
A8 C8 3
R
R
LB

B7
D8
'''