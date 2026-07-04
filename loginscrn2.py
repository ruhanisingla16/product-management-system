from tkinter import*
from addproduct import*
from updateproduct import*
from deleteproduct import*
from showyourproducts import*
def getlogin():
    window=Tk()
    window.title("PRODUCT MODIFICATION")
    options = {'fill' :'both','padx':10,'pady':10,'ipadx':5,'ipady':5}
    b1=Button(window,text="ADD PRODUCT",command=add_products)
    b2=Button(window,text="UPDATE PRODUCT",command=update_products)
    b3=Button(window,text="DELETE PRODUCT",command=delete_products)
    b5=Button(window,text="YOUR PRODUCTS",command=get_list_of_products)
    b6=Button(window,text="EXIT",command=window.destroy)
    b1.pack(**options)
    b2.pack(**options)
    b3.pack(**options)
    b5.pack(**options)
    b6.pack(**options)
    window.mainloop()  