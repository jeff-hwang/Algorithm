N = int(input())
mans = list(map(int, input().split()))

dic = {}
for i in range(N-1, -1, -1):
    dic[mans[i]] = i+1
print(dic)
'''
for i in range(N):
    if i != N-1:
        print(dic[i], end=" ")
    else:
        print(dic[i])
'''