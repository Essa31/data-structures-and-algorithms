def sum_series(lst,n):
    ln=len(lst)
    if ln%2==0:
        lst.insert(ln//2,n)
    else:
        lst.insert((ln//2)+1,n)
    return lst
sum_series([42,8,15,23,42], 16)