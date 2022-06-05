def sum_series(lst,n):
    ln=len(lst)
    if ln%2==0:
       x = lst[:((ln//2))]
       y =lst[((ln//2)):]
       new_lst= x + [n]  + y
    else:
        x = lst[:(ln // 2)+1 ]
        y = lst[(ln // 2)+1 :]
        new_lst = x + [n] + y
    return new_lst
print (sum_series([42,8,15,23,42], 16))