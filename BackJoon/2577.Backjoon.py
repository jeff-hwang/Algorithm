
# 인풋 데이터를 엔터로 세 번 받아야 하므로
# 컴프리헨션으로 input Data 를 3번 받아 inData 변수에 삽입한다.
inData = [int(input()) for i in range(3)]

# input으로 받은 3개의 데이터 곱의 정보를 받을 변수 선언
rstNum = 1

# inData 안의 원소를 하나씩 불러와 rstNum 에 곱한다.
for i in inData:
    rstNum = rstNum * i

#cntNum 0 부터 9까지 몇번 나왔는지 카운트 할 변수를 만듬
# 0 1 2 3 4 5 6 7 8 9 
# [0,0,0,0,0,0,0,0,0,0]

cntNum = [0 for i in range(10)]

# 곱한값(rstNum)을 문자열로 형변환하여 문자하나하나 검사하여
# cntNum 에 하나씩 카운팅 한다.
for i in str(rstNum):
    cntNum[int(i)] += 1

# 출력된 결과가 숫자가 몇 번 나왔는지 라인별로 보여주어야하니
# print() 함수를 사용하여 마무리한다.
for i in cntNum:
    print(i)
