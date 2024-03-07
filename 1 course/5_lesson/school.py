def school(n, cond_need, m, cond_have):
    cond_need.sort()
    cond_have.sort(key=lambda x: (x[1]))
    res = 0
    p1 = 0
    p2 = 0
    for p1 in cond_need:
        while p1 > cond_have[p2][0]:
            p2 += 1
        else:
            res += cond_have[p2][1]
    return res
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = [tuple(map(int, input().split())) for _ in range(m)]
print(school(n, a, m, b))
                