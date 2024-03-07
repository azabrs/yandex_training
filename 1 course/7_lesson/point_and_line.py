def point_and_line(lines, points):
    l = []
    p = 0
    for line in lines:
        l.append((min(line), 0))
        l.append((max(line), 2))
    for point in points:
        l.append((point, 1, p))
        p += 1
    count_otr = 0
    res = [0] * len(points)
    l.sort()
    for coord in l:
        if coord[1] == 0:
            count_otr += 1
        elif coord[1] == 1:
            res[coord[2]] = count_otr
        elif coord[1] == 2:
            count_otr -= 1
    return res
n, m = list(map(int, input().split()))
print(*point_and_line([list(map(int, input().split())) for _ in range(n)], list(map(int, input().split()))))

