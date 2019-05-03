N = int(input())

arr = [list(map(int,input().split())) for i in range(N)]

ft = [[0 for i in range(31)] for j in range(31)]

for i in range(31):
    ft[i][i] = 1
    ft[i][0] = 1

for i in range(2,31):
    for j in range(i-1, -1, -1):
        ft[i][j] = ft[i-1][j-1] + ft[i-1][j]
    
for i in arr:
    print(ft[i[1]][i[0]])
       

    

