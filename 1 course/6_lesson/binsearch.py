def binsearch(seq, k):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = (l + r) // 2
        if seq[m] > k:
            r = m
        elif seq[m] < k:
            l = m + 1
        else:
            return True
    return True if k == seq[l] else False
def solve(n, k, seq1, seq2):
    for elem in seq2:
        print("YES" if binsearch(seq1, elem) else "NO")
n, k = map(int, input().split())
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))
solve(n, k, seq1, seq2)