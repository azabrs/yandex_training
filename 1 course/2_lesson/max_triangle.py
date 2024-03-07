def Maxim_triangle(first, l):
    prev = first
    dia = [30.0, 4000.0]
    for i in l:
        if i[1] == "closer" and i[0] > prev:
            if dia[0] < ((i[0] + prev) / 2):
                dia[0] = ((i[0] + prev) / 2)
        elif i[1] == "closer" and i[0] < prev:
            if dia[1] > ((i[0] + prev) / 2):
                dia[1] = ((i[0] + prev) / 2)
        elif i[1] == "further" and i[0] > prev:
            if dia[1] > ((i[0] + prev) / 2):
                dia[1] = ((i[0] + prev) / 2)
        elif i[1] == "further" and i[0] < prev:
            if dia[0] < ((i[0] + prev) / 2):
                dia[0] = ((i[0] + prev) / 2)
        prev = i[0]

    return list(map(float, dia))
l = [input().split() for _ in range(int(input()))]
n = float(l[0][0])
l = list(map(lambda x: (float(x[0]),x[1]), l[1:]))
print(*Maxim_triangle(n, l))        

