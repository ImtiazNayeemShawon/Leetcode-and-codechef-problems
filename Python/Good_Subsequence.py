T = int(input())

for _ in range(T): 
    N = int(input())
    array = list(map(int, input().split()))
    if N == 1:
        print(1)
        continue
    ans = 1
    for i in range(1,N):
        if array[i] % 2 != array[i-1] % 2:
            ans += 1
    print(ans)
    
   