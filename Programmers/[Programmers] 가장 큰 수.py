def solution(numbers):
    numbers = [str(i) for i in numbers]
    ln = len(numbers)
    quickSort(numbers)
    

    if numbers[0] == "0" :
        return "0"
    else : 
        return"".join(numbers)

def quickSort(arr, start=None, end=None):
    if start != None:
        part2 = partition(arr, start, end)
        if start < part2-1:
            quickSort(arr, start, part2-1)
        if part2 < end:
            quickSort(arr, part2, end)
    else:
        quickSort(arr, 0, len(arr)-1)

def partition(arr, start, end):
    pivot = arr[(start+end)//2]
    while start <= end:
        while(arr[start]+pivot>pivot+arr[start]):start+=1
        while(arr[end]+pivot<pivot+arr[end]): end-=1
        if (start<=end):
            swap(arr, start, end)
            start+=1
            end-=1
    return start

def swap(arr, a, b):
    x = arr[a]
    y = arr[b]
    if x != 0 and y!=0:
        if int(x+y) >= int(y+x):
            return
        else :
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp
            return
    elif x==0:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        return
    else:
        return

print(solution([0,0,0,0]))