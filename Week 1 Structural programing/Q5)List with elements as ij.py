m=int(input("Enter number of rows:"))
n=int(input("Enter number of columns:"))
a=[[(i*j) for j in range(m)]for i in range(n)]        
print(a)