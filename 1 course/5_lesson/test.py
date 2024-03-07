def school(n, cond_need, m, cond_have):
    cond_need = sorted(cond_need, reverse=True)
    cond_have = sorted(cond_have, key=lambda x: (x[0], x[1]),reverse=True)
    res = [0] * n
    p1 = n - 1
    p2 = m - 1
    while p1 > 0:
        while cond_need < 
    