def solution(X, A):
    # 비어있는 딕셔너리 변수
    dic = {}
    # A의 길이
    ln = len(A)

    # 0 ~ ln 까지 반복
    for i in range(ln):
        # dicCount 함수 호출
        dicCount(dic, A[i])
        
        # 딕셔너리 길이가 X 이면 인덱스 리턴
        if len(dic) == X:
            return i    

# 원소가 나왔는지 안나왔는지 검증해주는 코드
def dicCount(dic, key):
    try:
        pass

    except:
        # 원소가 나왔으면 True와 동시에 생성
        dic[key] = True

X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]

print(solution(X,A))