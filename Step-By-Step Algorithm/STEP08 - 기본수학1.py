# 기본 수학 1 - 1712번[손익분기점]
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)


# 기본 수학 1 - 2292번[벌집]
N = int(input())
res = 1
i = 1
while True:
    if N-1 <= 0: break
    N = N - (6*i)
    res += 1
    i += 1
print(res)


# 기본 수학 1 - 1193번[분수찾기]
X = int(input())
i = 1
while True:
    if X <= i:
        break
    X -= i
    i += 1
if i % 2 == 0:
    print(f'{X}/{i-X+1}')
else:
    print(f'{i-X+1}/{X}')


# 기본 수학 1 - 2869번[달팽이는 올라가고 싶다]
############ 내가 짠 거 -> 시간초과
A, B, V = map(int, input().split())
i = 1
while True:
    V = V - A
    if V <= 0:
        break
    V = V + B
    i += 1
print(i)
############ 인터넷
A, B, V = map(int, input().split())
i = 0
if (V - B) % (A - B) != 0:
    i = ((V - B) // (A - B)) + 1
else:
    i = ((V - B) // (A - B))
print(i)


# 기본 수학 1 - 10250번[ACM호텔]
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    h = N % H
    if h == 0:
        h = H
    if N % H != 0:
        w = N // H + 1
    else:
        w = N // H
    if len(str(w)) == 1:
        print(f'{h}0{w}')
    else:
        print(f'{h}{w}')


# 기본 수학 1 - 2775번[부녀회장이 될테야]
#########내가 짠 코드 -> 런타임 에러
T = int(input())
floor = []
for _ in range(15):
    room = []
    for _ in range(1, 15):
        room.append(_)
    floor.append(room)
for i in range(T):
    k = int(input())
    n = int(input())
    for x in range(1, k+1):
        for y in range(n+1):
            if y == 0:
                floor[x][y] = 1
            else:
                floor[x][y] = floor[x - 1][y] + floor[x][y - 1]
    print(floor[k][n])
########인터넷 참조
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    floor0 = [x for x in range(1, n+1)]
    for x in range(k):
        for y in range(1, n):
            floor0[y] += floor0[y-1]
    print(floor0[-1])


# 기본 수학 1 - 2839번[설탕 배달]
#######인터넷 도움
N = int(input())
bag = 0
while N >= 0:
    if N % 5 == 0:
        bag += (N // 5)
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)


# 기본 수학 1 - 1011번[Fly me to the Alpha Centauri]
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = 1
