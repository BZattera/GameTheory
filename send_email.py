import smtplib

gmail_user = 'benedetta.zattera@gmail.com'
gmail_password = 'benedetta123'

sent_from = gmail_user
to = ['benedetta.zattera@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hello'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')