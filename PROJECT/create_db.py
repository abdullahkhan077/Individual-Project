import sqlite3
def create_db():
    con=sqlite3.connect(database="PROJECT.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(regnum INTEGER PRIMARY KEY AUTOINCREMENT,name text,course text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS awardpoint(rid INTEGER PRIMARY KEY AUTOINCREMENT,regnum text,name text,course text, points_ob text,total_points text)")
    con.commit()

    con.close()
    
create_db()
