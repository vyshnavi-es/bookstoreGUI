from tkinter import *

window=Tk()


def fun1():
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462 
    ounces=float(e1_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

b1=Label(window,text="kg")
b1.grid(row=0,column=0)

b2=Button(window,text="convert",command=fun1)
b2.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)


t1=Text(window,height=1,width=10)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=10)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=10)
t3.grid(row=1,column=2)

window.mainloop()