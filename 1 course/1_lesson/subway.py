def subway(a, b, n, m):
    max_first = a * (n + 1) + n
    min_first = a * (n - 1) + n 
    max_second = b * (m + 1) + m
    min_second = b * (m - 1) + m
    left = max(min_first, min_second)
    right = min(max_first,max_second)
    ans = [-1] if right < left else (left, right)
    return ans
a, b, n, m = map(int, [input() for i in range(4)])
print(*subway(a, b, n, m))