str1=input("Enter string1:")
str2=input("Enter string2:")
a=[]
b=[]
a.extend(str1)
b.extend(str2)
x= set(a)
y=set(b)
if x==y:
    print("Are the two strings Rationally equal?: True")
else:
    print("Are the two strings Rationally equal?: False")

