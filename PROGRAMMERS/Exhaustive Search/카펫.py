def solution(brown, yellow):
    b = (brown - 4) // 2
    a = b // 2 + 1 if b % 2 != 0 else b // 2
    for i in range(a, b):
        if i * (b-i) == yellow:
            return [i+2, b-i+2]




b, y = 10, 2    # [4, 3]
b1, y1 = 8, 1   # [3, 3]
b2, y2 = 24, 24 # [8, 6]

print(solution(b, y))

