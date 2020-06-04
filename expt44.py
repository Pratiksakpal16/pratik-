from tkinter import *
w=Tk()
w.geometry("500x500")
M=Menu(w)

newfile=Menu(M,tearoff=0)
newfile.add_command(label="New File")
newfile.add_separator()
newfile.add_command(label="Open")
newfile.add_command(label="Save")

Edit=Menu(M,tearoff=0)
Edit.add_command(label="Undo")
Edit.add_separator()
Edit.add_command(label="Redo")
Edit.add_command(label="Cut")

Format=Menu(M,tearoff=0)
Format.add_command(label="Indent")
Format.add_separator()
Format.add_command(label="Client")
Format.add_command(label="Paragraph")

M.add_cascade(label="File",menu=newfile)
M.add_cascade(label="Edit",menu=Edit)
M.add_cascade(label="Format",menu=Format)
w.config(menu=M)
