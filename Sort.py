def insertionSort(arr):
    size = len(arr)
    if size < 1:
        return arr
    for i in range(size-1):
        j = i
        while arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j-=1
    return arr

def selectSort(arr):
    size = len(arr)
    
    if size < 1:
        return arr
    MAX = max(arr)
    idx = None

    for i in range(size):
        MIN = MAX     
        for j in range(i, size):
            if MIN>arr[j]:
                MIN = arr[j]
                idx = j
        
        temp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = temp
        
    return arr

        
    

print(insertionSort([2,5,3,7,3,2]))
print(selectSort([1,5,3,2,6,7,10,2]))