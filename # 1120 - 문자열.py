import sys
A, B = sys.stdin.readline().split()
result = len(A)
for a in range(len(B)-len(A)+1):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i+a]:
            count += 1
    if count < result:
        result = count
print(result)