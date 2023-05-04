def solution(s):
    minN, maxN = 0, 0
    num = s.split(' ')
    numbers = []

    for i in num:
        numbers.append(int(i))

    minN = min(numbers)
    maxN = max(numbers)

    return f'{minN} {maxN}'
