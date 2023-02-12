def isPrime(num):
    count=0
    for i in range(2,num+1):
        if (num%i==0):
            count+=1
    if(count==1):
        return 1
    else:
        return 0

n=int(input("Enter a number:"))
if(isPrime(n)):
    print(n," is a prime number")
else:
    print(n," is a composite number")