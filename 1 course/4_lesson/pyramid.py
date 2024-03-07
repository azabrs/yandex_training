def pyramid(coor):
    temp = {}
    for w, h in coor:
        if h > temp.setdefault(w, 0):
            temp[w] = h
    res = 0
    for key in temp:
        res += temp[key]
    return res
l = [list(map(int, input().split())) for i in range(int(input()))]
print(pyramid(l))