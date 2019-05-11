def solution(N):
    answer = [ "" ]
    MAX = len(N)
    dic = {1:0, 2:0, 3:0, 4:0}
    
    for i in N:
        makeDic(dic, i)
    res = dic[4]
    res += dic[1]//4
    res += dic[2]//2
    
    dic[1]%=4
    dic[2]%=2

    if dic[2]!=0 or dic[3]!=0:
        res+= dic[2]
        res+= dic[3]
        return res
    else :
        res+=1
        return res 
def makeDic(dic, k):
    dic[k] += 1
    
    

print(solution([1,2,4,3,3]))