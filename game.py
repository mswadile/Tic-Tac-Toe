from tkinter import *
from tkinter import messagebox
a=[[3,3,3],
    [3,3,3],
    [3,3,3]]
#-----------Logic----------
def cwin():
    def win():
        global w
        global p
        w=1
        if(p==0):
            bt1.configure(text="X Win")
            bt2.configure(text="X Win")
            bt3.configure(text="X Win")
            bt4.configure(text="X Win")
            bt5.configure(text="X Win")
            bt6.configure(text="X Win")
            bt7.configure(text="X Win")
            bt8.configure(text="X Win")
            bt9.configure(text="X Win")
        else:
            bt1.configure(text="O Win")
            bt2.configure(text="O Win")
            bt3.configure(text="O Win")
            bt4.configure(text="O Win")
            bt5.configure(text="O Win")
            bt6.configure(text="O Win")
            bt7.configure(text="O Win")
            bt8.configure(text="O Win")
            bt9.configure(text="O Win")
    def draw():
        bt1.configure(text="Draw")
        bt2.configure(text="Draw")
        bt3.configure(text="Draw")
        bt4.configure(text="Draw")
        bt5.configure(text="Draw")
        bt6.configure(text="Draw")
        bt7.configure(text="Draw")
        bt8.configure(text="Draw")
        bt9.configure(text="Draw")
    #columnc
    global i,j
    if(a[0][j]==a[1][j] and a[1][j]==a[2][j]):
        win()
    #row():
    if(a[i][0]==a[i][1] and a[i][1]==a[i][2]):
        win()
    #diagonal():
    if(i==j):
        if(a[0][0]==a[1][1] and a[1][1]==a[2][2]):
            win()
    if(i==2 and j==0 or i==1 and j==1 or i==0 and j==2):
        if(a[2][0]==a[1][1] and a[1][1]==a[0][2]):
            win()
    #Draw()
    if(k==9 and w==0):
        draw()
def playerbt1():
    global p
    global cha
    global i,j,k
    i=0
    j=0
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt1.configure(text=cha)
    else:
    	cha='O'
    	a[i][j]=1
    	bt1.configure(text=cha)
    k=k+1
    cwin()
def playerbt2():
    global p
    global cha
    global i,j,k
    i=1
    j=0
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt2.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt2.configure(text=cha)
    k=k+1
    cwin()
def playerbt3():
    global p
    global cha
    global i,j,k
    i=2
    j=0
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt3.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt3.configure(text=cha)
    k=k+1 
    cwin()
def playerbt4():
    global p
    global cha
    global i,j,k
    i=0
    j=1
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt4.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt4.configure(text=cha)
    k=k+1
    cwin()
def playerbt5():
    global p
    global cha
    global i,j,k
    i=1
    j=1
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt5.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt5.configure(text=cha)
    k=k+1
    cwin()
def playerbt6():
    global p
    global cha
    global i,j,k
    i=2
    j=1
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt6.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt6.configure(text=cha)
    k=k+1
    cwin()
def playerbt7():
    global p
    global cha
    global i,j,k
    i=0
    j=2
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt7.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt7.configure(text=cha)
    k=k+1
    cwin()
def playerbt8():
    global p
    global cha
    global i,j,k
    i=1
    j=2
    if(p==0):
        p=1
    else:
        p=0
    if(p==0):
        cha='X'
        a[i][j]=0
        bt8.configure(text=cha)
    else:
        cha='O'
        a[i][j]=1
        bt8.configure(text=cha)
    k=k+1
    cwin()
def playerbt9():
    global p
    global cha
    global i,j,k
    i=2
    j=2
    if(p==0):
        p=1
    else:
        p=0
    if(p==0 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==1 and (a[i][j]==0 or a[i][j]==1)):
        messagebox.showinfo("Error","Already clicked")
    elif(p==0):
        cha='X'
        a[i][j]=0
        bt9.configure(text=cha)
    else:
        cha='O'
        bt9.configure(text=cha)
        a[i][j]=1
    k=k+1
    cwin()
window=Tk()
window.title("Tic-Tac-Toe")
window.geometry('200x225')
window.resizable(0,0)
#-----------GUI--------------
p=0
k=0
w=0
bt1=Button(window,height=4,width=8,text="",command=playerbt1)
bt1.grid(column=0,row=0)
bt2=Button(window,height=4,width=8,text="",command=playerbt2)
bt2.grid(column=0,row=1)
bt3=Button(window,height=4,width=8,text="",command=playerbt3)
bt3.grid(column=0,row=2)
bt4=Button(window,height=4,width=8,text="",command=playerbt4)
bt4.grid(column=1,row=0)
bt5=Button(window,height=4,width=8,text="",command=playerbt5)
bt5.grid(column=1,row=1)
bt6=Button(window,height=4,width=8,text="",command=playerbt6)
bt6.grid(column=1,row=2)
bt7=Button(window,height=4,width=8,text="",command=playerbt7)
bt7.grid(column=2,row=0)
bt8=Button(window,height=4,width=8,text="",command=playerbt8)
bt8.grid(column=2,row=1)
bt9=Button(window,height=4,width=8,text="",command=playerbt9)
bt9.grid(column=2,row=2)
window.mainloop()
