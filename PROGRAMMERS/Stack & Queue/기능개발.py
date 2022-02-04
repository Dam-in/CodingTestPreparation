def solution(progresses, speeds):
    day = []
    answer = []
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        if rest % speeds[i] == 0:
            temp = rest // speeds[i]
        else:
            temp = rest // speeds[i] + 1
        day.append(temp)
    print(day)

    count = 1
    for l in range(len(day)-1):
        try:
            if max(day[l-count+1:l]) < day[l+1]:
                answer.append(count)
                count = 1
            else:
                count += 1
        except:
            if day[l] < day[l + 1]:
                answer.append(count)
                count = 1
            else:
                count += 1
    answer.append(count)
    return answer


p1 = [93, 30, 55]  # [2, 1]
s1 = [1, 30, 5]

p2 = [95, 90, 99, 99, 80, 99]  # [1, 3, 2]
s2 = [1, 1, 1, 1, 1, 1]

p3 = [90, 91, 92, 93]  # [4]
s3 = [1, 1, 1, 1]

p4 = [4, 3, 2, 1]  # [1, 1, 1, 1]
s4 = [1, 1, 1, 1]

p5 = [20, 99, 93, 30, 55, 10]  # [3, 3]
s5 = [5, 10, 1, 1, 30, 5]

p6 = [96, 99, 98, 97]  # [4]
s6 = [1, 1, 1, 1]

p7 = [99, 98, 97, 96, 95]  # [1, 1, 1, 1, 1]
s7 = [1, 1, 1, 1, 1]

p8 = [40, 93, 30, 55, 60, 65]  # [1, 2, 3]
s8 = [60, 1, 30, 5, 10, 7]

p9 = [90, 98, 94, 100]  # [4]
s9 = [1, 1, 1, 1]

print(solution(p8, s8))
