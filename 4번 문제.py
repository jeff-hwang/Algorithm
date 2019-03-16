def solution(pobi, crong):
    answer = 0
    if exceptCase(pobi) and exceptCase(crong):
        answer = 0
    else:
        return -1
    pobiScore = calcScore(pobi)
    crongScore = calcScore(crong)
    

    if pobiScore > crongScore:
        return 1
    elif pobiScore == crongScore:
        return 0
    else :
        return 2

def calcScore(num):
    num1 = str(num[0])
    num2 = str(num[1])
    
    
    sumVal = 0
    mulVal = 1

    sumVal1 = 0
    mulVal1 = 1
    for i in num1:
        sumVal += int(i)
    for i in num1:
        mulVal *= int(i)

    for i in num2:
        sumVal1 += int(i)
    for i in num2:
        mulVal1 *= int(i)

    return max(max(sumVal, mulVal),max(sumVal1, mulVal1))

def exceptCase(num):
    if num[0]%2==0:
        return False
    if num[1]%2!=0:
        return False
    if num[1]-num[0]!=1:
        return False
    return True



print(solution([99,102], [211,212]))