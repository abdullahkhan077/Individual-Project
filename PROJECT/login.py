#EMAIL IS abc@cui.com
#PASSWORD IS 1234


from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk
import os
import sys

class loginClass:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
#=====Variables=====
        self.var_email=StringVar()
        self.var_password=StringVar()
#====BackgroundImage++++=
        self.kk_image=Image.open("images/4455.jpg")
        self.kk_image=ImageTk.PhotoImage(self.kk_image)
        self.lbl_kk=Label(self.root,image=self.kk_image).place(x=0,y=0,width=1366,height=750)
#====Entry Fields=====
        txt_email=Entry(textvariable=self.var_email,font=("goudy old style",20,"bold"))
        txt_email.place(x=485,y=280,width=320)
        txt_password=Entry(textvariable=self.var_password,font=("goudy old style",20,"bold"))
        txt_password.place(x=485,y=345,width=320)
#=====Buttons===== 
        btn_search=Button(self.root,text="LOGIN",font=("goudy old style",15,"bold"),bg="purple",cursor="hand2",command=self.login).place(x=560,y=415,width=150,height=30)
 
#=====labels===== 
        lbl_email=Label(self.root,text="EMAIL",font=("goudy old style",15,"bold"),bg="purple").place(x=485,y=251)
        lbl_password=Label(self.root,text="PASSWORD",font=("goudy old style",15,"bold"),bg="purple").place(x=485,y=316)
        

    def login(self):
        if self.var_email.get()=="abc@cui.com":
            if self.var_password.get()=="1234":
                self.root.destroy()
                os.system("python dashboard.py")

                
                
        
            
        else:
            messagebox.showerror("Error","Login Unsuccessful")

            



if __name__=="__main__":
    root=Tk()
    obj=loginClass(root)
    root.mainloop()    