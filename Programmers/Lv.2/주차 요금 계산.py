import math


def solution(fees, records):
    answer = {}
    times = []
    nums = []
    result = []

    for r in range(len(records)):
        time, num, state = records[r].split(" ")    # 시간, 차 번호, IN/OUT
        hour, minute = time.split(":")
        t = int(hour) * 60 + int(minute)    # 시간을 분으로 바꾸기

        if num in nums: # 차가 IN한 상태면
            idx = nums.index(num)   # 차 idx 구하기
            answer[num] += t - times[idx]   # idx에 맞는 시간 구하기
            times.pop(idx)  # OUT한 차 제거하기
            nums.pop(idx)

        else:
            if num not in answer:   # 한번도 들어온 적 없는 차 0으로 넣어주기
                answer[num] = 0
            times.append(t)
            nums.append(num)

    for n in range(len(nums)):  # OUT 안 한 차 처리
        answer[nums[n]] += 1439 - times[n]

    sort_data = sorted(answer.items())  # 차 번호 낮은 순대로

    for v in sort_data: # 주차 요금 정산
        if v[1] <= fees[0]:
            result.append(fees[1])
        else:
            result.append(fees[1] + math.ceil((v[1] - fees[0]) / fees[2]) * fees[3])

    return result


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])