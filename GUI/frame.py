from tkinter import*
import tkinter as tk

root = Tk()

root.title('Basic frame') 
root.geometry('500x250') 
tk.Label(root, text='on the window').pack()

frm = tk.Frame(root)
frm.pack()
frm_L = tk.Frame(frm)
frm_R = tk.Frame(frm)
frm_L.pack(side='left')
frm_R.pack(side='right')

tk.Label(frm_L, text='on the left frame 1').pack()
tk.Label(frm_L, text='on the left frame 2').pack()
tk.Label(frm_R, text='on the right frame 1').pack()

root.mainloop()
