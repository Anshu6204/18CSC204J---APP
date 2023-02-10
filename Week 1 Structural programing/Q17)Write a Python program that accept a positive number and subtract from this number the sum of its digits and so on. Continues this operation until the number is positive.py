def repeat(n):
    s=str(n)
    while(n>0):
        n-=sum(int(i) for i in list(s))
        s= list(str(n))
    return n

n=int(input("Enter a number:"))
print(repeat(n))
