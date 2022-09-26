def merge(lLst, rLst):
    lp = rp = 0
    result = []
    while lp < len(lLst) and rp < len(rLst):
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])
            lp += 1
        else:
            result.append(rLst[rp])
            rp += 1
    result.extend(lLst[lp:])
    result.extend(rLst[rp:])
    return result


def merge_s(lst):
    global cnt
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = merge_s(lst[:mid])
    right = merge_s(lst[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_s(arr)
    print(f'#{tc} {result[N//2]} {cnt}')