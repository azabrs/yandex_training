def max_prod_3(l):
    l.sort()
    if l[0] * l[1] * l[-1] > l[-3] * l[-2] * l[-1]:
        return l[0], l[1], l[-1]
    else:
        return l[-3], l[-2], l[-1]

l = list(map(int,input().split()))
print(*max_prod_3(l))