def summ_number(seq, n, key):
    pref_str = [0] * (n + 1)
    for i in range(1, n + 1):
        pref_str[i] = pref_str[i - 1] + seq[i - 1]
    p1 = res = cur_sum = 0
    p2 = 1
    res = 0
    cur_sum = 0
    while p2 < len(pref_str):
        if pref_str[p2] - pref_str[p1] < key:
            cur_sum += pref_str[p2]
            p2 += 1
        elif pref_str[p2] - pref_str[p1] > key:
            cur_sum -= pref_str[p1]
            p1 += 1
        else:
            cur_sum += pref_str[p2]
            p2 += 1
            res += 1
    return res
n, k = map(int, input().split())
l = list(map(int,input().split()))
print(summ_number(l, n, k))