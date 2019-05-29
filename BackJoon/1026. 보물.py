
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
    

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

quickSort(A)
B.sort(reverse=True)

res = 0
for i in range(N):
    res += (A[i]*B[i])

print(res)