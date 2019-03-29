def solution(N, A):
    # N 개의 원소를 가지고 있는 list 생성
    li = [0] * N

    # N+1 이 나왔을 때의 max 값
    mx = 0
    # 현재의 max 값
    preMx = 0

    # A의 원소를 하나하나 반복
    for i in A:
        # 원소가 N+1 이면 현재 최대 값을
        # mx 변수에 대입하여 N+1 이 실행됬는지 확인
        if i == N+1:
            mx = preMx

        # 1<=i<=N 인 경우
        else :
            # N+1 이 나온 경우 모든 원소들이 mx로 치환 됨
            # 매번 바꾸는 것이 아니라 li[i-1]이 mx 값보다 작을 때
            # 대입하고 나중에 최종적으로 한번만 더해줌
            # 매번 바꾸게 되면 O(N^2) 이지만
            # 나중에 한번 바꾸면 O(N+M)
            if li[i-1] < mx :
                li[i-1] = mx

            # i-1 의 인덱스를 1증가
            li[i-1] +=1

            # 현재 최대 값을 연산
            if preMx < li[i-1]:
                preMx = li[i-1]

        print(li)

    # N 만큼 반복
    for i in range(N):
        # 만약 N+1 발생된 mx 값보다 li[i] 가 작으면
        # mx를 대입해줌
        if li[i] < mx :
            li[i] = mx

    # li return        
    return li

lst = [3,4,4,6,1,4,4]
print(solution(5,lst))
