from tkinter import *
import registration1
import login
import portal
global main_screen
def fun1():
    global main_screen
    main_screen.destroy();
    login.function();
    
def fun2():
    global main_screen;
    main_screen.destroy();
    registration1.function();
    

def welcome():
    global main_screen
    main_screen = Tk()   
    main_screen.geometry("500x500") 
    main_screen.title("Welcome Page") 
 

    Label(text="Welcome To SWEAR ANALYSIS", bg="yellow", width="30", height="2", font=("Calibri", 13)).pack()
    Label(text="Please Login to Analyse", bg="blue", width="20", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack() 
 

    Button(text="Login", height="2", width="20", command=fun1).pack() 
    Label(text="").pack() 
 

    Button(text="Register", height="2", width="20", command=fun2).pack()
 
    main_screen.mainloop()
