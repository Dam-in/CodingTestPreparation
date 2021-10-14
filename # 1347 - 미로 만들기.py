# 1347 미로 만들기
def changeDirection(key, D):
    if key == 'R':
        if D == 'v':
            D = '<'
        elif D == '<':
            D = '^'
        elif D == '^':
            D = '>'
        else:
            D = 'v'
    else:
        if D == 'v':
            D = '>'
        elif D == '<':
            D = 'v'
        elif D == '^':
            D = '<'
        else:
            D = '^'
    return D


import sys
N = int(sys.stdin.readline())
note = sys.stdin.readline().strip()
maze = [['#' for _ in range(101)] for _ in range(101)]
x, y = 50, 50
maze[x][y] = '.'  # 출발점
Direction = 'v'
OutputRange = [[50, 50]]
for i in note:
    if i == 'R' or i == 'L':
        Direction = changeDirection(i, Direction)
    else:
        if Direction == 'v':
            x += 1
        elif Direction == '<':
            y -= 1
        elif Direction == '^':
            x -= 1
        else:
            y += 1
        OutputRange.append([x, y])
        maze[x][y] = '.'
a = set()  # 미로 세로 길이
b = set()  # 미로 가로 길이
for i in range(len(OutputRange)):
    a.add(OutputRange[i][0])
    b.add(OutputRange[i][1])
for x in range(min(a), max(a)+1):
    for y in range(min(b), max(b)+1):
        print(maze[x][y], end='')
    print()

'''
11
RFLFFFLFRFF

..
.#
.#
..
#.
#.
'''





# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
#
# command_length = int(input())
# commands = input()
#
# dir = 2
# pos = [0, 0]
# x_list = [0]
# y_list = [0]
# for command in commands:
#     if command == 'L':
#         dir = (dir - 1) % 4
#     elif command == 'R':
#         dir = (dir + 1) % 4
#     elif command == 'F':
#         x, y = pos
#         nx, ny = x + dx[dir], y + dy[dir]
#         x_list.append(nx)
#         y_list.append(ny)
#         pos = [nx, ny]
#
# max_x, min_x, max_y, min_y = max(x_list), min(x_list), max(y_list), min(y_list)
# N, M = max_x - min_x + 1, max_y - min_y + 1
# start_x, start_y = abs(min_x), abs(min_y)
# maze = [['#'] * M for _ in range(N)]
# for x, y in zip(x_list, y_list):
#     maze[start_x + x][start_y + y] = '.'
#
# for line in maze:
#     print("".join(line))