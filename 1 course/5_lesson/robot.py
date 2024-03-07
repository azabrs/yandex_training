def robot(k, oper):
    p1 = 0
    n = len(oper)
    p2 = k
    res = 0
    i = 0
    while p1 < n - k:
        i = 0
        while p2 < n and oper[p2] == oper[p1]:
            res = res + 1 + i
            i = i + 1
            p1 += 1
            p2 += 1
        p1 += 1
        p2 = p1 + k
        i = 0
    return res
print(robot(int(input()), input()))