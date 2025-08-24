Testcase = int(input()) 

for _ in range(Testcase):
    N = int(input())  
    pattern = "abacde"
    result = (pattern * ((N // len(pattern)) + 1))[:N]
    
    print(result)
