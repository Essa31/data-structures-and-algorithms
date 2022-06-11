def BinarySearch(arr,n):
   begin=0
   end =len(arr)-1
   while begin <= end :
        mid=  begin+(end-begin)//2
        mid_value=arr[mid]
        if mid_value == n:
            return mid
        elif mid_value>n:
            end=mid-1
        else:
            begin=mid+1
   return -1



print(BinarySearch([4, 8, 15, 16, 23, 42], 34))



