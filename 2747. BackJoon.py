inData = int(input())

arrFib = [None] * (inData + 1)


def fib(num):
    arrFib[0] = 0
    arrFib[1] = 1
    if num <= 1:
        return arrFib[num]
    else:
        for i in range(2, num+1):
            arrFib[i] = arrFib[i-1] + arrFib[i-2]

        return arrFib[num]


print(fib(inData))
