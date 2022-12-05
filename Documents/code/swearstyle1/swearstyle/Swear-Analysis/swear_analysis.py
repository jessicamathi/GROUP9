import welcome
#from fpdf import FPDF
import mysql.connector
#127.0.0.1
conn = mysql.connector.connect(user='root', password='coffee123', host='127.0.0.1',database='swear')
cursor = conn.cursor()
drop_table = cursor.execute('DROP TABLE `swear`.`student`,`swear`.`cquestions`,`swear`.`pythonquestions`,`swear`.`quantquestions`,`swear`.`verbalquestions`;')
student_table = cursor.execute('create table student (id char(10),fn varchar(30),ln varchar(30),emailid varchar(50),conno char(15),password varchar(30),cstatus char(1),pythonstatus char(1),quantstatus char(1), verbalstatus char(1),primary key(id));')
cqst_table=cursor.execute('create table cquestions (sno varchar(50) NOT NULL,question varchar(255) not null,option1 varchar(255) not null,option2 char(255) not null,option3 char(255) not null,option4 char(255) not null,ans char(255) not null);')
pyqst_table=cursor.execute('create table pythonquestions(sno varchar(50) NOT NULL,question varchar(255) not null,option1 varchar(255) not null,option2 char(255) not null,option3 char(255) not null,option4 char(255) not null,ans char(255) not null);')
q_qst_table=cursor.execute('create table quantquestions(sno varchar(50) NOT NULL,question varchar(255) not null,option1 varchar(255) not null,option2 char(255) not null,option3 char(255) not null,option4 char(255) not null,ans char(255) not null);')
verb_table=cursor.execute('create table verbalquestions(sno varchar(50) NOT NULL,question varchar(255) not null,option1 varchar(255) not null,option2 char(255) not null,option3 char(255) not null,option4 char(255) not null,ans char(255) not null);')

welcome.welcome();
conn.close();