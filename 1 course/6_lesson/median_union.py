import random as rand
def median_union(seq):
    res_res = []
    n = len(seq)
    m = len(seq[0])
    for i in range(n - 1):
        for j in range(i + 1, n):
            p1 = p2 = 0
            last = None
            while p1 + p2 < m:
                if p1 < m and (p2 == m or seq[i][p1] < seq[j][p2]):
                    last = seq[i][p1]
                    p1 += 1
                else:
                    last = seq[j][p2]
                    p2 += 1
            res_res.append(last)
    return res_res

n, m = list(map(int, input().split()))   
print(*median_union([list(map(int, input().split())) for i in range(n)]))

