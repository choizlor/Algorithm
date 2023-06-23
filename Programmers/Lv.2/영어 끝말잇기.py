def solution(n, words):
    user_num, word_num = 0, 0
    check = {}
    check[words[0]] = 1

    for i in range(1, len(words)):
        user_num = (i % n) + 1
        word_num = (i // n) + 1

        if words[i - 1][-1] != words[i][0]:
            return [user_num, word_num]

        if words[i] in check:
            return [user_num, word_num]
        else:
            check[words[i]] = 1

    return [0, 0]