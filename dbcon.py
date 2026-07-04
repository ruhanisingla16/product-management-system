from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
con = mysql.connector.connect(
    host="localhost", user="root", passwd="hello", database="project_work"
)
mycur = con.cursor()

def updatetable(query):
    try:
        mycur.execute(query)
        con.commit()
        showinfo(title="Success", message="Operation successful")
    except mysql.connector.Error as e:
        showerror(title="Error", message=str(e))

def checklogin(query):
    mycur.execute(query)
    m = mycur.fetchall()
    return m[0][0] != 0

def gettable(query):
    mycur.execute(query)
    return mycur.fetchall()