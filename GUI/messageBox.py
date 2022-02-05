from tkinter import messagebox
from tkinter import*
import tkinter as tk


root = Tk()

root.title('Basic frame') 
root.geometry('500x250') 

def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='hahahaha')
    # tk.messagebox.showwarning(title='Hi', message='nonono')
    # tk.messagebox.showerror(title='Hi', message='wrong results')
    #print(tk.messagebox.askquestion(title='Hi', message='Do you like apple?'))   #return 'yes' or 'no'
    # print(tk.messagebox.askyesno(title='Hi', message='hahahaha')) #return true or false
    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))  #return true or false


tk.Button(root, text='hit me', command=hit_me).pack()


root.mainloop()