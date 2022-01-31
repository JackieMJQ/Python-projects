from tkinter import*
from tkinter import font
import tkinter as tk

root = Tk()

root.title('Insert words') 
root.geometry('500x250') 

entry = tk.Entry(root, show = '*')
entry.pack()

def insert_point():
    var = entry.get()
    t.insert('insert', var)
    
def insert_end():
    var = entry.get()
    t.insert('end', var)
    

MyButton1 = Button(root, text='insert point', command=insert_point)
MyButton1.pack()

b2 = tk.Button(root, text='insert end', command = insert_end)
b2.pack()

t = tk.Text(root,height=2)
t.pack()
root.mainloop()