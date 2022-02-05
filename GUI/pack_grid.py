from tkinter import*
import tkinter as tk


root = Tk()

root.title('Basic frame') 
root.geometry('500x250') 


#pack()
# tk.Label(root, text=1).pack(side='top')
# tk.Label(root, text=1).pack(side='bottom')
# tk.Label(root, text=1).pack(side='right')
# tk.Label(root, text=1).pack(side='left')

#grid()
# for i in range(4):
#     for j in range(3):
#         tk.Label(root, text=1).grid(row=i, column=j, padx=10, pady=10)


#place()
tk.Label(root, text=1).place(x=10, y=100, anchor='nw' ) # anchor: direction : nw = northwest



root.mainloop()
