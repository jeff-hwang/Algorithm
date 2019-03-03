#문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

#iData = [i for i in input().split('\n')]
#print(iData)
#iDataLen = len(iData)

iData = []
for i in range(4):
    iData.append(input())


for i in iData:
    if 'A'<=i[0] and 'Z'>=i[0]:
        ln = len(i)
        print(i[0]+i[ln-1])
