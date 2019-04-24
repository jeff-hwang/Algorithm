lenList = int(input())

lst = input().split(' ')
rst = [int(i) for i in lst]
rst = sorted(rst)
print(rst[0], rst[lenList-1])