from collections import Counter
def solution(participant, completion):
    result = list(Counter(participant) - Counter(completion))
    return result[0]


###
def solution(participant, completion):
    dic1 = {}
    dic2 = {}
    for x in participant:
        if x in dic1:
            dic1[x] += 1
        else:
            dic1[x] = 1
    for y in completion:
        if y in dic2:
            dic2[y] += 1
        else:
            dic2[y] = 1
    for i in dic1:
        if i in dic2:
            if dic1[i] > dic2[i]:
                return i
        else:
            return i