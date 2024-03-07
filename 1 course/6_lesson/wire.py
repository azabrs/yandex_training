
def check(seq, m, k):
    count = 0
    for i in seq:
        count += i // m
    return count >= k
def wire(seq, k):
    l = 0
    r = max(seq)
    while l < r:
        m = (r + l + 1) // 2
        if check(seq, m, k):
            l = m
        else:
            r = m - 1
    return l
n, k = list(map(int, input().split()))
print(wire([int(input()) for _ in range(n)], k))
