+





rt tkinter as tk
import sqlite3
  
root=tk.Tk()
root.geometry("600x400")

try:
    conn =  sqlite3.connect('test.db')
except Exception as e:
    print("Error in connecting",str(e)) 

c = conn.cursor()
  
name_var=tk.StringVar()
reg_var=tk.StringVar()
disp_output = ""
 
def submit():
++ 
    name=name_var.get()
    regnum=reg_var.get()
     
    print("The name is : " + name)
    print("The regnum is : " + regnum)

    c.execute("insert into students values ('"+name+"', "+regnum +")")
    conn.commit()
    print("Data inserted!")
    display()
    name_var.set("")
    reg_var.set("")

def display():
    disp_output=""
    for line in c.execute("select * from students"):
        disp_output+=str(line)
       disp_output+="\n"
    display_label = tk.Label(root,text= disp_output)
    display_label.grid(row=4,column=1)

def close():
    conn.close()
    root.destroy()    


name_label = tk.Label(root, text = 'Name', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  

reg_label = tk.Label(root, text = 'Reg No.', font = ('calibre',10,'bold'))
reg_entry=tk.Entry(root, textvariable = reg_var, font = ('calibre',10,'normal'))

sub_btn = tk.Button(root,text = 'Submit', command = submit)
close_btn = tk.Button(root,text='Close',command = close)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
reg_label.grid(row=1,column=0)
reg_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
close_btn.grid(row=3,column=1)

display()

root.mainloop()



