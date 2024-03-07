def count_list(m , param):
    n, x, y = param
    return ((m - x) // y) +  ((m - x) // x) + 1 >= n or ((m - y) // y) +  ((m - y) // x) + 1 >= n 
def easy_task(param):
    n, x, y = param
    l = 0
    r = n * (x + y)
    while l < r:
        m = (l + r) // 2
        if count_list(m, param):
            r = m
        else:
            l = m + 1
    return l
print(easy_task(list(map(int, input().split()))))