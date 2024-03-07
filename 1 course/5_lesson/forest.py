def forest(n, k, seq):
    dic = {}
    res = [0, -1]
    p2 = 0
    p1 = 0
    while p2 < n:
        while len(dic.keys()) != k and p2 < n:
            dic[seq[p2]] = dic.get(seq[p2], 0) + 1
            p2 += 1
        while len(dic) == k and p1 < p2:
            dic[seq[p1]] -= 1
            if dic[seq[p1]] == 0:
                dic.pop(seq[p1])
            p1 += 1
        if res[1] - res[0] > p2 - p1 or res[1] == -1:
            res = [p1, p2] 
    return res
n, k = map(int, input().split())
l = list(map(int,input().split()))
print(*forest(n, k, l))




