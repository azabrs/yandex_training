def seat(students, d):
    dic = {}
    stud_sort = sorted(students)
    dic[stud_sort[0]] = 1
    for i in range(1, len(stud_sort)):
        if stud_sort[i]  <= stud_sort[i - 1] + d:
            dic[stud_sort[i]] = dic[stud_sort[i - 1]] + 1
        else:
            dic[stud_sort[i]] = 1
    print(max(dic.values()))
    for s in students:
        print(dic[s],end=' ')
    
n, d = list(map(int, input().split()))
seat(list(map(int, input().split())), d)

