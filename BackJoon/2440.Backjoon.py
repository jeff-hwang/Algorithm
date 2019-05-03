
inData = int(input())

for i in range(inData):
    for j in range(inData-i):
        print('*', end="")
    print('', end="\n")
