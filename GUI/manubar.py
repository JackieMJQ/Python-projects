from tkinter import*
import tkinter as tk

root = Tk()

root.title('MenuBar') 
root.geometry('500x250') 

l = tk.Label(root, bg='white', width = 20, text='empty')
l.pack()


counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1
    

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit())

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu,underline=0)
submenu.add_command(label='Submenu1', command=do_job)

root.config(menu=menubar)

root.mainloop()