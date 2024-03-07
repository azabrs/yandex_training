def opencalculator(seq, num):
    s_num = set(str(num))
    return len(s_num - seq)

seq = set(input().split())
num = int(input())
print(opencalculator(seq, num))