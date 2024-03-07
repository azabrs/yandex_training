def mount_trace(seq, n, traces, m):
    pref_summ_straight = (n) * [0]
    pref_summ_rev = (n) * [0]
    for i in range(1, n):
        if (seq[i][1] - seq[i - 1][1]) > 0:
            pref_summ_straight[i] = pref_summ_straight[i - 1] + (seq[i][1] - seq[i - 1][1])
            pref_summ_rev[i] = pref_summ_rev[i - 1]
        else:
            pref_summ_straight[i] = pref_summ_straight[i - 1]
            pref_summ_rev[i] = pref_summ_rev[i - 1] - (seq[i][1] - seq[i - 1][1])
    res = []
    print(pref_summ_straight)
    print(pref_summ_rev)
    for start, finish in traces:
        if finish > start:
            res.append(pref_summ_straight[finish - 1] - pref_summ_straight[start - 1])
        else:
            res.append(pref_summ_rev[start - 1] - pref_summ_rev[finish - 1])
    return res
n = int(input())
l1 = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
l2 = [tuple(map(int, input().split())) for _ in range(m)]
print(*mount_trace(l1, n, l2, m), sep='\n')

