def popList(cyList):
    rst = []

    
    for i in range(len(cyList)):
        if i == 0:
            rst.append(cyList[i])                        
        elif rst[-1] != cyList[i]:
            rst.append(cyList[i])
        else:
            rst.pop()
            i+=1
        
        
    return rst

def solution(cryptogram):
    answer = ''
    cyList = list(cryptogram)
    for i in popList(cyList):
        answer+=i
    
    return answer

print(solution('browoanoommnaon'))