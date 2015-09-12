#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMail:
    def __init__(self):
        pass

    def send(self):

        username = "forblackking@gmail.com"
        password = "**************"

        # username = "354016028@qq.com"
        # password = "***************"

        to = ['forblackking@qq.com']
        msg = MIMEMultipart()
        msg['Subject'] = 'Test'
        content = MIMEText('test', 'plain', 'utf-8')
        msg.attach(content)

        s = smtplib.SMTP('smtp.gmail.com')
        # s = smtplib.SMTP('smtp.qq.com')

        #   gmail support
        s.ehlo()
        s.starttls()
        #
        try:
            s.login(username, password)
            s.sendmail(username, to, msg.as_string())
            print('Success.')
        except smtplib.SMTPException as e:
            print("Fail.", e)
        finally:
            s.close()

if __name__ == '__main__':
    newmail=SendMail()
    newmail.send()


