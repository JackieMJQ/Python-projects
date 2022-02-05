import tkinter as tk
from tkinter import *
import pickle
from tkinter import messagebox

#overall arrangement
window = tk.Tk()
window.title('Welcome to Jackie Pyhton')
window.geometry('600x450')

#welcome image
wel_img = tk.Canvas(window, height=200, width=500)
img_file = tk.PhotoImage(file='/Users/jackie/Desktop/GUI/SignIn/welcome-youre-welcome.gif')
image = wel_img.create_image(0,0,anchor = 'nw', image = img_file)
wel_img.pack(side='top')

#user info
tk.Label(window, text='User name: ').place(x=70,y=220)
tk.Label(window, text='Password: ').place(x=70,y=260) 

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=220)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=260)

#user operation function
def usr_login(): ###store users information in a file 
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open ('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info, usr_file)
    
    #compare information users type with the database
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title ='Welcome', message= 'Welcome my GUI system! How are you?\n' + usr_name)
        else:
            tk.messagebox.showinfo(title = 'Error', message = 'Your password is wrong, plase try again!')
    else:
        sign_up = tk.messagebox.askyesno('Welcome', 'You have not signed up yet. Sign up today?')
        if sign_up:
            usr_sign_up()
            
            
#sign up function
def usr_sign_up():
    def sign_to_jackie():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error','Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error','The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome','You have successfully signed up!')
            window_sign_up.destroy()
        
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('500x300')
    window_sign_up.title('Sign up Now')
    
    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=20,y=20)
    entry_new_name =tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=200, y=20)
    
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text= 'Password: ').place(x=20,y=60)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=200, y=60)
    
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm your password: ').place(x=20, y=100)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=200, y=100)
    
    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_jackie)
    btn_confirm_sign_up.place(x=200, y=140)



#button set
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y= 300)
btn_sign_up = tk.Button(window, text='Sign up', command= usr_sign_up)
btn_sign_up.place(x=270, y=300)


window.mainloop()