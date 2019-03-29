def solution(N, A):
    
    li = [0] * N
    mx = 0
    preMx = 0
    for i in A:
        if i == N+1:
            mx = preMx
        else :
            if li[i-1] < mx :
                li[i-1] = mx
            li[i-1] +=1
            if preMx < li[i-1]:
                preMx = li[i-1]
        print(li)
    for i in range(N):
        if li[i] < mx :
            li[i] = mx
    return li

lst = [3,4,4,6,1,4,4]
print(solution(5,lst))
