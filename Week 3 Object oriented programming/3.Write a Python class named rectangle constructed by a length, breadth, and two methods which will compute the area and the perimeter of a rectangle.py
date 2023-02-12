class rectangle:
    def peri_rectangle(l, b):
        peri=(2*(l+b))
        print("perimeter=",peri)
    def area_rectangle(l, b):
        area=l*b
        print("area=",area)
a=rectangle()
length=int (input ("Enter length of the rectangle: "))
width=int (input ("Enter width of the rectangle: "))
rectangle.peri_rectangle(length, width)
rectangle.area_rectangle(length,width)