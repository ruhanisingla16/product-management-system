from tkinter import*
from dbcon import *
# from tkinter.messagebox import showerror
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="project_work")
# mycur=con.cursor()
def add_products():
    window=Tk()
    window.title("ADD PRODUCTS")
    l1=Label(window,text="ADD PRODUCT")
    l2=Label(window,text="Product Id")
    e1=Entry(window)
    l3=Label(window,text="Product Name")
    e2=Entry(window)
    l4=Label(window,text="Product Price")
    e3=Entry(window)
    def cancel():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    def add():
        try:
            product_id=int(e1.get())
            product_name=(e2.get())
            product_price=int(e3.get())
            query=f"select count(*) from products where product_id={product_id}"
            # if(checklogin(query)):
            #     query=("insert into products(product_id,product_name,product_price) values({},'{}',{})".format(product_id,product_name,product_price))
            #     # updatetable(query)
            #     mycur.execute(query)
            #     con.commit()
            try:
                (checklogin(query))
                query=("insert into products(product_id,product_name,product_price) values({},'{}',{})".format(product_id,product_name,product_price))
                # updatetable(query)
                mycur.execute(query)
                con.commit()
                showinfo(title="progress",message="successfull")
            except mysql.connector.errors.IntegrityError as a:
                showerror(title="error",message="product already exists at this id")

                

            # else:
            #     showerror(title="error",message="product already exists at this id")
            # mycur.execute(query)
            # con.commit()
        except ValueError as e:
            showerror(title="error",message="please enter valid information.")
    b1=Button(window,text="ADD PRODUCTS",command=add)
    b2=Button(window,text="CANCEL",command=cancel)
    b3=Button(window,text="exit",command=window.destroy)
    l1.grid(row=0,columnspan=2,padx=10,pady=10,ipadx=5,ipady=5)
    l2.grid(row=1,column=0,padx=10,pady=10,ipadx=5,ipady=5)
    l3.grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5)
    l4.grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)
    e1.grid(row=1,column=1,padx=10,pady=10,ipadx=5,ipady=5)
    e2.grid(row=2,column=1,padx=10,pady=10,ipadx=5,ipady=5)
    e3.grid(row=3,column=1,padx=10,pady=10,ipadx=5,ipady=5)
    b1.grid(row=4,column=0,padx=10,pady=10,ipadx=5,ipady=5)
    b2.grid(row=4,column=1,padx=10,pady=10,ipadx=5,ipady=5)
    b3.grid(row=5,columnspan=2,padx=10,pady=10,ipadx=5,ipady=5)
    window.mainloop()
# add_products()