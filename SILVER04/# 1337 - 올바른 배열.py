# 1337 올바른 배열
import sys
N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])
result = 4
if N == 2:
    if arr[1] - arr[0] < 5:
        result = 3
elif N == 3:
    if arr[2] - arr[0] < 5:
        result = 2
    elif arr[2] - arr[1] < 5 or arr[1] - arr[0] < 5:
        result = 3
elif N == 4:
    if arr[3] - arr[0] < 5:
        result = 1
    elif (arr[1] - arr[0] > 4 and arr[3] - arr[1] < 5) or (arr[3] - arr[2] > 4 and arr[2] - arr[0] < 5):
        result = 2
    elif ((arr[1]-arr[0] < 5 or arr[3]-arr[2] < 5) and arr[2]-arr[1] > 4) or (arr[2] - arr[1] < 5 and (arr[1] - arr[0] > 4 or arr[3] - arr[2] > 4)):
        result = 3
else:
    for i in range(N//2):
        count = 0
        if arr[i]+1 not in arr:
            count += 1
        if arr[i]+2 not in arr:
            count += 1
        if arr[i]+3 not in arr:
            count += 1
        if arr[i]+4 not in arr:
            count += 1
        result = min(count, result)
    for i in range(N-1, N//2, -1):
        count = 0
        if arr[i]-1 not in arr:
            count += 1
        if arr[i]-2 not in arr:
            count += 1
        if arr[i]-3 not in arr:
            count += 1
        if arr[i]-4 not in arr:
            count += 1
        result = min(count, result)
print(result)


# 28776KB / 64ms
'''
N = int(input())
arr = sorted([int(input()) for _ in range(N)])
count = []
for i in range(N):
    compare = set(range(arr[i], arr[i]+5))
    count.append(len(compare.difference(set(arr[i:i+5]))))
print(min(count))
'''

