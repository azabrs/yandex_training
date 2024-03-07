def checkers(seq, n, max_dif):
    p2 = 0
    res = 0
    uniq = {}
    dupl = 0
    for elem in seq:
         uniq[elem] = uniq.get(elem, 0) + 1
    uniq_key = sorted(uniq.keys())
    for p1 in range(len(uniq_key)):
        while p2 < len(uniq_key) and uniq_key[p1] * max_dif >= uniq_key[p2]:
            if uniq[uniq_key[p2]] > 1:
                dupl += 1
            p2 += 1
        range_len = p2 - p1
        if uniq[uniq_key[p1]] > 1:
            res += (range_len - 1) * 3
            dupl -= 1
        if uniq[uniq_key[p1]] > 2:
            res += 1
        res += (range_len - 2) * (range_len - 1) * 3
        res += dupl * 3


    return res
n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
print(checkers(l, n, m))
