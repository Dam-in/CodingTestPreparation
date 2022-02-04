def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack, end = [], []

    l = len(truck_weights)
    while len(end) != l:
        if len(truck_weights) > 0:
            if len(stack) == bridge_length:
                if sum(stack)-stack[0]+truck_weights[0] <= weight:
                    if stack[0] != 0:
                        end.append(stack.pop(0))
                    stack.append(truck_weights.pop(0))
                else:
                    if stack[0] != 0:
                        end.append(stack.pop(0))
                    stack.append(0)
            else:
                if sum(stack)+truck_weights[0] <= weight:
                    stack.append(truck_weights.pop(0))
                else:
                    stack.append(0)
            answer += 1
        else:
            if len(stack) == bridge_length:
                if stack[0] != 0:
                    end.append(stack.pop(0))
                    answer += 1
    return answer

b = 2               # 8
w = 10
t = [7, 4, 5, 6]

b1 = 100            # 101
w1 = 100
t1 = [10]

b2 = 100            # 110
w2 = 100
t2 = [10,10,10,10,10,10,10,10,10,10]

print(solution(b, w, t))