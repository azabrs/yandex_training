def count_diff_number(l):
    return len(set(l))
l = list(map(int, input().split()))
print(count_diff_number(l))