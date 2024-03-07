def nearest_number(l, val):
    diff = 2001
    for i in l:
        if abs(val - i) < abs(diff):
            diff = val - i
    return val - diff

input()
l = map(int, input().split())
val = int(input())
print(nearest_number(l, val))