import random
import math

def gete(flatno, flatsonfloor, floors):
    floorsbefore = (flatno - 1) // flatsonfloor
    entrance = floorsbefore // floors + 1
    floor = floorsbefore % floors + 1
    return entrance, floor

def check(k1, m, k2, p2, n2, flatsonfloor):
    entrance2, floor2 = gete(k2, flatsonfloor, m)
    if entrance2 == p2 and floor2 == n2:
        return gete(k1, flatsonfloor, m)
    return -1, -1

def test(k1, m, k2, p2, n2):
    ent = -1
    floor = -1
    goodflag = False
    for flatsonfloor in range(1,11):
        nent, nfloor = check(k1, m, k2, p2, n2, flatsonfloor)
        if nent != -1:
            goodflag = True
            if ent == -1:
                ent, floor = nent, nfloor
            elif ent != nent and ent != 0:
                ent = 0
            elif floor != nfloor and floor !=0:
                floor = 0
    if goodflag:
        return(ent,floor)
    else:
        return (-1, -1)


def fastskor(k1, m, k2, p2, n2):
    p_by_n = math.ceil(k2 / ((p2 - 1) * m + n2))
    p1 = math.ceil(k1 /(m * p_by_n))
    n1 = math.ceil((k1 - m * (p1 - 1) * p_by_n) / p_by_n)
    cond1 = k1 > p_by_n
    cond2 = ((m * (p2 - 1) * (p_by_n + 1) + (p_by_n + 1) * (n2 - 1)) < k2 and k2 <  (m * (p2 - 1) * (p_by_n + 1) + (p_by_n + 1) * (n2)))
    cond3 = k1 != k2 
    if (n1 > m or n2 > m or ((m * (p2 - 1) * p_by_n + p_by_n * (n2 - 1)) >= k2)
    or (k2 > (m * p2 * p_by_n))):
        return(-1, -1)
    elif (cond1 and cond2  and cond3):
        p_by_n_orig = p_by_n
        full = True
        only_p = True
        only_n = True
        empty = True
        while ((m * (p2 - 1) * (p_by_n + 1) + (p_by_n + 1) * (n2 - 1)) < k2 and k2 <  (m * (p2 - 1) * (p_by_n + 1) + (p_by_n + 1) * (n2))):
            p_by_n += 1
            p1_new = math.ceil(k1 /(m * p_by_n))
            n1_new = math.ceil((k1 - m * (p1_new - 1) * p_by_n) / p_by_n)
            if p1_new != p1:
                only_p = False
                full = False
            if n1_new != n1:
                only_n = False
                full = False
            if p_by_n == 4 * p_by_n_orig or  not only_n and  not full and not only_p:
                break
        if full:
            return p1, n1
        if only_p or n1 != n1_new and p1 == p1_new:
            return p1, 0
        if only_n or p1_new != p1 and n1_new == n1:
            return 0, n1  
        if m == 1:
            return 0, 1
        elif (p_by_n_orig) * m > k1:
            return 1, 0
        else:
            return 0, 0
    return p1, n1
#print(fastskor(11, 1, 1, 1, 1))
#print(fastskor(8, 9, 9, 1, 5))
#WA (-1, -1) (1, 4)
#print(fastskor(5, 5, 9, 2, 5))
#WA (1, 5) (-1, -1)
#print(fastskor(6, 2, 4, 1, 2))
#WA (-1, -1) (0, 1)
#print(fastskor(5, 5, 6, 1, 3))
#WA (1, 2) (1, 3)
#print(fastskor(4, 9, 6, 1, 2))
#WA (1, 2) (1, 0)
#print(*fastskor(9, 2, 4, 1, 2))
#WA (0, 0) (0, 1)
while True:
    randvals = [0] * 5
    for i in range(5):
        randvals[i] = random.randint(1, 10)
    k1, m, k2, p2, n2 = randvals
    print(*randvals)
    slowans = test(k1, m, k2, p2, n2)
    fast = fastskor(k1, m, k2, p2, n2)

    if slowans == fast:
        print("OK")
    else:
        print('WA', fast, slowans)
        break