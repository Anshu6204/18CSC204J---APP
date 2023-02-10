
def test_number(x,y):
    if x==y or (x+y)==5 or abs(x-y)==5:
        return True
    else:
        return False
x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))
print (test_number(x,y))
