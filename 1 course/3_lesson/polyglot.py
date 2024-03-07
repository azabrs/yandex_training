l = [[input() for i in range(int(input()))] for _ in range(int(input()))]
inter = set(l[0])
union = set(l[0])
for i in range(1, len(l)):
    inter &= set(l[i])
    union |= set(l[i])
print(len(inter))
print(*inter, sep="\n")
print(len(union))
print(*union, sep="\n")