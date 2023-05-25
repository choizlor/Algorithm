# # 중복 순열로 푸는 방법
# from itertools import product
#
#
# def solution(word):
#     cnt = 0
#     words = []
#     for i in range(1, 6):
#         for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
#             words.append(''.join(list(p)))
#     words.sort()
#     return words.index(word) + 1

# dfs로 푸는 방법
def solution(word):
    word_list = []
    words = 'AEIOU'

    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            word_list.append(w + words[i])
            dfs(cnt + 1, w + words[i])

    dfs(0, "")

    return word_list.index(word) + 1


solution("AAAAE")