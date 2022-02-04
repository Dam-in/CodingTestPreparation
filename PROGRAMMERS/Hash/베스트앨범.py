def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += [[i, plays[i]]]
        else:
            dic[genres[i]] = [[i, plays[i]]]
    print(dic)
    # print(dic[max(dic)][0][1])
    while len(dic) > 0:
        maxGenres = max(dic, key=lambda x: max(dic[x][0]))
        print(maxGenres)
        M = max(dic[maxGenres])[0]
        print('M :', M)
        answer.append(M)
        dic[maxGenres].remove(max(dic[maxGenres]))
        if len(dic[maxGenres]) != 0:
            M = max(dic[maxGenres])[0]
            print('m :', M)
            answer.append(M)
        del dic[maxGenres]
    return answer


g = ["classic", "pop", "classic", "classic", "pop"]     # [4, 1, 3, 0]
p = [500, 600, 150, 800, 2500]

g1 = ['c', 'c', 's', 'c', 'c']      # [4, 0, 2]
p1 = [100, 50, 300, 100, 400]
print(solution(g1, p1))




# def solution(genres, plays):
#     answer = []
#     dic = {}
#     for i in range(len(genres)):
#         if genres[i] in dic:
#             dic[genres[i]] += [[plays[i], i]]
#         else:
#             dic[genres[i]] = [[plays[i], i]]
#
#     while len(dic) > 0:
#         # 가장 많이 재생된 장르
#         maxGenres = max(dic)
#
#         # 두 개 찾아서 answer에 넣기
#         M = max(dic[maxGenres])[1]
#         answer.append(M)
#         dic[maxGenres].remove(max(dic[maxGenres]))
#         M = max(dic[maxGenres])[1]
#         answer.append(M)
#
#         # 장르 리스트에서 제거
#         del dic[maxGenres]
#
#     return answer