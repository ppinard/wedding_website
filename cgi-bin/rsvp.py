import cgi
import smtplib

form = cgi.FieldStorage()
name =  form.getvalue('name')
lastname =  form.getvalue('lastname')
email =  form.getvalue('email')
message =  form.getvalue('message')


#SERVER = "localhost"

FROM = 'philippe.pinard@gmail.com'

TO = ["sebrahimi1988@gmail.com"] # must be a list

SUBJECT = "New wedding guest"

TEXT = 'name: {}, lastname: {}, email: {}, allergies: {}'.format('name', 'lastname', 'email', 'message')

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP('myserver')
server.sendmail(FROM, TO, message)
server.quit()
