
from tkinter import*
import tkinter as tk

root = Tk()

root.title('Insert words') 
root.geometry('500x250') 

var1 = tk.StringVar()
l = tk.Label(root, bg='black', width = 4, textvariable = var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
    
b1 = tk.Button(root, text='print selection', command=print_selection)
b1.pack()


var2 = tk.StringVar()
var2.set((11,22,3,21,32,4))

lb = tk.Listbox(root, listvariable=var2)
list_item = [1,2,3,4]
for item in list_item:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

root.mainloop()