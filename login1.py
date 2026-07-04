from tkinter import*
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="project_work")
# mycur=con.cursor()
from dbcon import *
from loginscrn2 import*
from tkinter.messagebox import showerror
window=Tk()
window.title("LOGIN SCREEN")
l1=Label(window,text="LOGIN")
l2=Label(window,text="Enter Username")
e1=Entry(window)
l3=Label(window,text="Enter Password")
e2=Entry(window,show="*")
def username():
    x=(e1.get())
    y=(e2.get())
    # query=f"select count(*) from login where username='{x}' and password='{y}'"
    hashed = hash_password(y)
    query = f"select count(*) from login where username='{x}' and password='{hashed}'"
    if(checklogin(query)):
        getlogin()
    # mycur.execute(query)
    # z=mycur.fetchall()

    # if(z[0][0]==1):
    #     z=getlogin()
    #     return z
    else:
        showerror(title="error",message="incorrect information.")
def delete():
    e1.delete(0,END)
    e2.delete(0,END)
b1=Button(window,text="LOGIN",command=username)
b2=Button(window,text="CANCEL",command=delete)
b3=Button(window,text="EXIT",command=window.destroy)
l1.grid(row=0,columnspan=2,padx=10,pady=10,ipadx=5,ipady=5)
l2.grid(row=1,column=0,padx=10,pady=10,ipadx=5,ipady=5)
l3.grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5)
e1.grid(row=1,column=1,padx=10,pady=10,ipadx=5,ipady=5)
e2.grid(row=2,column=1,padx=10,pady=10,ipadx=5,ipady=5)
b1.grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)
b2.grid(row=3,column=1,padx=10,pady=10,ipadx=5,ipady=5)
b3.grid(row=5,columnspan=2,padx=10,pady=10,ipadx=5,ipady=5)
window.mainloop()



