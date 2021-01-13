import random
from Tkinter import *







def rand():
    a=eval(ea.get())
    b=eval(eb.get())
    ab=random.randint(a,b)
    
    t1.insert(END,ab,"\n")
    


def close():
    sys.exit()


root=Tk()
root.title("RANDOM NUMBER GENERATOR")

a1=StringVar()
b1=StringVar()

label1=Label(root,text="ENTER THE STARTING NUMBER",font="arial 10 bold")
label1.place(x=0,y=0)

label2=Label(root,text="ENTER THE ENDING NUMBER",font="arial 10 bold")
label2.place(x=0,y=30)

ea=Entry(root,textvariable=a1,bg="lightblue")
ea.place(x=210,y=0)

eb=Entry(root,textvariable=b1,bg="lightblue")
eb.place(x=210,y=30)

t1=Text(root,width=80,height=20,bg="green",font="arial 36 bold")
t1.grid(row=9,column=1)

b1=Button(root,text="GENERATE RANDOM NUMBERS",command=rand,width=40,bg="orange",font="arial 20 bold")
b1.grid(row=9,column=0)



root.mainloop()


