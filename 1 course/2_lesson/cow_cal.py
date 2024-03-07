import random
def cow_cal(l):
    max_ind = -1
    max = -1
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
            max_ind = i
    if max ==  -1:
        return 0
    ans = -1
    for i in range(max_ind + 1, len(l) - 1):
        if l[i] > l[i + 1] and l[i] % 5 == 0 and l[i] % 10 != 0 and l[i] > ans:
            ans = l[i]
    if ans == -1:
        return 0
    sor = sorted(l,reverse=True)
    high_pos = sor.index(ans)
    return high_pos + 1
input()
l = list(map(int, input().split()))


print(cow_cal(l))

