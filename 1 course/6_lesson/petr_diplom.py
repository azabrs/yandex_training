def checksize(m, params):
    w, h, n = params
    return (m // w) * (m // h) >= n
def petr_diplom(params):
    w, h, n = params
    l = 1
    r = n * (w + h) - 1
    while l < r:
        m = (r + l) // 2
        if checksize(m, params):
            r = m
        else:
            l = m + 1
    return l
print(petr_diplom(list(map(int, input().split()))))