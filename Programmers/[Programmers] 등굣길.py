def solution(m, n, puddles):
    path = [[1 for j in range(n)] for i in range(m)]
    for i in puddles:
        path[i[0]-1][i[1]-1] = 0

    for i in range(1, n):
        if path[0][i]== 0 or path[0][i-1]==0:
            path[0][i] = 0

    for i in range(1, m):
        if path[i-1][0] == 0 or path[i][0]==0:
            path[i][0] = 0
        for j in range(1, n):
            if path[i][j] != 0:
                path[i][j] = path[i-1][j] + path[i][j-1]
    return path[m-1][n-1]%1000000007

solution(4,3,[[2,2]])