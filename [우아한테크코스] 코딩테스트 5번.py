# 369 게임
# 숫자 중 3 6 9 가 나온 갯수만큼 박수를 친다

def solution(number):
    answer = 0
    
    for i in range(1, number+1):
        
        for j in str(i):
            if j == '3':
                answer+=1
                
            if j == '6':
                answer+=1
                
            if j == '9':
                answer+=1            
    return answer

print(solution(33))