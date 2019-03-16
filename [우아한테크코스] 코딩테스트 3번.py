'''
문제 소개

input으로 word가 주어진다.


input  >> A,B,C, .... ,X,Y,Z
output >> Z,Y,X, .... ,C,B,A

input  >> a,b,c, .... ,x,y,z
output >> z,y,x, .... ,c,b,a

이런식으로 변환하여 출력하시오.
단, 문자만 반대로 변환한다.

ex) input > I love you
    output > R olev blf
'''

from string import ascii_lowercase, ascii_uppercase

def solution(word):
    answer = ''
    
    # up 은 알파벳 대문자를 List 정보를 담고 있음
    up = list(ascii_uppercase)
    # 대문자 역순으로 재정렬
    upRvs = sorted(up, reverse=True)
    # low 는 알파벳 소문자를 List 정보를 담고 있음
    low = list(ascii_lowercase)
    # 소문자 역순으로 재정렬
    lowRvs = sorted(low, reverse=True)

    # 파라미터 word를 하나하나 검사한다.
    for i in word:
        # i가 대문자인 경우
        if (i>='A' and i<='Z'):
            # cnt 변수는 index 정보를 표현하기 위한 변수
            cnt = 0
            # 대문자 list를 하나하나 돌려 비교한다.
            for j in up:
                # i와 j 가 일치하면 answer 에다 revers된 문자를 추가
                if i==j:
                    answer+=upRvs[cnt]
                    break
                # 조건에 맞지 않다면 +1
                cnt+=1

        # i가 소문자인 경우
        elif (i>='a' and i<='z'):
            # cnt 변수는 index 정보를 표현하기 위한 변수
            cnt = 0
            for j in low:
                if i==j:
                    answer+=lowRvs[cnt]
                    break
                cnt+=1
        # i가 알파벳이 아닌경우는 그냥 answer에 붙여준다.
        else:
            answer+=i
    return answer

word = 'I love you'
print(solution(word))