import math
def laptop_place(a1, b1, a2, b2):
    l1 = sorted([a1, b1]) 
    l2 = sorted([a2, b2]) 
    max_l, min_l = (l1, l2) if l1[1] > l2[1] else (l2, l1) 
    if min_l[1] <= max_l[0]:
        return max_l[1] + min_l[0], max_l[0]
    else:
        return max_l[1], min_l[0] + max_l[0]

a1, b1, a2, b2 = map(int, input().split())
print(*laptop_place(a1, b1, a2, b2))