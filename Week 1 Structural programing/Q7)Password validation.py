password=input("Create your password:")
for char in password:
    flag1=flag2=flag3=flag4=0
    if(ord(char)<=90 and ord(char)>=64):
        flag1=flag1+1
    elif(ord(char)<=122 and ord(char)>=97):
        flag2=flag2+1
    elif(ord(char)==35 and ord(char)==36):
        flag3=flag3+1
    elif(len(password)==6 and len(password)<=16):
        flag4=flag4+1

if(flag1>=1 and flag2>=1 and flag3>=1 and flag4>=1):
    print("Valid Password")
else:
    print("Not a Valid Password")
    
    

