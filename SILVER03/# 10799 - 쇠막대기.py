#10799 쇠막대기
import sys
List = sys.stdin.readline().strip()
stack = []
laser, cnt = 0, 0
for i in range(len(List)):
    if List[i] == '(':
        if len(stack) > 0:
            cnt += len(stack)*laser
            laser = 0
        stack.append('(')
    else:
        if List[i-1] == '(':
            laser += 1
            del stack[-1]
        else:
            del stack[-1]
            cnt += laser + 1
        if len(stack) == 0:
            laser = 0
print(cnt)



# 레이저 괄호를 -로 교체한 경우
'''
import sys
List = sys.stdin.readline().strip()
List = List.replace('()', '-')
stick, cnt = 0, 0
for i in List:
    if i == '(':
        stick += 1
    elif i == '-':
        cnt += stick
    else:
        stick -= 1
        cnt += 1
print(cnt)
'''