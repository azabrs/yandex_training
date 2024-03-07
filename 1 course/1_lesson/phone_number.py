def checkcode(s):
    l = []
    for i in s:
        if i.isdigit():
            l.append(i)
    if len(l) == 11:
        return l[1:]
    else:
        return ['4','9','5', *l]

l = [checkcode(input()) for i in range(4)]
for i in l[1:]:
    print("YES" if i == l[0] else "NO")