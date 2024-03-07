from functools import reduce
def turtle(count_turtle, data):
    count = 0
    s = set()
    for forw, back in data:
        if forw + back == count_turtle - 1 and forw >= 0 and back >= 0 and (forw, back) not in s:
            count += 1
        s.add((forw, back))
    return count
count_turtle = int(input())
s = set()
data = [list(map(int, input().split())) for i in range(count_turtle)]
print(turtle(count_turtle, data))