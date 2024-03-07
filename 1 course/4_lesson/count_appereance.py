def count_appereance(text):
    l = text.split()
    res = {}
    for i in l:
        res[i] = res.get(i, -1) + 1
        print(res[i], end=" ")
infile = open("input.txt")
count_appereance(infile.read())