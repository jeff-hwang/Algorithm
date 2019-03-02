inData = input().split(' ')

a = int(inData[0])
b = int(inData[1])
tmp = 0
if a>=b:
    tmp = a
    a = b
    b = tmp
#print(a, b)

if b>a:
    print(b-(a+1), end='\n')
    for i in range(a+1, b):
        print(i, end=' ')

else :
    print(0)