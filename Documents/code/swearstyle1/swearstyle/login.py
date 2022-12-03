from tkinter import *
import portal
global sid, passw,main_screen1
import mysql.connector
import welcome
def sucesslogin():
    global sid, passw,main_screen1
    username=sid.get();
    password=passw.get();
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='swear');
    #print(a1.get(),b1.get())
    #print(cnx)
    cursor=cnx.cursor();
    try:
        sql_c='select * from student where id="'+username+'" and password="'+password+'";';
        print(sql_c)
        cursor.execute(sql_c);
        row=cursor.fetchall();
        if len(row)==1:
            print("sucess");
            main_screen1.destroy();
            #print(row[0][0]);
            portal.function(row[0][0]);   
        else:
            print("Fail");
    except:
        print("error");
    
    cnx.close()

def back():
    global main_screen1
    main_screen1.destroy();
    welcome.welcome()

def function():
    global sid, passw,main_screen1
    main_screen1 = Tk()   
    main_screen1.geometry("500x500") 
    main_screen1.title("Account Login") 
 
    Label(main_screen1,text="Welcome To SWEAR ANALYSIS", bg="yellow", width="30", height="2", font=("Calibri", 13)).pack()
    Label(main_screen1,text="Please Login to Analyse", bg="blue", width="20", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack() 
    Label(main_screen1,text="Enter Student ID", width="20", height="2", font=("Calibri", 13)).pack()
    sid=Entry(main_screen1,width="20")
    sid.pack()

    Label(main_screen1,text="Enter Password",width="20", height="2", font=("Calibri", 13)).pack()
    passw=Entry(main_screen1,width="20",show="*")
    passw.pack()
    
    Button(main_screen1,text="Login", height="2", width="10", bg="black",fg="white",command=sucesslogin).pack() 
    Label(text="").pack()

    Button(main_screen1,text="Back", height="2", width="10", bg="black",fg="white",command=back).pack() 
    Label(text="").pack()
    
 
    main_screen1.mainloop() 
 

