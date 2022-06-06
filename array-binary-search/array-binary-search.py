def BinarySearch(lst,n):
    if n in lst:
        for i in range(len(lst)):
            if lst[i]==n:
                return i
    else:
        return -1

print (BinarySearch([1, 2, 3, 5, 6, 7], 4))