from itertools import product


def solution(users, emoticons):
    answer = []
    min_sale = min([user[0] for user in users])
    sales = [10, 20, 30, 40]
    sale = []

    for s in sales:
        if s >= min_sale:
            sale.append(s)

    for cwr in product(sale, repeat=len(emoticons)):
        tmp = [0, 0]
        for u in users:
            mid_s = 0
            if max(cwr) >= u[0]:
                for c in range(len(emoticons)):
                    if cwr[c] >= u[0]:
                        mid_s += emoticons[c] * (100-cwr[c]) * 0.01
                if mid_s >= u[1]:
                    tmp[0] += 1
                else:
                    tmp[1] += mid_s
        answer.append(tmp)
    answer.sort(key=lambda x: (x[0], x[1]))

    return answer[-1]


solution([[40, 10000], [25, 10000]], [7000, 9000])