from tkinter import *

root = Tk()

def angle(n):
	return 360*n/1000

Label(root, text="Pie Chart").pack()

canvas = Canvas(root, width=200, height=200)
canvas.pack()

canvas.create_arc((2,2,150,150), fill="red", outline="red", start=angle(0), extent=angle(750))
canvas.create_arc((2,2,150,150), fill="blue", outline="blue", start=angle(750), extent=angle(150))
canvas.create_arc((2,2,150,150), fill="green", outline="green", start=angle(900), extent=angle(100))

root.mainloop()