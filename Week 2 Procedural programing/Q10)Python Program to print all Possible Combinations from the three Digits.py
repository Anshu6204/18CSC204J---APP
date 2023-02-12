def combo(L):
    for i in range(3):
        for j in range(3):
            for k in range(3):

                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])

num=int(input("Enter a three digit number:"))
z=num%10
y=(num//10)%10
x=num//100
combo([x,y,z])