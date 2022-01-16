import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk


class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("RESULT")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#033050")
        self.root.focus_force()
        #====Title=====
        title=Label(self.root,text="VIEW RESULT",font=("goudy old style",20,"bold"),bg="#0676ad",fg="white").place(x=10,y=15,width=1180,height=35)
#SEARCH=====
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.root,text="Search by Reg#",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=310,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow").place(x=450,y=100,width=150)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="tomato",fg="white",cursor="hand2",command=self.search).place(x=610,y=100,width=100,height=28)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=720,y=100,width=100,height=28)
    # labels=====
        lbl_regnum=Label(self.root,text="Reg#",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_ob_marks=Label(self.root,text="Obtained Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_total_marks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)

        self.regnum=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.regnum.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self._ob_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self._ob_marks.place(x=600,y=280,width=150,height=50)
        self.total_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.total_marks.place(x=750,y=280,width=150,height=50)
        
#=====button delete====\
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=476,y=350,width=100,height=35)

#====functions====
    def search(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Reg# should be required",parent=self.root)
            else:
                cur.execute("select* from awardpoint where regnum=?",(self.var_search.get(),))
                row=cur.fetchone()
            
                if row!=None:
                    self.var_id=row[0]
                    self.regnum.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self._ob_marks.config(text=row[4])
                    self.total_marks.config(text=row[5])

                else:
                     messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
    def clear(self):
        self.var_id=""
        self.regnum.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self._ob_marks.config(text="")
        self.total_marks.config(text="")
        self.var_search.set("")
    def delete(self):    
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search student result first",parent=self.root)
            else:
                cur.execute("select * from awardpoint where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid student result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confrim","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from awardpoint where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Marks deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
             



if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()
