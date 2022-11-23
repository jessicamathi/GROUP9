import mysql.connector
import pandas as pd

pythonquestions=pd.read_csv(r'/home/shavia/Documents/swearstyle/pythonquestions.csv',encoding='latin1')

print(pythonquestions.head());

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='swear');
cursor=cnx.cursor();

for i in range(0,len(pythonquestions)):
    sno = str(pythonquestions.at[i,'sno'])
    question = str(pythonquestions.at[i,'question'])
    option1 = str(pythonquestions.at[i,'option1'])
    option2 = str(pythonquestions.at[i,'option2'])
    option3 = str(pythonquestions.at[i,'option3'])
    option4 = str(pythonquestions.at[i,'option4'])
    ans = str(pythonquestions.at[i,'ans'])
    values = sno+",'"+question+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+ans+"'";
    print(values)
    sql_c="insert into pythonquestions values ("+values+");"
    cursor.execute(sql_c);
cnx.commit();
