from tkinter import *
from tkinter import ttk
import mysql.connector
import cquiz
import pythonquiz
import quantquiz
import verbalquiz
import welcome
import report
global sid1,fn,ln,emailid,conno,passw,window;

def report1():
    global windowsid1;
    window.destroy();
    report.function(sid1)

def function(id):
    global sid1,fn,ln,emailid,conno,passw,window;
    cnx = mysql.connector.connect(user='root', password='coffee123', host='127.0.0.1',database='swear');
    cursor=cnx.cursor();
    sql_c="select * from student where id='"+id+"';"
    cursor.execute(sql_c);
    rows=cursor.fetchall();
    for row in rows:
        print(row)
        sid=sid1=row[0];
        fn=row[1];
        ln=row[2];
        print(sid,fn,ln);
        cstatus=row[6];
        pythonstatus=row[7];
        quantstatus=row[8];
        verbalstatus=row[9];
        quizstatus=[row[6],row[7],row[8],row[9]];
    #print(sid,fn,ln);
    def welco():
        window.destroy();
        welcome.welcome();
    window = Tk();
    window.title("Swear Analysis")
    window.geometry('800x500')
    #window.configure(background = "grey");
    logout = Button(window ,text="Log-Out",command=welco).place(x = 600,y = 50)
    a = Label(window ,text = "Welcome to Swear Analysis").place(x = 300,y = 50)
    # b = Label(window ,text = "Your Name : "+fn+" "+ln).place(x = 200,y = 80)
    # c = Label(window ,text = "Student Id : "+sid).place(x = 200,y = 100)
    d = Label(window ,text = "Your Analysis Status : ").place(x = 200,y = 120)
    e = Label(window ,text = "C Quiz :").place(x = 300,y = 150)
    f = Label(window ,text = "Python Quiz :").place(x = 300,y = 170)
    g = Label(window ,text = "Quantitative Quiz :").place(x = 300,y = 190)
    h = Label(window ,text = "Verbal Quiz :").place(x = 300,y = 210)

    for row in rows:
        quizstatus = [row[6],row[7],row[8],row[9]]
    
        xpos=420;ypos=150;
        def cquizs():
            window.destroy();
            cquiz.function(sid);
        def pythonquizs():
            window.destroy();
            pythonquiz.function(sid);
        def quantquizs():
            window.destroy();
            quantquiz.function(sid);
        def verbalquizs():
            window.destroy();
            verbalquiz.function(sid);
        for i in range(0,4):
            if(quizstatus[i]=='0'):
                Label(window ,text = " Not Completed").place(x = xpos,y = ypos);
            else:
                Label(window ,text = " Completed").place(x = xpos,y = ypos);
            ypos=ypos+20;
            flag=1;
            if(quizstatus[0]=='0'):
                btn1=Button(window ,text="Click-Here",command=cquizs).place(x=600,y=150);
                flag=0;
            if(quizstatus[1]=='0'):
                btn2=Button(window ,text="Click-Here",command=pythonquizs).place(x=600,y=170);
                flag=0;
            if(quizstatus[2]=='0'):
                btn3=Button(window ,text="Click-Here",command=quantquizs).place(x=600,y=190);
                flag=0;
            if(quizstatus[3]=='0'):
                btn4=Button(window ,text="Click-Here",command=verbalquizs).place(x=600,y=210);
                flag=0;
            if flag==1:
                    btn5=Button(window ,text="Click-Here for Report",command=report1).place(x=500,y=300);
    window.mainloop()

#function("160031322")
