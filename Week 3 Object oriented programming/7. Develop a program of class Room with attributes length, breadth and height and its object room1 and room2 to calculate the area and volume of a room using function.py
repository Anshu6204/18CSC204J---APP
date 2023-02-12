class Room:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def room1(self):
        return (self.l*self.b)
    def room2(self):
        return (self.l*self.b*self.h)

length=int(input("Enter length of room:"))
breadth=int(input("Enter breadth of room:"))
height=int(input("Enter height of room:"))
ob=Room(length,breadth,height)
print("Area=",ob.room1())
print("Volume=",ob.room2())


