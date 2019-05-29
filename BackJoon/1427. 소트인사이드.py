N = input()
arr = [i for i in N]
arr.sort(key=lambda x : int(x), reverse= True)
print("".join(arr))

    
