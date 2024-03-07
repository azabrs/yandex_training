def Mayan_writing(g, S):
    word = {}
    seq = {}
    for i in range(len(g)):
        word[g[i]] = word.setdefault(g[i], 0) + 1
        seq[S[i]] = seq.setdefault(S[i], 0) + 1
    if word == seq:
        res = 1
    else:
        res = 0
    for i in range(len(g), len(S)):
        start_seq = S[i - len(g)]
        seq[start_seq] -= 1
        if seq[start_seq] == 0:
            seq.pop(start_seq)
        seq[S[i]] = seq.setdefault(S[i], 0) + 1
        if word == seq:
            res += 1

    return res
input()
print(Mayan_writing(input(), input()))
