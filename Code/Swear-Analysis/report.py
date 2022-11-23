import mysql.connector
import numpy
from fpdf import FPDF
from tkinter import * 
from tkinter import messagebox as mb 
import json
global q_no
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A6
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph
from datetime import datetime

import calendar
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle


def function(id):

    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='swear');
    cursor=cnx.cursor();
    sql_c="select * from student where id="+id+";"
    cursor.execute(sql_c);
    records = cursor.fetchall()
    for row in records:
        sid=row[0];
        fnam=row[1];
        lnam=row[2];
        email=row[3]
        contactno=row[4]
        #print(sid,fnam,lnam);
        #cstatus=row[6];
        #pythonstatus=row[7];
        #quantstatus=row[8];
        #verbalstatus=row[9];
        quizstatus=[row[6],row[7],row[8],row[9]];
        print(row)

    doc = SimpleDocTemplate(fnam+'_'+lnam+'_report.pdf', pagesize=A6)
    elements = []
    data= [['Swear-Analysis Report'],['Report Generated Time',datetime.now()],['Name: ',fnam+' '+lnam],
    ["ID: ",sid],['Email-ID: ',email],['Contact No: ',contactno],['Verbal Section: ',quizstatus[3]+'/10'],['Quantitative Section',quizstatus[2]+'/10'],['Coding Section',str((int(quizstatus[0])+int(quizstatus[1]))/2)+'/10']]
    t=Table(data)
    t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
    ('TEXTCOLOR',(0,0),(1,-1),colors.black)]))
    elements.append(t)
    # write the document to disk
    doc.build(elements)


#function("160031322")
        
        
    
