def merge_sort(arr):

    if len(arr) == 0:
        return 'EMPTY ARRAY'

    elif len(arr) == 1:
        return arr

    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on the left side
        merge_sort(left)
        # Recursive call on the right side
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # set remaining entries in arr to remaining values in left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # set remaining entries in arr to remaining values in right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        # return the sorted array
        return arr
