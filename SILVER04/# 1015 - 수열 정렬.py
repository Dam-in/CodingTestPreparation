# 1015 수열 정렬
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
ori = A
for i in range(N):
    A[i] = [i, A[i]]
A = sorted(A, key=lambda x: x[1])
for x in ori:
    for y in A:
        if x == y:
            print(A.index(y), end=' ')
            break


# 탐색을 완전탐색이 아닌 이진탐색으로 하는 경우
'''
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    A[i] = [i, A[i]]
ori = A
A = sorted(A, key=lambda x: x[1])


# 이진 탐색으로 찾기
def binarySearch(target, data):
    start = data.index(data[0])
    end = data.index(data[-1])
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid][1] == target[1]:
            if target[1] != data[mid-1][1]:
                start = mid + 1
            else:
                if data[mid-1][0] < target[0]:
                    start = mid + 1
                else:
                    end = mid - 1
        elif data[mid][1] <= target[1]:
            start = mid + 1
        else:
            end = mid - 1


for x in ori:
    print(binarySearch(x, A))
'''




# 예제 입력 및 출력
'''
5
2 1 3 1 2
-> 2 0 4 1 3

5
4 2 6 1 9
-> 2 1 3 0 4

7
3 3 3 2 2 2 1
-> 4 5 6 1 2 3 0

5
1 0 1 0 1
-> 2 0 3 1 4

3
1 1 1
-> 0 1 2
'''

# 문제 설명
'''
5
600 200 300 400 500
이 입력으로 주어진 경우

답은 4 0 1 2 3이다

설명
B[] = 600
B[] = 200
B[] = 300
B[] = 400
B[] = 500

인덱스 부여
B[0] = 600
B[1] = 200
B[2] = 300
B[3] = 400
B[4] = 500

B의 값을 기준으로 정렬
B[1] = 200
B[2] = 300
B[3] = 400
B[4] = 500
B[0] = 600

인덱스 한번 더 부여
B[1,0] = 200
B[2,1] = 300
B[3,2] = 400
B[4,3] = 500
B[0,4] = 600

B의 첫번째 값을 기준으로 정려 for 다시 원래순서로 돌아가기 위해
B[0,4] = 600
B[1,0] = 200
B[2,1] = 300
B[3,2] = 400
B[4,3] = 500

답은 B의 두번째 값인 4 0 1 2 3이다

출처: https://www.crocus.co.kr/823 [Crocus]
'''