
def solution(clothes):
    ml = 1
    sm = 0
    dic = {}
    for i in clothes:
        dicCount(dic, i)
    
    ln = len(dic)
    if ln == 1:
        return len(clothes)
        
    for i, v in dic.items():    
        ml*=v
        sm += v
    return ml+sm

# dic , list
def dicCount(dic, li):
    try :
        dic[li[1]] +=1
    except :
        dic[li[1]] = 1



inData = [["yellow_hat", 'headgear'], \
        ['blue_sunglasses', 'eyewear'], \
        ['green_turban', 'headgear']]

print(solution(inData))
