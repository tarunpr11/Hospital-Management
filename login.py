from tkinter import *
from tkinter import messagebox

import hospital
from hospital import *

def on_enter_user(e):
    user.delete(0,'end')
def on_enter_pass(e):
    code.delete(0,'end')
    code.config(show='*')


def on_leave(e):
    name = user.get()
    passw = code.get()
    if name == '':
        user.insert(0,'Username')
    if passw == '':
        code.insert(0,'Password')
        code.config(show='')

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '12345':
        print("Credentials Verified")
        root.destroy()
        hospital.mainPage()

    else:
        messagebox.showerror("Invalid","Invalid username and password")
    

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="white")
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=90,y=130)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter_user)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter_pass)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=234)


root.mainloop()