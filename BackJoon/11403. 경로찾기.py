N = int(input())
data = [list(map(int, input().split(" "))) for i in range(N)]
path = [[0 for i in range(N)] for i in range(N)] # 경로

for i, iv in enumerate(data):
    path[i][i] = 1
    for j, jv in enumerate(iv):
        if jv == 1 :
            path[i][j] = 1
            path[j][i] = 1


for i in path:
    for j in i:
        print(j, end=' ')
    if i != N-1:
        print()
        
