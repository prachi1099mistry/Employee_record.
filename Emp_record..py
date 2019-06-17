from tkinter import *
import mysql.connector
from mysql.connector import MySQLConnection,Error
try:
    conn=mysql.connector.connect(host='localhost',database='prachi',user='root',password='root')
    print("connecting to MySQL database..")
    if conn.is_connected():
        print("Connection established")
        cursor=conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS EMP")
        cursor.execute("CREATE TABLE EMP(emp_no char(10),emp_name char(10),dept_no char(10),dateofbirth char(10))")
        print("table created successfully")

        p=Tk()
        p.title("mydatabase")
        def add():
            q=m.get()
            w=n.get()
            e=o.get()
            r=l.get()
            q1="INSERT INTO EMP(emp_no,emp_name,dept_no,dateofbirth)values('{}','{}','{}','{}')".format(q,w,e,r)
            cursor.execute(q1)
            print("row inserted successfully")

        def querry():
            print("EMP-NO\t\tEMP-NAME\tDEPT-NO\tBIRTHDAY\n")
            q2="select * from emp"
            cursor.execute(q2)
            result=cursor.fetchall()
            for row in result:
                emp_no=row[0]
                emp_name=row[1]
                dept_no=row[2]
                dateofbirth=row[3]
                print(emp_no,"\t\t",emp_name,"\t\t",dept_no,"\t\t",dateofbirth)
    
        m=StringVar()
        n=StringVar()
        o=StringVar()
        l=StringVar()
        Label(p,text="Enter records:").grid(row=0,column=1)
        Label(p,text="EMP-NO:").grid(row=1,column=0)
        Label(p,text="EMP-Name:").grid(row=2,column=0)
        Label(p,text="DEPT-NO:").grid(row=3,column=0)
        Label(p,text="Date of birth:").grid(row=4,column=0)
        Entry(p,textvariable=m).grid(row=1,column=1)
        Entry(p,textvariable=n).grid(row=2,column=1)
        Entry(p,textvariable=o).grid(row=3,column=1)
        Entry(p,textvariable=l).grid(row=4,column=1)
        Button(p,text="add",command=add).grid(row=5,column=0)
        Button(p,text="submit",command=querry).grid(row=5,column=1)
        p.mainloop()
    else:
        print("connection failed")
except Error as e:
    print(e)
finally:
    conn.commit()
    conn.close()
    print("connection closed")
print("end of program")
