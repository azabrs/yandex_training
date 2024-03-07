def style(trousers, t_shorts):
    p1 = 0
    p2 = 0
    min_sub = -1
    res = []
    while p1 < len(trousers) - 1 or p2 < len(t_shorts) - 1:
        if p1 < len(trousers) - 1 and (trousers[p1] < t_shorts[p2] or p2 == len(t_shorts) - 1):
            p1 += 1
        else:
            p2 += 1
        if min_sub == -1 or min_sub > abs(trousers[p1] - t_shorts[p2]):
            min_sub = abs(trousers[p1] - t_shorts[p2])
            res = [trousers[p1], t_shorts[p2]]
    return res

input()
seq1 = list(map(int, input().split()))
input()
seq2 = list(map(int, input().split()))
print(*style(seq1, seq2))
