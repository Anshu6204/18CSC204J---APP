from concurrent.futures.process import _ThreadWakeup


def testDistinct(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False

list=[]
n=int(input("Enter number of inputs:"))
for i in range(n):
    x=int(input("Enter list elements:"))
    list.append(x)
print(testDistinct(list))