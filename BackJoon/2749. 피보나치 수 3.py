
N = int(input())

pb = [0 for i in range(N+1)]

pb[1] = 1
pb[2] = 1

if N >= 3:
    for i in range(3, N+1):
        pb[i] = ((pb[i-1]%1000000)+(pb[i-2]%1000000)) % 1000000

print( pb[N])

