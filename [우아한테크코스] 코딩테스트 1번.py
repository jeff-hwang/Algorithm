# 문제
# money 를 넣어
# 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1
# money를 최소 개수의 화폐의 정보를 return

def solution(money):
    # 결과값을 return 시킬 변수
    answer = []
    
    # 화폐 정보
    li = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

    # 반복문을 돌려 화폐를 하나씩 돌린다.
    for i in li:
        # 현재돈을 i 로 나눠 몫을 answer에 append
        answer.append(money // i)
        # 나머지 거스름돈을 money에 새로 대입
        money %= i
    return answer

money = 50237
print(solution(money))
