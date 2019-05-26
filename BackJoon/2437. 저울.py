N = int(input())
gram = list(map(int, input().split()))
gram.sort()

if gram[0] != 1:
    print(1)
else :
    SUM = 1
    for i in range(1, N):
        if gram[i] > SUM+1:
            break
        else:
            SUM+=gram[i]
    print(SUM+1)

    
    
