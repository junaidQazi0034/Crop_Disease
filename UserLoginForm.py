from atexit import register
import os
from tkinter import *
from tkinter import font
from turtle import width
from tkinter import messagebox
from click import command
import mysql.connector




def getUser():
    dbCon = mysql.connector.connect(host="localhost", user="root",password="", database="db_cropdisease")
    query ="select * from users where username=%s and password=%s"
    queryParameters =[username.get().strip(), passwd.get()]
    queryCursor = dbCon.cursor()
    queryCursor.execute(query,queryParameters)
    userData = queryCursor.fetchall()
    if userData:
        messagebox.showinfo("Login Successful", "Welcome you are Logged in successfully")
        win.destroy()
        import Main
       # os.system("Main.py")
        
    else:
            messagebox.showerror("Login Failed", "Username or password is invalid")   
   

def login():
    if username.get().strip()=="" or passwd.get()=="":
        messagebox.showerror("Fields are empty", "Fill all the fields")
    else:
        getUser()

win=Tk()
win.title("Crop Disease Detection system (Prototype)")
win.geometry("800x600+350+50")
win.resizable(False, False)
win.config(bg="#FFFDA2")

mainTitle = Label(win, text="Provide Your Login Credentials",bg="#FFFDA2",fg="black", font=("Arial Black", 28))
mainTitle.place(x=100,y=50)

Label(win,text="Enter User Name",bg="#FFFDA2", font=('courier',18)).place(x=50,y=195)
username=Entry(win, font=("arial",18))
username.place(x=300, y=190,height=50, width=400)

Label(win,text="Enter Password",bg="#FFFDA2", font=('courier',18)).place(x=50,y=305)
passwd=Entry(win, font=("arial",26), show="*")
passwd.place(x=300, y=295,height=50, width=400)

b1=Button(win, text="Submit", command=login, bg="#00A19D", fg="black", width=16, font=("arial",16))
b1.place(x=380, y=370)


win.mainloop()