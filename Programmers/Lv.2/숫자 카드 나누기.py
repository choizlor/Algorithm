def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)


def solution(arrayA, arrayB):
    gcd_A = arrayA[0]
    for a in arrayA:
        gcd_A = gcd(gcd_A, a)

    answerA = gcd_A
    for num in arrayB:
        if num % gcd_A == 0:
            answerA = gcd_A // gcd(num, gcd_A)

    gcd_B = arrayB[0]
    for b in arrayB:
        gcd_B = gcd(gcd_B, b)

    answerB = gcd_B
    for num in arrayA:
        if num % gcd_B == 0:
            answerB = gcd_B // gcd(num, gcd_B)

    if answerA > answerB:
        return answerA
    elif answerA == answerB:
        return 0
    else:
        return answerB


solution([14, 35, 119], [18, 30, 102])