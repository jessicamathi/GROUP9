from tkinter import *
from tkinter import ttk
import mysql.connector
import welcome;
global sid1,fn,ln,emailid,conno,passw,window;
def function():
    global sid1,fn,ln,emailid,conno,passw,window;
    window = Tk()
    window.title("Registration Form")
    window.geometry('500x500')
    #window.configure(background = "grey");
    a = Label(window ,text = "First Name :").place(x = 100,y = 120)
    b = Label(window ,text = "Last Name :").place(x = 100,y = 140)
    c = Label(window ,text = "Email Id :").place(x = 100,y = 160)
    d = Label(window ,text = "Contact Number :").place(x = 100,y = 180)
    sid = Label(window ,text = "Student ID :").place(x = 100,y = 100)
    d = Label(window ,text = "Password :").place(x = 100,y = 200)
    sid1 = Entry(window)
    sid1.place(x = 250,y = 100)
    fn = Entry(window)
    fn.place(x = 250,y = 120)
    ln = Entry(window)
    ln.place(x = 250,y = 140)
    emailid = Entry(window)
    emailid.place(x = 250,y = 160)
    conno = Entry(window)
    conno.place(x = 250,y = 180)
    passw = Entry(window,show="*")
    passw.place(x = 250,y = 200)
    btn = ttk.Button(window ,text="Sign-Up",command=clicked)
    btn.place(x = 200,y = 280)
    window.mainloop()

def clicked():
    global sid1,fn,ln,emailid,conno,passw,window;
    cnx = mysql.connector.connect(user='root', password='coffee123', host='127.0.0.1',database='swear');
    #print(a1.get(),b1.get())
    print(cnx)
    cursor=cnx.cursor();
    id = sid1.get()
    fname = fn.get()
    lname = ln.get()
    email = emailid.get()
    c = conno.get()
    password = passw.get()
    
    try:
        # sql_c='insert into studentest values("'+sid1.get()+'","'+fn.get()+'","'+ln.get()+'","'+emailid.get()+'","'+conno.get()+'","'+passw.get()+'","0","0","0","0");';
        query = "insert into student(id,fn,ln,emailid,conno,password) values(%s,%s,%s,%s,%s,%s)"
        data = (id,fname,lname,email,c,password)
        cursor.execute(query,data);
        cnx.commit();
    except Error as e:
        print (e)
    msg = Label(window ,text = " You succesfully signed-up Please Close this window and continue with Login.").place(x = 50,y = 400)
    window.destroy();
    welcome.welcome();
    cnx.close()

