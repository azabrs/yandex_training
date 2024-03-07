def type_of_seq(l):
    prev = l[0]
    list = ["CONSTANT", "ASCENDING", "WEAKLY ASCENDING", "DESCENDING", "WEAKLY DESCENDING", "RANDOM"]
    for i in l[1:]:
        if "CONSTANT" in list and i != prev:
            list.remove("CONSTANT")
        if "ASCENDING" in list and i <= prev:
            list.remove("ASCENDING")
        if "WEAKLY ASCENDING" in list and i < prev:
            list.remove("WEAKLY ASCENDING")
        if "DESCENDING" in list and i >= prev:
            list.remove("DESCENDING")
        if "WEAKLY DESCENDING" in list and i > prev:
            list.remove("WEAKLY DESCENDING")

        prev = i
    return list[0]

def input_parser():
    val = int(input())
    l = [val]
    while val != -2*10**(9):
        val = int(input())
        l.append(val)
    l.pop(-1)
    return l

print(type_of_seq(input_parser()))