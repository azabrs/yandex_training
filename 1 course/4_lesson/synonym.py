def synonym(l, key):
    dic = {}
    dic_rev = {}
    for first, last in l:
        dic[first] = last
        dic_rev[last] = first
    if dic_rev.get(key) != None:
        return dic_rev.get(key)
    if dic.get(key) != None:
        return dic.get(key)
l = [input().split() for i in range(int(input()))]
key = input()
print(synonym(l, key))        