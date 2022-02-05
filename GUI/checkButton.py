from tkinter import*
import tkinter as tk

root = Tk()

root.title('Insert words') 
root.geometry('500x250') 

l = tk.Label(root, bg='black', width = 20, text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only Java')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')
    
        
var1= tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Python', variable=var1, onvalue=1, offvalue=0, 
                    command=print_selection)
c2 = tk.Checkbutton(root, text='Java', variable=var2, onvalue=1, offvalue=0, 
                    command=print_selection)

c1.pack()
c2.pack()

root.mainloop()