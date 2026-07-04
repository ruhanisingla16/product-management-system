from tkinter import *
from tkinter.messagebox import showerror, showinfo
from dbcon import *

def update_products():
    window = Tk()
    window.title("UPDATE PRODUCTS")
    
    Label(window, text="UPDATE PRODUCT").grid(row=0, columnspan=2, padx=10, pady=10)
    Label(window, text="Product Id").grid(row=1, column=0, padx=10, pady=10)
    Label(window, text="Product Name").grid(row=2, column=0, padx=10, pady=10)
    Label(window, text="Product Price").grid(row=3, column=0, padx=10, pady=10)
    
    e1 = Entry(window)
    e2 = Entry(window)
    e3 = Entry(window)
    e1.grid(row=1, column=1, padx=10, pady=10)
    e2.grid(row=2, column=1, padx=10, pady=10)
    e3.grid(row=3, column=1, padx=10, pady=10)

    def update():
        try:
            product_id = int(e1.get())
            product_name = e2.get()
            product_price = int(e3.get())
            check = f"select count(*) from products where product_id={product_id}"
            if checklogin(check):
                query = f"update products set product_name='{product_name}', product_price={product_price} where product_id={product_id}"
                updatetable(query)
            else:
                showerror(title="Error", message="Product doesn't exist at this id")
        except ValueError:
            showerror(title="Error", message="Please enter valid information")

    Button(window, text="UPDATE", command=update).grid(row=4, column=0, padx=10, pady=10)
    Button(window, text="CANCEL", command=lambda: [e.delete(0, END) for e in [e1,e2,e3]]).grid(row=4, column=1)
    Button(window, text="EXIT", command=window.destroy).grid(row=5, columnspan=2, pady=10)
    window.mainloop()