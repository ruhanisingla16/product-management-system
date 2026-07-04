from tkinter import ttk
from tkinter import *
from dbcon import *

def get_list_of_products():
    window = Tk()
    window.title("YOUR PRODUCTS")
    cols = ("product_id", "product_name", "product_price")
    tree = ttk.Treeview(window, columns=cols)
    tree.column("#0", width=0, stretch=NO)
    for x in cols:
        tree.column(x, width=80, anchor=CENTER)
        tree.heading(x, text=x, anchor=CENTER)
    results = gettable("select * from products")
    for i, x in enumerate(results):
        tree.insert(parent='', index=i, values=x)
    tree.pack()
    window.mainloop()