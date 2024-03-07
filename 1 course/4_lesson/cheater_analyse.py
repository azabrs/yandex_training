import re
def cheater_analyse(C, D, key_val, lines):
    key_val = set(key_val)
    idenf = {}
    pos = {}
    count = 0 
    for line in lines:
        s = ""
        if C == "yes":           
            line = "".join([i if (i.isalnum() or i == "_") else " " for i in line ]).split()
        else:
            line = "".join([i if (i.isalnum() or i == "_") else " " for i in line ]).lower().split()
        for word in line:
            if  word not in key_val and not (word[0].isdigit() and(D == "no" or  len(word) == 1) ) :
                if word in idenf:
                    idenf[word] += 1
                else:
                    idenf[word] = 1
                    pos[word] = count
            count += 1
    res = None
    max_count = -1
    min_pos = -1
    for item, count in idenf.items():
        if min_pos == -1 or res == None or max_count < count:
            max_count = count
            min_pos = pos[item] 
            res = item
        elif max_count == count and pos[item] < min_pos:
            min_pos = pos[item] 
            res = item
    return res
def input_parser(l):
    n, C, D = l[0].split() 
    if C == "no":
        key_val = [i.lower().strip() for i in l[1:int(n) + 1]]
    else:
        key_val = [i.strip() for i in l[1:int(n) + 1]]
    code = l[int(n) + 1:]
    return C, D, key_val, code

inf = open("input.txt")
print(cheater_analyse(*input_parser(inf.readlines())))
