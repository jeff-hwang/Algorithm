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