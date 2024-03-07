def Manh_walk(t, d, l):
    cp = [[0, 0],[0, 0]] #min x-y max x - y min x + y max x + y
    pn = [[0, 0],[0, 0]]
    for i in l:
        cp = [[cp[0][0] - t, cp[0][1] + t], [cp[1][0] - t, cp[1][1] + t]]
        pn = [[i[0] + i[1] - d, i[0] + i[1] + d], [i[0] - i[1] - d, i[0] - i[1] + d]]
        cp = [[max(pn[0][0], cp[0][0]), min(pn[0][1], cp[0][1])], [max(pn[1][0], cp[1][0]), min(pn[1][1], cp[1][1])]]
    points = []
    for xplusy in range(cp[0][0], cp[0][1] + 1):
        for xminusy in range(cp[1][0], cp[1][1] + 1):
            if (xplusy + xminusy) % 2 == 0:
                x = (xplusy + xminusy) // 2
                y = xplusy - x
                points.append((x, y))
    print(len(points)) 
    for i in points:
        print(*i)

        
t, d, n = map(int, input().split())
l = [tuple(map(int, input().split())) for i in range(n)]
Manh_walk(t, d, l),