def solution(answers):
    answer = [0 for i in range(3)]
    
    math1 = [1, 2, 3, 4, 5]
    math2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for a in range(len(answers)):
        if answers[a] == math1[a % 5]:
            answer[0] += 1
        if answers[a] == math2[a % 8]:
            answer[1] += 1
        if answers[a] == math3[a % 10]:
            answer[2] += 1
    
    result = []
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i+1)
    
    return sorted(result)