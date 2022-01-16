from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class markingclass:
    def __init__(self,root):
        self.root=root
        self.root.title("MARKING")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#033050")
        self.root.focus_force()
        #====Title=====
        title=Label(self.root,text="Marking",font=("goudy old style",20,"bold"),bg="#0676ad",fg="white").place(x=10,y=15,width=1180,height=50)
        #VARIABLES======
        self.var_regnum=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_ob_marks=StringVar()
        self.var_total_marks=StringVar()
        self.regnum_list=[]
        self.fetch_regnum()

        #====labels====
        lbl_select=Label(self.root,text="Select student",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=250,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=250,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=250,y=220)
        lbl_ob_marks=Label(self.root,text="Obtained Points",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=250,y=280)
        lbl_total_marks=Label(self.root,text="Total Points",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=250,y=349)
        #==entry===
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_regnum,values=(self.regnum_list),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_student.place(x=450,y=100,width=200)
        self.txt_student.set("Select")

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="tomato",fg="white",cursor="hand2",command=self.search).place(x=670,y=101,width=100,height=29)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow",state="readonly").place(x=450,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",state="readonly").place(x=450,y=220,width=320)
        txt_ob_marks=Entry(self.root,textvariable=self.var_ob_marks,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=450,y=280,width=320)
        txt_total_marks=Entry(self.root,textvariable=self.var_total_marks,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=450,y=340,width=320)
#====button====
        btn_add=Button(self.root,text="Submit",font=("goudy old style",15,"bold"),bg="limegreen",fg="white",cursor="hand2",command=self.add).place(x=410,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=540,y=420,width=120,height=35)
#====image===
    '''   self.bg_image=Image.open("images/bbb.jpg")
        self.bg_image=self.bg_image.resize((500,300),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg=Label(self.root,image=self.bg_image).place(x=630,y=100)'''
#=====functions====
    def fetch_regnum(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select regnum from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.regnum_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where regnum=?",(self.var_regnum.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])

            else:
                messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
    def add(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select * from awardpoint where regnum=? and course=?",(self.var_regnum.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Marking already done ",parent=self.root)
                else:
                    cur.execute("insert into awardpoint(regnum,name,course,points_ob,total_points) values(?,?,?,?,?)",(
                        self.var_regnum.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_ob_marks.get(),
                        self.var_total_marks.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Marking Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def clear(self):
        self.var_regnum.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_ob_marks.set(""),
        self.var_total_marks.set("")





if __name__=="__main__":
    root=Tk()
    obj=markingclass(root)
    root.mainloop()