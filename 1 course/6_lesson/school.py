def check(m, cur_sum, cur_len):
    return cur_sum + m * 5 >= 3.5 * (cur_len + m)
def school_mark(two, three, four):
    l = 0
    cur_sum = sum([two * 2, three * 3, four * 4])
    r = cur_len = sum([two, three, four])
    while l < r:
        m = (l + r) // 2
        if check(m, cur_sum, cur_len):
            r = m
        else:
            l = m + 1
    return l
print(school_mark(*map(int, [input() for i in range(3)])))