val=input("Enter string:")
letters=digits=0
for char in val:
    if(ord(char)>=65 and ord(char)<=90):
        letters=letters+1
    elif(ord(char)>=97 and ord(char)<=122):
        letters=letters+1
    elif(ord(char)>=48 and ord(char)<=57):
        digits=digits+1
    else:
        pass
print("Number of Letter:",letters)
print("Number of Digits:",digits)

