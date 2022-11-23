import mysql.connector
import pandas as pd

verbalquestions=pd.read_csv(r'/home/shavia/Documents/swearstyle/pythonquestions.csv',encoding='latin1')

print(verbalquestions.head());

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='swear');
cursor=cnx.cursor();

for i in range(0,len(verbalquestions)):
    sno = str(verbalquestions.at[i,'sno'])
    question = str(verbalquestions.at[i,'question'])
    option1 = str(verbalquestions.at[i,'option1'])
    option2 = str(verbalquestions.at[i,'option2'])
    option3 = str(verbalquestions.at[i,'option3'])
    option4 = str(verbalquestions.at[i,'option4'])
    ans = str(verbalquestions.at[i,'ans'])
    values = sno+",'"+question+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+ans+"'";
    #print(values)
    sql_c="insert into verbalquestions values ("+values+");"
    cursor.execute(sql_c);
cnx.commit();
