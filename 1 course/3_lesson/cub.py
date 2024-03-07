def cub(ann_cub, bor_cub):
    common = ann_cub & bor_cub
    ann_unique = ann_cub - common
    bor_unique = bor_cub - common
    print(len(common), *sorted(common), len(ann_unique), *sorted(ann_unique), len(bor_unique), *sorted(bor_unique),sep="\n")

ann_len, bor_len = map(int, input().split())
ann = set([int(input()) for _ in range(ann_len)])
bor = set([int(input()) for _ in range(bor_len)])
cub(ann, bor)