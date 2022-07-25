def insertion_sort(arr):
    """
    this function will take an array of integers and return it in sorted order
    """
    if len(arr) == 0:
        return 'EMPTY ARRAY'
    elif len(arr) == 1:
        return arr
    else:
        for i in range(1, len(arr)):
            j = i - 1
            temp = arr[i]

            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1

            arr[j + 1] = temp

        return arr