# 문자열 - 11654번[아스키 코드]
print(ord(input()))


# 문자열 - 11720번[숫자의 합]
l = int(input())
s = input()
n = []
for i in range(l):
    n.append(int(s[i]))
print(sum(n))


# 문자열 - 10809번[알파벳 찾기]
s = input()
dm = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
for i in range(len(s)):
    for j in range(0, 26):
        if s[i] == chr(j + 97) and dm[j] == -1:
            dm[j] = i
for i in dm:
    print(i, end=" ")


# 문자열 - 2675번[문자열 반복]
T = int(input())
for i in range(T):
    R, S = input().split()
    for j in S:
        print(j*int(R), end='')
    print()


# 문자열 - 1157번[단어 공부]
S = input()
S = S.upper()
al = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in S:
    for j in range(0, 26):
        if i == chr(j + 65):
            al[j] += 1
result = list(filter(lambda x: al[x] == max(al), range(len(al))))   # 중복된 값에 따른 인덱스 모두 저장하기
if len(result) > 1:
    print('?')
else:
    print(chr(al.index(max(al)) + 65))


# 문자열 - 1152번[단어의 개수]
print(len(input().split()))


# 문자열 - 2908번[상수]
A, B = input().split()
if ''.join(reversed(A)) > ''.join(reversed(B)):
    print(''.join(reversed(A)))
else:
    print(''.join(reversed(B)))


# 문자열 - 5622번[다이얼]
c = 0
for i in input():
    if i == chr(65) or i == chr(66) or i == chr(67):
        c += 3
    elif i == chr(68) or i == chr(69) or i == chr(70):
        c += 4
    elif i == chr(71) or i == chr(72) or i == chr(73):
        c += 5
    elif i == chr(74) or i == chr(75) or i == chr(76):
        c += 6
    elif i == chr(77) or i == chr(78) or i == chr(79):
        c += 7
    elif i == chr(80) or i == chr(81) or i == chr(82) or i == chr(83):
        c += 8
    elif i == chr(84) or i == chr(85) or i == chr(86):
        c += 9
    elif i == chr(87) or i == chr(88) or i == chr(89) or i == chr(90):
        c += 10
print(c)


# 문자열 - 2941번[크로아티아 알파벳]
########## 내가 짠 코드
s = input()
n = 0
for i in range(len(s)):
    if s[i] == '=':
        if s[i-1] == 'c' or s[i-1] == 'z' or s[i-1] == 's' or s[i-1] == 'z':
            continue
    elif s[i] == '-':
        if s[i-1] == 'c' or s[i-1] == 'd':
            continue
    elif s[i] == 'd':
        if s[i+1] == 'z' and s[i+2] == '=':
            continue
    elif s[i] == 'j':
        if s[i-1] == 'l' or s[i-1] == 'n':
            continue
    n += 1
print(n)
######### 인터넷 참고 코드
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for t in a:
    alpha = alpha.replace(t, '*')
print(len(alpha))


# 문자열 - 1316번[그룹 단어 체커]
######### 인터넷 참조
N = int(input())
count = 0
a = []
for i in range(N):
    s = input()
    for j in range(len(s)):
        if j != len(s)-1:
            if s[j] == s[j+1]:
                pass
            elif s[j] in s[j+1:]:
                break
        else:
            count += 1
print(count)


