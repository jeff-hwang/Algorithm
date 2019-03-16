def list_overlap_del(input_list):
    result_list = []

    
    for i in range(len(input_list)):
        if i == 0:
            result_list.append(input_list[i])                        
        elif result_list[-1] != input_list[i]:
            result_list.append(input_list[i])
        else:
            result_list.pop()
            i+=1
        
        
    return result_list

def solution(cryptogram):
    answer = ''
    cyList = list(cryptogram)
    for i in list_overlap_del(cyList):
        answer+=i
    
    return answer

print(solution('browoanoommnaon'))