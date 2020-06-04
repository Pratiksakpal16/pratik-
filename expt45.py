from tkinter import *
w=Tk()
w.geometry("500x500")
l=["Mumbai","Thane","UP"]
c=StringVar()
o=OptionMenu(w,c,*l)
o.pack()
o.config(width=10)
c.set("Select City")

