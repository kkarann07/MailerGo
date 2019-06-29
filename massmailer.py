from tkinter import *
from tkinter.filedialog import askopenfilename
import re
import csv
import smtplib
from email.mime.text import MIMEText

window=Tk()

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
def import_msg():
    global m
    msg_path = askopenfilename()
    print(msg_path)
    m.set(msg_path)

l1=Label(window,text="From")
l1.grid(row=0,column=0)

l2=Label(window,text="Password")
l2.grid(row=1,column=0)

l3=Label(window,text="Subject")
l3.grid(row=2,column=0)

l4=Label(window,text="Row")
l4.grid(row=3,column=0)

l5=Label(window, text="File Path")
l5.grid(row=4, column=0)

l6=Label(window,text="Message")
l6.grid(row=5,column=0)

e1_entry=StringVar()
e1=Entry(window,textvariable=e1_entry)
e1.grid(row=0,column=1)

e2_entry=StringVar()
e2=Entry(window,textvariable=e2_entry)
e2.grid(row=1,column=1)

e3_entry=StringVar()
e3=Entry(window,textvariable=e3_entry)
e3.grid(row=2,column=1)

e4_entry=StringVar()
e4=Entry(window,textvariable=e4_entry)
e4.grid(row=3,column=1)

v = StringVar()
e5 = Entry(window, textvariable=v)
e5.grid(row=4, column=1)
print(v.get())

m=StringVar()
e6=Entry(window,textvariable=m)
e6.grid(row=5,column=1)

Button(window, text='Browse Data Set',command=import_csv_data).grid(row=6, column=0)
Button(window, text='Browse message',command=import_msg).grid(row=6, column=1)

def send():
    fp = open(m.get(), 'r')
    msg = MIMEText(fp.read())
    print(msg)
    fp.close()
    msg['Subject'] = e3_entry.get()
    msg['From'] = e1_entry.get()
    emailid=e1_entry.get()
    password=e2_entry.get()
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(emailid, password)
    r = int(e4_entry.get())
    email_data = csv.reader(open(v.get(), 'r'))
    email_pattern= re.compile("^.+@.+\..+$")
    for row in email_data:
        print(row[r])
        if( email_pattern.search(row[r]) ):
            del msg['To']
            msg['To'] = row[r]
        try:
            server.sendmail(emailid, [row[r]], msg.as_string())
        except smtplib.SMTPException:
            print ("An error occured.")
    server.quit()
Button(window, text='Send Mail',command=send).grid(row=7, column=0)
Button(window, text='Close',command=window.destroy).grid(row=8, column=0)
window.mainloop()
