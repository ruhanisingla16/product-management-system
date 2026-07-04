from tkinter import *
from tkinter.messagebox import showerror, showinfo
from dbcon import *

def delete_products():
    window = Tk()
    window.title("DELETE PRODUCTS")
    
    Label(window, text="DELETE PRODUCT").grid(row=0, columnspan=2, padx=10, pady=10)
    Label(window, text="Product Id").grid(row=1, column=0, padx=10, pady=10)
    e1 = Entry(window)
    e1.grid(row=1, column=1, padx=10, pady=10)

    def delete():
        try:
            product_id = int(e1.get())
            check = f"select count(*) from products where product_id={product_id}"
            if checklogin(check):
                query = f"delete from products where product_id={product_id}"
                updatetable(query)
            else:
                showerror(title="Error", message="Product doesn't exist at this id")
        except ValueError:
            showerror(title="Error", message="Please enter a valid product ID")

    Button(window, text="DELETE", command=delete).grid(row=2, column=0, padx=10, pady=10)
    Button(window, text="CANCEL", command=lambda: e1.delete(0, END)).grid(row=2, column=1)
    Button(window, text="EXIT", command=window.destroy).grid(row=3, columnspan=2, pady=10)
    window.mainloop()