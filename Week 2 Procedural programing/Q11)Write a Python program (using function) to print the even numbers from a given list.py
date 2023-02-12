def isEven(num):
    if(num%2==0):
        print(num," is even")
    
list=[]
n=int(input("Enter number of elements to be added in the list:"))
for i in range(n):
    a=int(input("Enter a number:"))
    list.append(a)

for i in range(n):
    isEven(list[i])