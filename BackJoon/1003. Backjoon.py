# BackJoon 1003 번 : 피보나치 함수

# 문제에서 제시한 테스트 케이스의 갯수
n = int (input ())

# 테스트 케이스의 값
arr = [int(input()) for x in range(n)]

# 테스트 케이스들 중 최대 값
mx = max(arr)

# 한 번 구한 피보나치의 값은 계속 사용되므로 한 번 계산한 것은
# 또 다시 계산하지 않도록 저장할 피보나치 배열
fibArr = [None] * (mx+1)

# 피보나치 함수
def fib(num):
    # 피보나치를 계산하려면 초기값이 필요함

    # 초기값 0일 때의 경우
    if num == 0:
        # fibArr[0] 에 [1, 0] 을 삽입
        fibArr[num] = [1, 0]
        return [1,0]

    # 초기값 1의 경우
    if num == 1 :
        # fibArr[1] 에 [0, 1] 을 삽입
        fibArr[num] = [0, 1]
        return [0,1]
    
    # 피보나치 배열에 값이 존재한다면 그대로 리턴
    if fibArr[num] != None:
        return fibArr[num]
    
    # fibArr[num] 을 계산
    # fibArr 은 2차원 배열이므로 계산하기 복잡하니 변수를 선언해서 구함
    a = fib(num-1)
    b = fib(num-2)

    # 결과적으로 fib(num) 은  fib(num-1) + fib(num-2) 의 원소들을 각각 더한 값
    fibArr[num] = [ a[0]+b[0], a[1]+b[1] ]

    return fibArr[num]

# 출력 결과
for i in arr:
    a = fib(i)
    print("{} {}".format(a[0], a[1]))
    