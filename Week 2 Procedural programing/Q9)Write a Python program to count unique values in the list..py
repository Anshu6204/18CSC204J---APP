list=[]
n=int(input("Number of elements to be inserted in list:"))
i=0
for i in range(n):
    element=input("Enter List Element:")
    list.append(element)
l1=[]
count=0
for item in list:
    if item not in l1:
        count+=1
        l1.append(item)

print(count)

