def prisoner_if(a, b, c, d, e):
    if a <= d and b <= e or a <= e and b <= d:
        return "YES"
    elif c <= d and b <= e or c <= e and b <= d:
        return "YES"
    elif a <= d and c <= e or a <= e and c <= d:
        return "YES"
    else:
        return "NO"

a, b, c, d, e = map(int,[input() for i in range(5)])
print(prisoner_if(a, b, c, d, e))