N = int(input())
arr = list(map(int, input().split()))
arr.sort()
SUM = 0
ln = len(arr)
for i in range(ln,0, -1):
    #print("i : {} calc : {}".format(i, i*arr[ln-i]))
    SUM+=i*arr[ln-i]

print(SUM)