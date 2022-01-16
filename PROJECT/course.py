from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("MANAGE COURSE DETAILS")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#033050")
        self.root.focus_force()
        #====Title=====
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#0676ad",fg="white").place(x=10,y=15,width=1180,height=35)
        #====Variables====
        self.var_course=StringVar()
        
        #====Widgets=====
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=10,y=60)
        lbl_Description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=10,y=100)
        
        #====EntryFields====
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_courseName.place(x=150,y=60,width=200)
        self.txt_Description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_Description.place(x=150,y=100,width=500,height=200)

        #====Buttons====
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=120,height=35)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=280,y=400,width=120,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=410,y=400,width=120,height=35)
        #====search=panel=====
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="#0676ad").place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="tomato",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        #====contents====\
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        




        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"

        self.CourseTable.column("cid",width=47)
        self.CourseTable.column("name",width=47)
        self.CourseTable.column("description",width=200)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=++==++==++==++==++==++==++==++==++==++==++==++==++==
    def clear(self):
        self.show()
        self.var_course.set("")
        self.txt_Description.delete("1.0",END)
        self.txt_courseName.config(state=NORMAL)
  
    def get_data(self,ev):
        self.txt_courseName.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]

        self.var_course.set(row[1])
        self.txt_Description.delete("1.0",END)
        self.txt_Description.insert(END,row[2])

    def delete(self):    
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confrim","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course delete Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
             


    def add(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("insert into course(name,description) values(?,?)",(
                        self.var_course.get(),
                        self.txt_Description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")


    def show(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def search(self):
        con=sqlite3.connect(database="PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
        



if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()