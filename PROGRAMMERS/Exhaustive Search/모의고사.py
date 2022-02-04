def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        i1, i2, i3 = i % len(one), i % len(two), i % len(three)
        if one[i1] == answers[i]:
            count[0] += 1
        if two[i2] == answers[i]:
            count[1] += 1
        if three[i3] == answers[i]:
            count[2] += 1
    M = max(count)
    answer = [i+1 for i in range(len(count)) if count[i] == M]
    return answer


a = [1, 2, 3, 4, 5]
a1 = [1, 3, 2, 4, 2]
print(solution(a1))
