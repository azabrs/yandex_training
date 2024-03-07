def intersec_set(s1, s2):
    return sorted(s1 & s2)
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(*intersec_set(s1, s2))