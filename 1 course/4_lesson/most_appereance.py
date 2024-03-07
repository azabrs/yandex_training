def most_appereance(words):
    l = words.split()
    res = {}
    for word in l:
        res[word] = res.get(word, 0) + 1
    return min(res, key=lambda x:(-res[x], x))
infile = open("input.txt")
print(most_appereance(infile.read()))