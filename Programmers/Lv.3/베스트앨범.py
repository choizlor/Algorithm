def solution(genres, plays):
    hash_map = {}
    lst = []
    answer = []

    # 장르, 재생횟수, index
    for i in range(len(genres)):
        lst.append([genres[i], plays[i], i])

    # 장르별로 재생횟수 내림차순으로 정렬
    lst.sort(key=lambda x: (x[0], -x[1]))

    # 장르별로 재생횟수 많은 순으로 정렬
    for i in range(len(genres)):
        if genres[i] in hash_map:
            hash_map[genres[i]] += plays[i]
        else:
            hash_map[genres[i]] = plays[i]
    sortLst = sorted(hash_map.items(), key=lambda x: -x[1])

    # 장르별로 2개씩만
    for s in sortLst:
        cnt = 0
        for l in lst:
            if s[0] == l[0] and cnt < 2:
                answer.append(l[2])
                cnt += 1

    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))
