def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        new_array = array[i-1:j]
        answer.append(sorted(new_array)[k-1])
    return answer

a = [1, 5, 2, 6, 3, 7, 4]               # [5, 6, 3]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(a, c))