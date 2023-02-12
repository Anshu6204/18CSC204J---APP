import random
def getRandom():
    num= random.randint(0,1)
    return num
def generateBinaryString(n):
    s= ""
    for i in range(n):
        x= getRandom()
        s=s+str(x)
    print(s)

n=int(input("Enter length of string:"))
generateBinaryString(n)