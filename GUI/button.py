
from tkinter import*
import tkinter as tk

from show_list import print_selection

root = Tk()

root.title('Insert words') 
root.geometry('500x250') 

var = tk.StringVar()
l = tk.Label(root, bg='black', width = 20, text='empty')
l.pack()

def print_selection():
    l.config(text='You have selected '+ var.get())
    
r1 = tk.Radiobutton(root, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(root, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(root, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()


root.mainloop()