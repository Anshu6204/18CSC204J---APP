n=int(input('Enter a number for the pattern:'))
for i in range(n+1):
    for j in range(1,i+1):
        print("*", end=' ')
    print("\n")
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*", end=' ')
    print("\n")        
                         
    
        
