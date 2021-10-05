import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import xlrd


def mail(name):
    passfile = "pass.xlsx"
    wb = xlrd.open_workbook(passfile)
    ws1 = wb.sheet_by_index(0)
    password = int(ws1.cell_value(0,0))

    email_user = 'aggarwalayush995@gmail.com'
    email_send = 'aggarwalayush775@gmail.com'

    subject = 'subject'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'detected some motion'
    msg.attach(MIMEText(body,'plain'))

    filename='./test/{}'.format(name)
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login(email_user,password)


    server.sendmail(email_user,email_send,text)
    server.quit()
