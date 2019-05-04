import re
import csv 
import smtplib
from email.mime.text import MIMEText
fp = open('message.txt', 'r')
msg = MIMEText(fp.read())
print(msg)
fp.close()
msg['Subject'] = 'Subject goes here'
msg['From'] = 'techmints123@gmail.com'
emailid='xyz@gmail.com'
password='######'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(emailid, password)
email_data = csv.reader(open('data.csv', 'r'))
email_pattern= re.compile("^.+@.+\..+$")
for row in email_data:
    print(row[1])
    if( email_pattern.search(row[1]) ):
        del msg['To']
        msg['To'] = row[1]
    try:
        server.sendmail('techmints123@gmail.com', [row[1]], msg.as_string())
    except smtplib.SMTPException:
        print ("An error occured.")
server.quit()