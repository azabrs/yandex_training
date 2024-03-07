a, b, c = [int(input()) for i in range(3)]
if c < 0:
    print("NO SOLUTION")
elif a == 0:
    print("MANY SOLUTIONS")
else:
    if a != 0 and (c * c - b) / a == (c * c - b) // a:
        print((c * c - b) // a)
    else:
        print("NO SOLUTION")