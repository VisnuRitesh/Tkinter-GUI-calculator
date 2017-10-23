import tkinter
from tkinter import *

c=0

def add():
    global c
    a=e1.get()
    b=e2.get()
    c=int(a)+int(b)
    Label(mw,text=c).grid(row=2)

def sub():
    global c
    a=e1.get()
    b=e2.get()
    c=int(a)-int(b)
    Label(mw,text=c).grid(row=2)

def mul():
    global c
    a=e1.get()
    b=e2.get()
    c=int(a)*int(b)
    Label(mw,text=c).grid(row=2)

def div():
    global c
    a=e1.get()
    b=e2.get()
    c=int(a)/int(b)
    Label(mw,text=c).grid(row=2)

mw=tkinter.Tk()
mw.title('Calculator')

e1=Entry(mw)
e2=Entry(mw)
e1.grid(row=0)
e2.grid(row=1)

Button(mw,text='+',command=add).grid(row=3,column=0)
Button(mw,text='-',command=sub).grid(row=3,column=1)
Button(mw,text='*',command=mul).grid(row=4,column=0)
Button(mw,text='/',command=div).grid(row=4,column=1)
#eb=Button(mw,text='=',command=).grid(column=3)

mainloop()
