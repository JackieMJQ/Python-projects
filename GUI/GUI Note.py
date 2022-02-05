from tkinter import*
from tkinter import font

root = Tk()

root.title('My First Window') ###标题名
root.geometry('200x100') ###窗口大小

var = StringVar()#设置变量
MyLabel1 = Label(root, textvariable = var, bg='blue', font=('Arial', 12), width=15, 
                height=3) ###标签 文字内容， 背景， 字体， 标签的宽度 长度（数字代表一个字符）
MyLabel1.pack()
on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit == True
        var.set('Hello World!')#设置上面text 
    else:
        on_hit == True
        var.set('')#再点击就空了

MyButton1 = Button(root, text='hit me', width=15, height=5, command=hit_me)#按钮
MyButton1.pack()

root.mainloop()
