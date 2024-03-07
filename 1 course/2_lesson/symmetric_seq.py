def symmetric_seq(seq):
    seq_n = len(seq)
    left = 0
    right = seq_n - 1
    add = 0

    while left < right:
        if seq[left] == seq[right]:
            left += 1
            right -= 1
        else:
            right = seq_n - 1
            left += 1
            add = left
    return str(add), ' '.join(str(i) for i in seq[:add][::-1])

#seq_n = int(input())
#seq = [int(i) for i in input().split()]

print(*symmetric_seq([1, 2, 3, 4, 5, 3, 2, 1]),sep="\n")