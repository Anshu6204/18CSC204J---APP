str=input("Enter Text:")
str=str.upper()
for i in range(len(str)):
    if(len(str)==0):
        break
    ch=str[i]
    if(ch==' ' or ch=='\t'):
        continue
    count=0
    for j in range(0,len(str)):
        if(ch==str[j]):
            count=count+1
    print("The count of",ch, "is",count)
    str=str.replace(ch, ' ')
    