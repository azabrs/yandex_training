def appr_binsearch(seq, k):
    l = 0
    r = len(seq) - 1
    if k <= seq[0]:
        return seq[0]
    if k > seq[len(seq) - 1]:
        return seq[len(seq) - 1]
    while l < r:
        m = (l + r) // 2
        if r - l == 1:
            if abs(seq[l] - k) > abs(seq[r] - k):
                return seq[r]
            else:
                return seq[l]
        if seq[m] > k:
            r = m
        elif seq[m] < k:
            l = m
        else:
            return k
    return seq[l]
def solve(n, k, seq1, seq2):
    for elem in seq2:
        print(appr_binsearch(seq1, elem))
n, k = map(int, input().split())
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))
solve(n, k, seq1, seq2)