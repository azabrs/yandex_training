def graduate(students, teacher, seq):
    lines = []
    for s in seq:
        lines.append((s[0], 0))
        lines.append((s[1], 1))
    lines.sort()
    res = 0
    count_teacher = 0
    for line in  range(len(lines)):
        if line == 0:
            res += lines[line][0]
            count_teacher += 1
        elif lines[line][1] == 0:
            if count_teacher == 0 and line != 0:
                res += lines[line][0] - lines[line - 1][0] - 1
            count_teacher += 1
        
        elif lines[line][1] == 1:
            count_teacher -= 1
            if count_teacher == 0 and line == len(lines) - 1:
                res += (students - 1 - lines[line][0]) 
    return res
n, k = list(map(int, input().split()))
print(graduate(n, k, [tuple(map(int, input().split())) for i in range(k)]))