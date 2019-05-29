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

def bubbleSort(arr):
    size = len(arr)
    
    cnt = 0
    for i in range(size):
        
        for j in range(size-1):
            cnt+=1
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# 퀵정렬 O(N*logN)
# pivot 을 맨 앞의 값으로 설정

'''
def quickSort(arr, start=None, end=None):
    if start==None:
        quickSort(arr, 0, len(arr)-1)
    else:
        part = partition(arr, start, end)
        if start < part -1 :
            quickSort(arr, start, part-1)
        if part < end :
            quickSort(arr, part, end)
        
def partition(arr, start, end):
    pivot = arr[start]
    
    while start <= end:
        while arr[start] > pivot: start += 1
        while arr[end] < pivot : end -= 1
        if start <= end :
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start +=1
            end -=1
    return start
'''


def quickSort(arr, start=None, end=None):
    if start==None:
        quickSort(arr, 0, len(arr)-1)
    else:
        part = partition(arr, start, end)
        if start < part :
            quickSort(arr, start, part-1)
        if part < end :
            quickSort(arr, part, end)

def partition(arr, start, end):
    pivot = arr[start]
    while start < end :
        while arr[start] < pivot: start+=1
        while arr[end] > pivot: end-=1
        if start <= end :
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1
    return start
        

    


print(insertionSort([2,5,3,7,3,2]))
print(selectSort([1,5,3,2,6,7,10,2]))
print(bubbleSort([1,3,5,2,36]))
a = [10,9,13,3,6,5,4,3,2,1]
quickSort(a)
print(a)