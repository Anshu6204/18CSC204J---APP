str=input("Enter a string:")
for char in str:
    if(ord(char)<=122 and ord(char)>=97):
        pass
    elif(ord(char)<=90 and ord(char)>=65):
        pass
    elif(ord(char)<=57 and ord(char)>=48):
        pass
    elif(ord(char)==32):
        pass
    else:
        str=str.replace(char, " ")
print(str)