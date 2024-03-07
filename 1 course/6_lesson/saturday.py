def count_brig(m, seq, pep):
    p = 0
    count = 0
    while p + pep - 1 < len(seq):
        if seq[p + pep - 1] - seq[p] <= m:
            count += 1
            p += pep
        else:
            p += 1
    return count
def saturday(n, brig, pep, seq):
    seq = sorted(seq)
    l = 0
    r = seq[-1]
    while l < r:
        m = (l + r) // 2
        if count_brig(m, seq, pep) >= brig:
            r = m
        else:
            l = m + 1
    return l

print(saturday(*(n := list(map(int, input().split()))), [int(input()) for _ in range(n[0])]))