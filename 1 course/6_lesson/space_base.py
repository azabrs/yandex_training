def checksize(d, params):
    n, a, b, w, h = params
    return (h // (a + 2 * d)) * (w // (b + 2 * d)) >= n or (w // (a + 2 * d)) * (h // (b + 2 * d)) >= n
def space_base(params):
    n, a, b, w, h = params
    if a >= w and b >= h or a >= h and b >= w:
        return 0
    l = 0
    r = n * (w + h) - 1
    while l < r:
        m = (r + l + 1) // 2
        if checksize(m, params):
            l = m
        else:
            r = m - 1
    return l
print(space_base(list(map(int, input().split()))))