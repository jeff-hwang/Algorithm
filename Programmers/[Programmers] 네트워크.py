def solution(n, computers):
    
    su = [0 for i in range(n)]
        
    for i1, v1 in enumerate(computers):
        for i2, v2 in enumerate(v1):
            su[i2] += v2

    mx = max(su)
    
    if 1 in su:
        
    else:
        return 1 

sl = solution(3, [[1,],[1,0,1],[0,1,2]])
print(sl)