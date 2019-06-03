import sys
N = int(input())
mans = list(map(int, input().split()))

res = []
for i in range(N-1, -1, -1):
    res.insert(mans[i], i+1)

for i in range(N):
    if i != N-1:
        sys.stdout.write(str(res[i])+" ")
    else:
        sys.stdout.write(str(res[i]))
'''
for i in range(N):
    if i != N-1:
        print(dic[i], end=" ")
    else:
        print(dic[i])
'''