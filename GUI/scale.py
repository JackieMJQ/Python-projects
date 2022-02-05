from tkinter import*
import tkinter as tk

root = Tk()

root.title('Insert words') 
root.geometry('500x250') 

l = tk.Label(root, bg='black', width = 20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='You have selected '+ v)
    
s = tk.Scale(root, label='try me', from_=5, to = 11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()
    
    
    
root.mainloop()