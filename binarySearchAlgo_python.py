arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def binarySearch(target,arr)->int:
    
    start=0
    end=len(arr)-1
    index=0
    
    def bsa(target, start, end):
        nonlocal index
        if (start>end):
            raise Exception(str(target) + " is not in list")

        middle = int((start+end)/2)

        if arr[middle]==target:
            index=middle

        if(arr[middle]>target):
            bsa(target, start, middle-1)

        if(arr[middle]<target):
            bsa(target, middle+1, end)

    try:
        bsa(target, start, end)
    except Exception as e:
        return str(e)
        
    return index

print(binarySearch('t', arr))
print(binarySearch('b', arr))
