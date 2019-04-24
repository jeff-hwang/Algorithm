def solution(v):
    
    # 결과를 저장할 answer 변수
    answer = []

    print('Hello Python')

    # 파라미터 v는 2차원 List
    # v의 값이 랜덤하게 되어있으므로 정렬해준다

    # x 좌표를 오름차순으로 정렬
    v.sort(key = lambda x : x[0])
    
    # y 좌표를 오름차순으로 정렬
    v.sort(key = lambda x : x[1])
    
    # x 좌표의 정보를 가지고 있는 딕셔너리 변수    
    xDic = {}
    # y 좌표의 정보를 가지고 있는 딕셔너리 변수
    yDic = {}


    # x, y 따로 count 해준다.
    for i in v:
        count(xDic, i[0])
        count(yDic, i[1])
    
    # x 좌표 먼저 카운트 해본다.
    for k, v in xDic.items():
        # 만약 value 가 1이면 x좌표가 부족한 것이므로
        # answer에다 x좌표를 append 해준다.
        if v == 1:
            answer.append(k)
    
    # y 좌표 카운트
    for k, v in yDic.items():
        # 만약 value 가 1이면 y좌표가 부족한 것이므로
        # answer에다 y좌표를 append 해준다.
        if v == 1:
            answer.append(k)
    
    return answer

# x 좌표가 얼마나 나왔는지 카운트 해주는 사용자 정의 함수
def count(dic, value):
        try:
            # dic의 value 키 값의 value를 1증가시킴
            dic[value] = dic[value]+1
        except:
            # 예외가 발생했으면 기존에 있던 데이터가 없으므로
            # 1로 새로 만들어준다.
            dic[value] = 1


v = [[1, 1], [1, 2], [2, 2]]
print(solution(v))
