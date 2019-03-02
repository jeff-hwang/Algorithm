inData = [int(input()) for i in range(3)]

rstNum = 1
for i in inData:
    rstNum = rstNum*i

cntNum = [0 for i in range(10)]

for i in str(rstNum):
    cntNum[int(i)]+=1

for i in cntNum:
    print(i)
