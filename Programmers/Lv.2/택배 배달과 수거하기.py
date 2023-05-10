# def solution(cap, n, deliveries, pickups):
#     dist = 0
#
#     while deliveries and pickups:
#
#         for i in range(len(deliveries)-1, -1, -1):
#             if deliveries[i] == 0 and pickups[i] == 0:
#                 deliveries.pop()
#                 pickups.pop()
#             else:
#                 break
#
#         box = cap
#         d_len = len(deliveries)
#         dist += len(deliveries)
#         for _ in range(len(deliveries)):
#             if box == 0:
#                 break
#             d = deliveries.pop()
#             if box >= d:
#                 box -= d
#             else:
#                 deliveries.append(d - box)
#                 break
#
#         for _ in range(d_len-len(deliveries)):
#             deliveries.append(0)
#
#         blank = 0
#         p_len = len(pickups)
#         dist += len(pickups)
#         for _ in range(len(pickups)):
#             if blank == cap:
#                 break
#             p = pickups.pop()
#             if p > 0:
#                 if p > cap - blank:
#                     blank += cap - blank
#                     pickups.append(p - (cap - blank))
#                     break
#                 else:
#                     blank += p
#
#         for _ in range(p_len-len(pickups)):
#             pickups.append(0)
#
#     return dist
#
#

def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    deli = 0
    pick = 0

    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]

        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (n - i) * 2

    return answer


solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
