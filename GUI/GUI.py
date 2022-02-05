from tkinter import*
from tkinter import font

root = Tk()

root.title('My First Window') 
root.geometry('500x250') 

var = StringVar()
MyLabel1 = Label(root, textvariable = var, bg='blue', font=('Arial', 12), width=15, 
                height=3)
MyLabel1.pack()
on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit == True
        var.set('Hello World!')
    elif on_hit == True:
        on_hit == False
        var.set('')

MyButton1 = Button(root, text='hit me', width=15, height=5, command=hit_me)
MyButton1.pack()

root.mainloop()
