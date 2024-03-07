def meet(n, k, seq):
    p2 = 1
    res = 0
    for p1 in range(n):
        while p2 < n and seq[p2] - seq[p1] <= k:
            p2 += 1
        res += n - p2
        if n == p2:
            break
    return res
n, k = map(int, input().split())
l = list(map(int,input().split()))
print(meet(n, k, l))