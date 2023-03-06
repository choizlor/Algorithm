def solution(s):
    test = 0
    answer = [0, 0]
    lst = list(s)

    while lst != ["1"]:
        arr_new = [i for i in lst if i != '0']
        num = len(arr_new)
        answer[1] += len(lst) - num
        lst = list(format(num, 'b'))
        answer[0] += 1
    return answer

print(solution("0111010"))