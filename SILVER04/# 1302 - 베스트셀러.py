# 1302 베스트셀러
import sys
dic = {}
for _ in range(int(sys.stdin.readline())):
    name = sys.stdin.readline().strip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
result = sorted(sorted(dic.items()), key=lambda x: x[1], reverse=True)
print(result[0][0])
