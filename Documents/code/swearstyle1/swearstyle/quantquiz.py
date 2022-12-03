import mysql.connector
import numpy
from tkinter import *
from tkinter import messagebox as mb
import json
import portal
global q_no

def function(id):

    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='swear');
    cursor=cnx.cursor();

    questions=[];
    flag=0;
    while(flag==0):
        num=numpy.random.randint(1,50);
        if num not in questions:
            questions.append(num);
        if len(questions)==10:
            flag=1;
    #print(questions);
    questions.sort();
    questions=str(questions)
    questions='('+ questions[1:-1] +')'
    #print(questions);
    sql_c="select * from quantquestions where sno in "+questions+";"
    cursor.execute(sql_c);
    records = cursor.fetchall()
    question=[];
    options=[];
    answer=[];
    ans1={'A':1,'B':2,'C':3,'D':4}

    for row in records:        
            question.append(row[1]);
            op=[row[2],row[3],row[4],row[5]]
            options.append(op);
            print(row[6].strip())
            answer.append(ans1[row[6].strip()])


 
    class Quiz:

        def __init__(self):
        
            #self.display_question.delete(1.0,END) 
            self.q_no=0
         
            self.display_title()
            self.display_question()
         
            self.opt_selected=IntVar()
         
            self.opts=self.radio_buttons()

            self.display_options()
         
            self.buttons()
         
            # no of questions
            self.data_size=len(question)
         
            # keep a counter of correct answers
            self.correct=0

        def display_result(self):
         
            wrong_count = self.data_size - self.correct
            correct = f"Correct: {self.correct}"
            wrong = f"Wrong: {wrong_count}"

            score = int(self.correct / self.data_size * 100)
            result = f"Score: {score}%"
         
            mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
            sql_c="update student set quantstatus='"+str(self.correct)+"' where id='"+id+"';";
            cursor.execute(sql_c);
            cnx.commit();
            print("sucess")
 
        def check_ans(self, q_no):

            if self.opt_selected.get() == answer[q_no]:
                return True

        def next_btn(self):
            q_no.config(text="")

            #print(self.q_no)
         
            if self.check_ans(self.q_no):
             
                self.correct += 1
         
            self.q_no += 1
         
            if self.q_no==self.data_size:
             
                self.display_result()
             
                gui.destroy()
                portal.function(id)
            else:
                self.display_question()
                self.display_options()
 
 

        def buttons(self):
         

            next_button = Button(gui, text="Next",command=self.next_btn,
            width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
         
            # palcing the button  on the screen
            next_button.place(x=750,y=700)
        
         

            quit_button = Button(gui, text="Quit", command=gui.destroy,
            width=5,bg="black", fg="white",font=("ariel",16," bold"))
         

            quit_button.place(x=1200,y=50)
 

        def display_options(self):
            val=0
         
            self.opt_selected.set(0)
         
            for option in options[self.q_no]:
                self.opts[val]['text']=option
                val+=1
 
 
        def display_question(self):
            global q_no
            #self.delete(1.0,END)
            q_no = Label(gui, width=99,text=question[self.q_no], justify="left",font=( 'ariel' ,16, 'bold' ), anchor= 'w', wraplength=1000 );
            #q_no.config(text=question[self.q_no])
         
            q_no.place(x=70, y=100)
 
 
        def display_title(self):
         

            title = Label(gui, text="Quant Section",
            width=99, bg="green",fg="white", font=("ariel", 20, "bold"))
         
            title.place(x=0, y=2)
 
        def radio_buttons(self):
         
            q_list = []
         
            y_pos = 300
            x_pos=100
            while len(q_list) < 4:
             
                radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
                value = len(q_list)+1,font = ("ariel",14), wraplength=200)
             
                q_list.append(radio_btn)
             
                radio_btn.place(x = x_pos, y = y_pos)
             
                x_pos += 300
         
            return q_list

    gui = Tk() 
    gui.geometry("1550x850")
    gui.title("Quant Section")
    question = (question)
    options = (options)
    answer = (answer)
    quiz = Quiz()
    gui.mainloop()
#function("160031322")
#create table student (id char(10),fname varchar(30),lname varchar(30),email varchar(50),contactno char(10), password varchar(30), cstatus char(1), pythonstatus char(1), quantstatus char(1), verbalstatus char(1), primary key(id));
