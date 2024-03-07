def substr(l, n, rep):
    seq = {}
    p1 = 0
    p2 = 0
    res = [-1, 0]
    while p1 < n:
        if l[p1] in seq and seq[l[p1]] == rep:
            while l[p1] != l[p2]:
                seq.pop(l[p2])
                p2 += 1
            seq.pop(l[p2])
            p2 += 1
        else:
            seq[l[p1]] = seq.setdefault(l[p1], 0) + 1
            p1 += 1
        res = max(res, [p1 - p2, p2 + 1], key=lambda x: x[0])

    return res
n, m = list(map(int, input().split()))
l = input()
print(*substr(l, n, m))