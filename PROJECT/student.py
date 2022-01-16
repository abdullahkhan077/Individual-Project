from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class studentclass:
    def __init__(self,root):
        self.root=root
        self.root.title("MANAGE STUDENT DETAILS")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#033050")
        self.root.focus_force()
        #====Title=====
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#0676ad",fg="white").place(x=10,y=15,width=1180,height=35)
        #====Variables====
        self.var_regnum=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        
        #====Widgets=====
        lbl_regnum=Label(self.root,text="Reg#",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=10,y=100)

        
        #====EntryFields====
        self.txt_regnum=Entry(self.root,textvariable=self.var_regnum,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_regnum.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_name.place(x=150,y=100,width=200)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=10,y=140)
        self.course_list=[]
        self.fetch_course()


        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=(self.course_list),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=150,y=140,width=200)
        self.txt_course.set("Select")
        

        #====Buttons====
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=140,y=390,width=120,height=35)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="ORANGERED",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=390,width=110,height=35)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=390,width=110,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=390,width=110,height=35)
        #====search=panel=====
        self.var_search=StringVar()
        lbl_search_regnum=Label(self.root,text="Reg#",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=720,y=60)
        txt_search_course=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="tomato",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        #====contents====\
        self.c_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_Frame.place(x=720,y=100,width=470,height=340)

        scrollx=Scrollbar(self.c_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.c_Frame,orient=VERTICAL)
        




        self.CourseTable=ttk.Treeview(self.c_Frame,columns=("regnum","name","course"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("regnum",text="Reg #")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable["show"]='headings'

        self.CourseTable.column("regnum",width=47)
        self.CourseTable.column("name",width=47)
        self.CourseTable.column("course",width=200)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#Functionbuttons
#=++==++==++==++==++==++==++==++==++==++==++==++==++==
    def clear(self):
        self.show()
        self.var_regnum.set(""),
        self.var_name.set(""),
        self.var_course.set("SELECT"),
        self.txt_regnum.config(state=NORMAL),
        self.var_search.set("")        
#=====getdata=========
    def get_data(self,x):
        self.txt_regnum.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_regnum.set(row[0]),                       
        self.var_name.set(row[1])
                           
#=====delete=====

    def delete(self):    
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_regnum.get()=="":
                messagebox.showerror("Error","Roll number is required",parent=self.root)
            else:
                cur.execute("select * from student where regnum=?",(self.var_regnum.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confrim","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where regnum=?",(self.var_regnum.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleteted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
             

#=====add========
    def add(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_regnum.get()=="":
                messagebox.showerror("Error","Reg# should be required",parent=self.root)
            else:
                cur.execute("select* from student where regnum=?",(self.var_regnum.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Reg# already present",parent=self.root)
                else: 
                    cur.execute("insert into student(regnum,name,course) values(?,?,?)" ,(
                        self.var_regnum.get(),
                        self.var_name.get(),
                        self.var_course.get()     
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

#====Update=====

    def update(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_regnum.get()=="":
                messagebox.showerror("Error","Roll Number Should Be Required",parent=self.root)
            else:
                cur.execute("select * from student where regnum=?",(self.var_regnum.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student from List",parent=self.root)
                else:
                    cur.execute("update student set name=?,course=? where regnum=?",(

                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_regnum.get(),           
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfuly",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")




    def show(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

#======fetchcourse=======

    def fetch_course(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")


#=====searchbutton===


    def search(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where regnum=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert("",END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
        



if __name__=="__main__":
    root=Tk()
    obj=studentclass(root)
    root.mainloop()