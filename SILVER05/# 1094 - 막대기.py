# 1094 막대기
X = int(input())
List = [64, 32, 16, 8, 4, 2, 1]
n = []
for i in List:
    if i > X:
        continue
    if sum(n)+i <= X:
        n.append(i)
print(len(n))
