from tkinter import*
from tkinter import messagebox
from random import*
import sys
import os
f = Tk()
f.title("เกมบันไดงู")
z1 = [0]
z2 = [0]
lb = Label(f,height=700,width=700,background="light blue")
lb.place(x=0,y=0)
ls = Label(f,text='start',height=8,width=13,background="yellow",foreground="black")
ls.place(x=490,y=429) #y+100

l1 = Label(f,text='1',height=5,width=8,background="green",foreground="white")
l1.place(x=420,y=450)

l2 = Label(f,text='2',height=5,width=8,background="red",foreground="white")
l2.place(x=352,y=450)

l3 = Label(f,text='3',height=5,width=8,background="green",foreground="white")
l3.place(x=284,y=450)

l4 = Label(f,text='4',height=5,width=8,background="red",foreground="white")
l4.place(x=216,y=450)

#snake
l4_1 = Label(f,height=1,width=8,background="black")
l4_1.place(x=216,y=450)

l4_2 = Label(f,height=1,width=8,background="red")
l4_2.place(x=216,y=430)

l4_3 = Label(f,height=1,width=8,background="black")
l4_3.place(x=216,y=410)

l4_4 = Label(f,height=1,width=8,background="red")
l4_4.place(x=216,y=390)

l4_3 = Label(f,height=1,width=8,background="black")
l4_3.place(x=216,y=370)

l4_4 = Label(f,height=1,width=8,background="red")
l4_4.place(x=216,y=350)
#

l5 = Label(f,text='5',height=5,width=8,background="green",foreground="white")
l5.place(x=148,y=450)

l6 = Label(f,text='6',height=5,width=8,background="red",foreground="white")
l6.place(x=80,y=450)

l7 = Label(f,text='7',height=5,width=8,background="green",foreground="white")
l7.place(x=80,y=362)

l8 = Label(f,text='8',height=5,width=8,background="red",foreground="white")
l8.place(x=80,y=274)

l9 = Label(f,text='9',height=5,width=8,background="green",foreground="white")
l9.place(x=148,y=274)

l10 = Label(f,text='10',height=5,width=8,background="red",foreground="white")
l10.place(x=216,y=274)

l11 = Label(f,text='11',height=5,width=8,background="green",foreground="white")
l11.place(x=284,y=274)

#ladders
l4_1 = Label(f,height=1,width=8,background="black")
l4_1.place(x=284,y=254)

l4_3 = Label(f,height=1,width=8,background="black")
l4_3.place(x=284,y=214)

l4_3 = Label(f,height=1,width=8,background="black")
l4_3.place(x=284,y=174)

l4_4 = Label(f,height=6,width=1,background="black")
l4_4.place(x=284,y=174)

l4_5 = Label(f,height=6,width=1,background="black")
l4_5.place(x=333,y=174)
#

l12 = Label(f,text='12',height=5,width=8,background="red",foreground="white")
l12.place(x=352,y=274)

l13 = Label(f,text='13',height=5,width=8,background="green",foreground="white")
l13.place(x=420,y=274)

l14 = Label(f,text='14',height=5,width=8,background="red",foreground="white")
l14.place(x=420,y=188)

l15 = Label(f,text='15',height=5,width=8,background="green",foreground="white")
l15.place(x=420,y=100)

l16 = Label(f,text='16',height=5,width=8,background="red",foreground="white")
l16.place(x=352,y=100)

l17 = Label(f,text='17',height=5,width=8,background="green",foreground="white")
l17.place(x=284,y=100)

l18 = Label(f,text='18',height=5,width=8,background="red",foreground="white")
l18.place(x=216,y=100)

l19 = Label(f,text='19',height=5,width=8,background="green",foreground="white")
l19.place(x=148,y=100)

lg = Label(f,text='Goal',height=8,width=13,background="orange",foreground="black")
lg.place(x=45,y=79)

def random_1():
    x1 = randint(1,6)
    lb_1 = Label(f,text=x1)
    lb_1.place(x=420,y=580)
    z1.append(x1)
    a = sum(z1)
    if a == 1:
        l1.place(x=420,y=450)
    elif a == 2:
        l1.place(x=352,y=450)
    elif a == 3:
        l1.place(x=284,y=450)
    elif a == 4 or a == 10:
        l1.place(x=216,y=450)
    elif a == 5 or a == 11  :
        l1.place(x=148,y=450)
    elif a == 6 or a ==12  :
        l1.place(x=80,y=450)
    elif a == 7 or a == 13 :
        l1.place(x=80,y=362)
    elif a == 8 or a == 14 :
        l1.place(x=80,y=274)
    elif a == 9 or a == 15 :
        l1.place(x=148,y=274)
    elif a == 11   :
        l1.place(x=284,y=274)
    elif a == 12  :
        l1.place(x=352,y=274)
    elif a == 13  :
        l1.place(x=420,y=274)
    elif a == 14  :
        l1.place(x=420,y=188)
    elif a == 15  :
        l1.place(x=420,y=100)
    elif a == 16 :
        l1.place(x=352,y=100)
    elif a == 17 or a ==11 :
        l1.place(x=284,y=100)
    elif a == 18:
        l1.place(x=216,y=100)
    elif a == 19:
        l1.place(x=148,y=100)
    elif a >= 20:
        l1.place(x=80,y=109)
        f.geometry("200x100")
        messagebox.showinfo("END GAME","Player1 WIN")

l1 = Label(f,text='1',height=3,width=3,background="white",foreground="black")
l1.place(x=490,y=429)

b1 = Button(f,text='Player1',command=random_1)
b1.place(x=470,y=580)

def random_2():
    x2 = randint(1,6)
    lb_2 = Label(f,text=x2)
    lb_2.place(x=420,y=630)
    z2.append(x2)
    
    a = sum(z2)
    if a == 1:
        l2.place(x=455,y=480) #x+35 y+30
    elif a == 2:
        l2.place(x=387,y=480)
    elif a == 3:
        l2.place(x=319,y=480)
    elif a == 4 or a == 10:
        l2.place(x=251,y=480)
    elif a == 5 or a== 11 :
        l2.place(x=183,y=480)
    elif a == 6 or a==12 :
        l2.place(x=115,y=480)
    elif a == 7 or a==13 :
        l2.place(x=115,y=392)
    elif a == 8 or a==14 :
        l2.place(x=115,y=304)
    elif a == 9 or a ==15 :
        l2.place(x=183,y=304)
    elif a == 11  :
        l2.place(x=319,y=304)
    elif a == 12   :
        l2.place(x=387,y=304)
    elif a == 13  :
        l2.place(x=455,y=304)
    elif a == 14  :
        l2.place(x=455,y=218)
    elif a == 15 :
        l2.place(x=455,y=130)
    elif a == 16  :
        l2.place(x=387,y=130)
    elif a == 17 or a == 11:
        l2.place(x=319,y=130)
    elif a == 18:
        l2.place(x=251,y=130)
    elif a == 19:
        l2.place(x=183,y=130)
    elif a >= 20:
        l2.place(x=80,y=109)
        f.geometry("200x100")
        messagebox.showinfo("END GAME","Player2 WIN")

l2 = Label(f,text='2',height=3,width=3,background="grey",foreground="white")
l2.place(x=560,y=429)

b2 = Button(f,text='Player2',command=random_2)
b2.place(x=470,y=630)


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
   

menubar = Menu(f)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = restart)

filemenu.add_separator()
menubar.add_cascade(label = "File", menu = filemenu)


f.config(menu = menubar)


f.minsize(700,700)
f.maxsize(700,700)
f.mainloop()
