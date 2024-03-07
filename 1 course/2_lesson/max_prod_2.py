
def max_prod_2(l):
    first_elem_p = max(l[0], l[1])
    second_elem_p = min(l[0], l[1])
    first_elem_n = min(l[0], l[1])
    second_elem_n = max(l[0], l[1])
    for i in l[2:]:
        if i > 0:
            if i >= first_elem_p:
                second_elem_p = first_elem_p
                first_elem_p = i
            elif i >= second_elem_p:
                second_elem_p = i
        else:
            if i <= first_elem_n:
                second_elem_n = first_elem_n
                first_elem_n = i
            elif i <= second_elem_n:
                second_elem_n = i                    
        
    return max((second_elem_p,first_elem_p), (first_elem_n, second_elem_n),key=lambda x: x[0] * x[1])

l = list(map(int,input().split()))
print(*max_prod_2(l))
