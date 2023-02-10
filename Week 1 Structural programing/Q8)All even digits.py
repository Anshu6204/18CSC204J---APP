for i in range(100,401,+1):
    count=0
    if((i//100)%2==0 and (i//10)%2==0 and (i%10)%2==0):
        count=count+1
    if(count==1):
        print(i)
   
