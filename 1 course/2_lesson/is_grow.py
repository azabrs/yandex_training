def is_grow(l):
    prev = l[0]
    for i in l[1:]:
        if i <= prev:
            return "NO"
        prev = i
    else:
        return "YES"

l = list(map(int,input().split()))
print(is_grow(l))
