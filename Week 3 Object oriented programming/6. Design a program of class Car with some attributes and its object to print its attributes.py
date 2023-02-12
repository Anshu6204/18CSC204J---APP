class Car:
    wheels = 4
    def __init__(self, color, style):
        self.color = color
        self.style = style

style=input("Enter vehicle style:")
color=input("Enter vehicle color:")
c = Car(color, style)
print("Color of vehicle:",c.color)
print("Vehicle type:",c.style)
