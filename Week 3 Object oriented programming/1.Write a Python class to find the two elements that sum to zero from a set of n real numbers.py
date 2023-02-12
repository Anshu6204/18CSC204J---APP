class sumzero:
    def twosum(self,a):
        b=[]
        i=0
        while i<len(a)-1:
            j=i+1
            while j<len(a):
                if(a[i]+a[j]==0):
                    b.append([a[i],a[j]])
                    j=j+1
                else:
                    j=j+1
            i=i+1
        return b

a=[]
n=int(input("Number of elements to be in the list:"))
for i in range(0,n):
    x=int(input("Enter array elements:"))
    a.append(x)
print(sumzero().twosum(a))