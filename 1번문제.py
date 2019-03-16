def solution(money):
    answer = []
    
    answer.append(money//50000)
    money%=50000
    answer.append(money//10000)
    money%=10000
    answer.append(money//5000)
    money%=5000
    answer.append(money//1000)
    money%=1000
    answer.append(money//500)
    money%=500
    answer.append(money//100)
    money%=100
    answer.append(money//50)
    money%=50
    answer.append(money//10)
    money%=10
    answer.append(money//1)
    return answer


money = 50237
print(solution(money))
