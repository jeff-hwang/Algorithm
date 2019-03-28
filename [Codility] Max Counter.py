def solution(N, A):
    
    li = [0]*N

    mx = 0
    
    for i in A:
        if i >= 0 and i <= N:
            li[i-1] += 1
            mx = maxCalc(mx, li[i-1])
            
        else :
            li  = [mx] * N
    return li
    

def maxCalc(mx, val):
    if mx <= val:
        return val
    else :
        return mx

lst = [3,4,4,6,1,4,4]
print(solution(5,lst))
