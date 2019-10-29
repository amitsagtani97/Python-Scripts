#!/usr/bin/python
"""
Script to send emails with python
"""
#imports
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendNotification():
    recepients_list = ["abs@gmail.com","cdf@gmail.com"]
    subject = 'Email subject'
    message = "Body message"
    sendemail(recepients_list,subject,message)

def sendemail(to_addr_list, subject, message):
    username = 'bot@gmail.com'
    password = '******'
    from_addr = 'bot@gmail.com'

    #server and port number for gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    newmessage = '\r\n'.join([
              'To: %s' %to_addr_list,
               'From: %s' % from_addr,
                'Subject: %s' %subject,
                '',
                message
                ])
    try:
        server.sendmail(from_addr, to_addr_list,newmessage)
        print 'notification sent'
    except:
        print 'error sending notification'
    server.quit()

if __name__ == "__main__":
    sendemail(["abs@gmail.com","cdf@gmail.com"],'Email subject',"Body message")
