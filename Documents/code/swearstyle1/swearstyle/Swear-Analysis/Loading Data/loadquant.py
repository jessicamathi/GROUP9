import mysql.connector
import pandas as pd

quantquestions=pd.read_csv(r'/home/shavia/Documents/swearstyle/pythonquestions.csv',encoding='latin1')

print(quantquestions.head());

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='swear');
cursor=cnx.cursor();

for i in range(0,len(quantquestions)):
    sno = str(quantquestions.at[i,'sno'])
    question = str(quantquestions.at[i,'question'])
    option1 = str(quantquestions.at[i,'option1'])
    option2 = str(quantquestions.at[i,'option2'])
    option3 = str(quantquestions.at[i,'option3'])
    option4 = str(quantquestions.at[i,'option4'])
    ans = str(quantquestions.at[i,'ans'])
    values = sno+",'"+question+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+ans+"'";
    print(values)
    sql_c="insert into quantquestions values ("+values+");"
    cursor.execute(sql_c);
cnx.commit();
