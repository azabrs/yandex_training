def checking_test(gram, text):
    dic = set()
    dic_low = set()
    for word in gram:
        dic.add(word)
        dic_low.add(word.lower())
    count = 0
    for word in text.split():
        if (word.lower() in dic_low and word not in dic) or (word.lower() not in dic_low and len(list(filter(lambda x : x.isupper(), word))) != 1):
            count += 1
    return count
l = [input() for i in range(int(input()))]
print(checking_test(l, input()))
