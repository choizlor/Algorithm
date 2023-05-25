def solution(begin, target, words):
    answer = 0
    q = []
    q.append([begin, 0])
    visited = [0 for _ in range(len(words))]

    while q:
        word, cnt = q.pop()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            tmp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = 1

    return answer