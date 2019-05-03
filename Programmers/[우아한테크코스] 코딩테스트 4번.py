'''
문제 소개

포비 랑 크롱이 있는데
책을 랜덤하게 펼치는데
왼쪽은 홀수, 오른쪽은 짝수페이지가 항상 나온다.
페이지 별로 각 자리 수를 더하거나 곱해서 가장 높은 수를 내세워
대결을 하는데
포비가 높으면 1을 return
크롱이 높으면 0을 return
그 예외 case 인경우 -1 을 return 하라
'''

def solution(pobi, crong):
    answer = 0

    # 예외 case를 계산하기 위한 문장
    if exceptCase(pobi) and exceptCase(crong):
        # 정상적인 페이지이므로 pass
        pass
    else:
        # 이상한 페이지이므로 -1 return
        return -1

    # 포비의 점수
    pobiScore = calcScore(pobi)
    # 크롱의 점수
    crongScore = calcScore(crong)
    

    if pobiScore > crongScore:
        return 1
    elif pobiScore == crongScore:
        return 0
    else :
        return 2

# 최대 점수를 계산하는 함수
def calcScore(num):
    # 왼쪽 페이지
    num1 = str(num[0])
    # 오른쪽 페이지
    num2 = str(num[1])
    
    # 왼쪽 페이지 합
    sumVal = 0
    # 왼쪽 페이지 곱
    mulVal = 1
    # 오른쪽 페이지 합
    sumVal1 = 0
    # 오른쪽 페이지 곱
    mulVal1 = 1
    for i in num1:
        sumVal += int(i)
    for i in num1:
        mulVal *= int(i)

    for i in num2:
        sumVal1 += int(i)
    for i in num2:
        mulVal1 *= int(i)

    # 가장 큰 수를 찾아내 return
    return max(max(sumVal, mulVal),max(sumVal1, mulVal1))

# 예외 처리하는 함수
def exceptCase(num):
    # 왼쪽 페이지가 짝수이면 False
    if num[0]%2==0:
        return False
    # 오른쪽 페이지가 홀수이면 False
    if num[1]%2!=0:
        return False
    # 페이지가 1만큼 차이 안나면 False 
    if num[1]-num[0]!=1:
        return False
    return True


print(solution([99,102], [211,212]))