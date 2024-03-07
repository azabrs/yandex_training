def test(seq, n):
    p1 = n - 1
    p2 = n - 2
    res = []
    while p1 > 0:
        while seq[p2] + seq[p2 + 1] > seq[p1]:
            p2 -= 1
        res = seq[p2:p1 + 1]
        p1 -= 1
    return res
print(test([1, 1, 3, 3, 4, 6, 11], 7))